import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_ai(model: str, messages: list):

    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": model,
        "messages": messages
    }

    data_bytes = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data_bytes,
        method="POST"
    )

    req.add_header(
        "Authorization",
        f"Bearer {API_KEY}"
    )

    req.add_header(
        "Content-Type",
        "application/json"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode("utf-8")
            result = json.loads(resp_body)

    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")

        return {
            "error": json.loads(err_body)
        }

    return result