from fastapi import APIRouter, HTTPException, Body
from app.services.message_service import MessageService
from app.models.message_model import Message
from uuid import UUID

router = APIRouter()
message_service = MessageService()


@router.get("/messages/{message_id}", response_model=Message, tags=["messages"])
async def get_message(message_id: UUID):
    """
    Fetch a message using its UUID.

    Args:
        message_id (UUID): UUID of the message to fetch.

    Returns:
        ContactRequest: Fetched message data.
    """
    message = await message_service.get_message({"message_id": message_id})
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return Message(**message)


@router.post("/messages/", response_model=Message, tags=["messages"])  # Add more decorators as needed
async def create_message(message: Message):
    """
    Add a new message to the database and send it to the destination emails.

    Args:
        message (ContactRequest): Pydantic model instance containing message data.

    Returns:
        ContactRequest: Created message data.
    """
    return await message_service.create_message(message)


@router.delete("/messages/{message_id}", response_model=dict, tags=["messages"])
async def delete_message(message_id: UUID):
    """
    Delete a message using its UUID.

    Args:
        message_id (UUID): UUID of the message to delete.

    Returns:
        dict: Status of the deletion.
    """
    deleted = await message_service.delete_message({"message_id": message_id})
    if not deleted:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"status": "Message deleted successfully"}
