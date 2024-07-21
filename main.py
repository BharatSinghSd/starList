from fastapi import FastAPI, HTTPException
from typing import List
from models import StarInDB
from schemas import StarCreate, StarUpdate
from database import collectionStars, serialize_doc
from bson import ObjectId

app = FastAPI()

@app.post("/stars", response_model=StarInDB)
async def create_star(star: StarCreate):
    star_dict = star.dict()
    result = await collectionStars.insert_one(star_dict)
    star_star = await collectionStars.find_one({"_id": result.inserted_id})
    return serialize_doc(star_star)

@app.get("/stars", response_model=List[StarInDB])
async def get_stars():
    stars = await collectionStars.find().to_list(length=100)
    return [serialize_doc(star) for star in stars]

@app.get("/stars/{star_id}", response_model=StarInDB)
async def get_star(star_id: str):
    star = await collectionStars.find_one({"_id": ObjectId(star_id)})
    if star:
        return serialize_doc(star)
    raise HTTPException(status_code=404, detail="star not found")

@app.put("/stars/{star_id}", response_model=StarInDB)
async def update_star(star_id: str, updated_star: StarUpdate):
    update_result = await collectionStars.update_one(
        {"_id": ObjectId(star_id)},
        {"$set": updated_star.dict()}
    )
    if update_result.matched_count:
        updated_star = await collectionStars.find_one({"_id": ObjectId(star_id)})
        return serialize_doc(updated_star)
    raise HTTPException(status_code=404, detail="star not found")

@app.delete("/stars/{star_id}", response_model=StarInDB)
async def delete_star(star_id: str):
    delete_result = await collectionStars.delete_one({"_id": ObjectId(star_id)})
    if delete_result.deleted_count:
        return {"id": star_id}
    raise HTTPException(status_code=404, detail="star not found")
