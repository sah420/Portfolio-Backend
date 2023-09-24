from app.services.database import get_database
from datetime import datetime


class MessageRepository:
    """
    Repository class for message-related operations.

    This class provides an interface to interact with the MongoDB collection dedicated
    to storing messages. It offers CRUD operations and other utility methods
    to manage message data in the database.

    Attributes:
        collection_name (str): Name of the message collection in the database.
    """

    def __init__(self):
        """Initializes the MessageRepository with the message collection name."""
        self.collection_name = "messages"

    async def fetch_message(self, filter: dict) -> dict:
        """
        Fetches a message from the database based on the provided filter.

        Args:
            filter (dict): Filter criteria to find the message.

        Returns:
            dict: Message document if found, None otherwise.
        """
        async with get_database() as db:
            collection = db[self.collection_name]
            document = await collection.find_one(filter)
            return document

    async def insert_message(self, document: dict) -> dict:
        """
        Inserts a new message document into the database.
        The date of submission is added automatically.

        Args:
            document (dict): Message data to insert.

        Returns:
            dict: Contains the inserted ID of the message.
        """
        document["date_submitted"] = datetime.now()

        async with get_database() as db:
            collection = db[self.collection_name]
            result = await collection.insert_one(document)
            return {"_id": str(result.inserted_id)}

    async def delete_message(self, filter: dict) -> bool:
        """
        Deletes a message from the database.

        Args:
            filter (dict): Filter criteria to find the message.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        async with get_database() as db:
            collection = db[self.collection_name]
            result = await collection.delete_one(filter)
            return result.deleted_count > 0
