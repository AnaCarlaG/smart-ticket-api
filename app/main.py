from fastapi import FastAPI
from app.routers.ticket_router import router

app = FastAPI(
    title="Smart Ticket API",
    description="API REST que utiliza IA para analisar e classificar chamados de suporte de TI automaticamente.",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à Smart Ticket API! Use o endpoint /api/tickets/analyze para analisar seus chamados de suporte de TI."}