import httpx
import os
from dotenv import load_dotenv

load_dotenv()

r = httpx.post(
    os.getenv("GROQ_API_URL"),
    headers={
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": os.getenv("GROQ_MODEL"),
        "messages": [{"role": "user", "content": "teste"}]
    }
)

print(r.status_code)
print(r.text)