from pydantic import BaseModel, EmailStr

class UserData(BaseModel):
    """User information model"""
    email: EmailStr
    name: str
    stack: str

class ProfileResponse(BaseModel):
    """Profile endpoint response model"""
    status: str
    user: UserData
    timestamp: str
    fact: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "user": {
                    "email": "john.doe@example.com",
                    "name": "John Doe",
                    "stack": "Python/FastAPI"
                },
                "timestamp": "2025-10-18T14:30:45.123Z",
                "fact": "Cats sleep for around 13 to 16 hours a day."
            }
        }