from pydantic import BaseModel

class TicketRequest(BaseModel):
    description: str

class TicketResponse(BaseModel):
    id: int
    title: str
    category: str
    priority: str
    summary: str
    suggested_response: str