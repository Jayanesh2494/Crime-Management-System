# dao.py
from pymongo import MongoClient

class UserDAO:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['crime_management']
        self.admin_collection = self.db['admins']
        self.user_collection = self.db['users']

    def add_user(self, user):
        if user.role == 'admin':
            self.admin_collection.insert_one(user.to_dict())
        else:
            self.user_collection.insert_one(user.to_dict())

    def find_user(self, username, role):
        if role == 'admin':
            return self.admin_collection.find_one({"username": username})
        else:
            return self.user_collection.find_one({"username": username})

class CrimeDAO:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['crime_management']
        self.collection = self.db['crimes']

    def add_crime(self, crime):
        self.collection.insert_one(crime.to_dict())

    def get_crimes(self):
        return list(self.collection.find())

    def update_crime_status(self, crime_id, status):
        self.collection.update_one({"_id": crime_id}, {"$set": {"status": status}})
