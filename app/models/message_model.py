from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
from typing import Literal
from datetime import datetime


class Message(BaseModel):
    message_id: UUID = uuid4()
    first_name: str
    last_name: str
    company_name: str
    subject: Literal["Questions", "Freelancing", "Offer", "Interview"]
    email: EmailStr
    message: str
    date: datetime = datetime.now()
