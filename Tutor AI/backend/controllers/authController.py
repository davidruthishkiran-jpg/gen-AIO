from fastapi import APIRouter,Request
from models.authModel import SignupModel,LoginModel
#from services.authService import signup as signup_service
import services.authService as auth

router=APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/signup")
async def signup(data:SignupModel,request:Request):
    #return signup_service(data)
    return await auth.signup(data,request.app.state.db)
@router.post("/login")
async def login(data:LoginModel,request:Request):
    return await auth.login(data,request.app.state.db)
