# AI Study Assistant

## Overview

AI-powered learning platform that combines LLMs and Retrieval-Augmented Generation (RAG) to provide document-aware tutoring, quiz generation, automated assessment, and semantic PDF question answering.

## Features

- AI Tutor
- Quiz Generation
- Quiz Evaluation
- PDF Upload
- Semantic Search
- RAG-based Question Answering

## Tech Stack

### Frontend

- React
- Tailwind CSS

### Backend

- FastAPI
- Pydantic

### AI

- OpenRouter
- Sentence Transformers

### RAG

- ChromaDB
- Semantic Search
- PDF Processing

## Architecture

                    ┌──────────────┐
                    │   React UI   │
                    └──────┬───────┘
                           │
                           ▼
                  ┌────────────────┐
                  │    FastAPI     │
                  └───────┬────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼

  AI Assistant      Quiz Engine       PDF Pipeline

        │                 │                 │
        ▼                 ▼                 ▼

   OpenRouter       OpenRouter      Text Extraction
      LLM              LLM           Chunking
                                           │
                                           ▼
                                   SentenceTransformers
                                           │
                                           ▼
                                       ChromaDB
                                           │
                                           ▼
                                     Semantic Search

## Setup

### Backend

pip install -r requirements.txt

uvicorn app.main:app --reload

### Frontend

npm install

npm run dev

## Future Improvements

- Authentication
- User Accounts
- Learning Analytics
- Study Progress Tracking