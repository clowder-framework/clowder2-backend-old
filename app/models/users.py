from pydantic import Field
from typing import Optional
import os
from bson import ObjectId
from mongoengine import Document, StringField, IntField, DynamicDocument, connect
from pydantic import BaseModel, Field
from app.models.pyobjectid import PyObjectId
from app.models.mongomodel import OID, MongoModel


class User(MongoModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field()
    hashed_password: str = Field()
