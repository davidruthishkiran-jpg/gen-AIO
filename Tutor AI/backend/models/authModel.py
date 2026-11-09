from pydantic import BaseModel
class SignupModel(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone:str
    password: str
class LoginModel(BaseModel):
    email: str
    password: str