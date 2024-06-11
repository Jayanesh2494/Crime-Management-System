# models.py
from bson import ObjectId

class User:
    def __init__(self, username, password, role='user'):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

class Crime:
    def __init__(self, crime_type, description, date, location, status='Pending'):
        self.crime_type = crime_type
        self.description = description
        self.date = date
        self.location = location
        self.status = status

    def to_dict(self):
        return {
            "type": self.crime_type,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "status": self.status
        }
