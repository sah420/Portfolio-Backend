from app.repositories.message_repository import MessageRepository
from app.models.message_model import Message
from uuid import UUID
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


class MessageService:
    def __init__(self):
        load_dotenv()
        self.repository = MessageRepository()
        self.destination_email = os.getenv("DESTINATION_EMAIL_ADDRESS")
        self.sender_email = os.getenv("SENDING_EMAIL_ADDRESS")
        self.sender_password = os.getenv("SENDING_EMAIL_PASSWORD")

    async def get_message(self, filter: dict) -> dict:
        return await self.repository.fetch_message(filter)

    async def create_message(self, document: Message):
        # Send the message to email
        self.send_email(document)

        # Add the message to the MongoDB collection
        result = await self.repository.insert_message(document.dict())

        # Return the created Message with its MongoDB ObjectID
        return {**document.dict(), **result}

    async def delete_message(self, message_id: UUID) -> bool:
        return await self.repository.delete_message(message_id)

    def send_email(self, message_data: dict):
        # Email destination configuration
        DESTINATION_EMAILS = [self.destination_email, message_data.email]

        # Set up the email content
        msg = EmailMessage()
        msg.set_content(f"From: {message_data.last_name}, {message_data.first_name} of {message_data.company_name}\n\n{message_data.message}")
        msg["Subject"] = f"Subject: {message_data.subject}"
        msg["From"] = self.sender_email
        msg["To"] = DESTINATION_EMAILS

        # Send the email using Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            smtp.send_message(msg)
