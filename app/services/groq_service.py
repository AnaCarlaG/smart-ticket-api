import httpx
import json
from app.models.ticket_model import TicketRequest, TicketResponse
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_URL = os.getenv("GROQ_API_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

ticket_counter = 1

async def analyze_ticket(request: TicketRequest) -> TicketResponse:
    global ticket_counter

    prompt = f"""
    Você é um assistente de suporte de TI. Analise o chamado abaixo e responda APENAS com um JSON válido, sem explicações.

    Descrição do problema: {request.description}

    Responda exatamente neste formato:
    {{
        "title": "título curto do chamado",
        "category": "Hardware | Software | Rede | Acesso | Outro",
        "priority": "ALTA | MÉDIA | BAIXA",
        "summary": "resumo objetivo em uma frase",
        "suggested_response": "sugestão de resposta para o atendente"
    }}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=body)
        response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]
    data = json.loads(content)

    result = TicketResponse(
        id=ticket_counter,
        title=data["title"],
        category=data["category"],
        priority=data["priority"],
        summary=data["summary"],
        suggested_response=data["suggested_response"]
    )

    ticket_counter += 1
    return result