from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Any
import os

uri = "mongodb+srv://bharatsingh:bhStarList@clusterstarlist.lfb9ncy.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true&appName=ClusterStarList"
client = AsyncIOMotorClient(uri)

database = client.DBstarList
collectionStars = database.collectionStars

def serialize_doc(doc: Any) -> dict:
    """Helper function to serialize MongoDB documents"""
    if "_id" in doc:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
    return doc
