from pymongo.database import Database
from datetime import datetime
from bson.objectid import ObjectId


class ShanyraksRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, user_id, input: dict):
        date = datetime.utcnow()
        payload = {
            "user_id": user_id,
            "type": input.type,
            "price": input.price,
            "address": input.address,
            "area": input.area,
            "rooms_count": input.rooms_count,
            "description": input.description,
            "date": date,
        }
        self.database["shanyraks"].insert_one(payload)
        shanyrak = self.database["shanyraks"].find_one({"date": date})

        return str(shanyrak['_id'])

    def get_shanyrak_by_id(self, id):
        shanyrak = self.database["shanyraks"].find_one({"_id": ObjectId(id)})

        return shanyrak

    def change_shanyrak(self, id: str, input: dict):
        data = {}
        for t in input:
            if not (t[1] is None):
                data[t[0]] = t[1]
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(id)},
            update={
                "$set": data
            }
        )

    def delete_shanyrak(self, id: str):
        self.database["shanyraks"].delete_one({"_id": ObjectId(id)})
