import os
from typing import List

from bson import ObjectId
from fastapi import APIRouter, Request, HTTPException
from mongoengine import connect

from app.models.datasets import Dataset, MongoDataset

router = APIRouter()

DATABASE_URI = os.environ["MONGODB_URL"]
db=DATABASE_URI+"/clowder"
connect(host=db)

@router.post('/datasets', response_model=Dataset)
async def save_dataset(body: Dataset, request: Request):
    res = await request.app.db["datasets"].insert_one(body.mongo())
    found = await request.app.db["datasets"].find_one({'_id': res.inserted_id})
    return Dataset.from_mongo(found)
    # dataset = MongoDataset(**body.dict()).save()
    # return Dataset(**dataset.dict())


@router.get("/datasets", response_model=List[Dataset])
async def get_datasets(request: Request, skip: int = 0, limit: int = 2):
    datasets = []
    for doc in await request.app.db["datasets"].find().skip(skip).limit(limit).to_list(length=limit):
        datasets.append(doc)
    return datasets


@router.get("/datasets/{dataset_id}", response_model=Dataset)
async def get_dataset(dataset_id: str, request: Request):
    if (dataset := await request.app.db["datassets"].find_one({"_id": ObjectId(dataset_id)})) is not None:
        return dataset
    raise HTTPException(status_code=404, detail=f"User {dataset_id} not found")
