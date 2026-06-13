from fastapi import APIRouter, UploadFile, File, HTTPException
from pypdf import PdfReader
from app.services.chunking import chunk_text
from app.services.vector_store import store_chunks
from app.services.vector_store import search_chunks
from app.services.ai_service import call_ai
from app.models.schemas import SearchRequest,AskPdfRequest
from pydantic import BaseModel
import os
UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf" or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    reader = PdfReader(file_path)

    total_pages = len(reader.pages)

    extracted_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            extracted_text += text + "\n"
        if not extracted_text.strip():
            return {
            "error": "No extractable text found in PDF."
        }
    
    chunks = chunk_text(extracted_text)
    store_chunks(chunks)
    return {
        "filename": file.filename,
        "pages": total_pages,
        "characters": len(extracted_text),
        #"preview": extracted_text[:500],
        "chunks_count": len(chunks),
        "first_chunk": chunks[0] if chunks else "",
        "stored": True
    }

@router.post("/search")
def search_document(data: SearchRequest):

    results = search_chunks(
        data.query
    )

    return {
        "results": results
    }

@router.post("/ask-pdf")
def ask_pdf(data: AskPdfRequest):

    context_chunks = search_chunks(
        data.question
    )

    context = "\n\n".join(context_chunks)

    messages = [
        {
            "role": "system",
            "content": """
            Answer ONLY using the provided context.
            If the answer is not found, say:
            'Information not found in the document.'
            """
        },
        {
            "role": "user",
            "content": f"""
            Context:
            {context}

            Question:
            {data.question}
            """
        }
    ]

    result = call_ai(
        "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        messages = messages
    )

    answer = result["choices"][0]["message"]["content"]

    return {
        "answer": answer,
        "sources": context_chunks
    }