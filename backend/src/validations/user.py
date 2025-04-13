from pydantic import BaseModel, Field

class UserLoginModel(BaseModel):
    username: str
    password: str
