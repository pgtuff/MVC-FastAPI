from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    agree_to_terms: bool

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    agree_to_terms: bool

    class Config:
        from_attributes = True