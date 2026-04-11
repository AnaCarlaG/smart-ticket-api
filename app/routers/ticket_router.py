from fastapi import APIRouter, HTTPException
from app.models.ticket_model import TicketRequest, TicketResponse
from app.services.groq_service import analyze_ticket

router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"]
)

@router.post("/analyze", response_model=TicketResponse)
async def analyze(request: TicketRequest):
    try:
        result = await analyze_ticket(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))