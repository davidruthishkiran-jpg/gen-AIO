from fastapi import FastAPI
from controllers.authController import router as AuthRouter
from database.mongodb import lifespan
app = FastAPI(
    title="TutorAI Application",
    description="This is a Tutor AI Application",
    version="1.0.0",
    lifespan=lifespan
)
#register all routers here
app.include_router(AuthRouter)
@app.get("/",tags=["Root"]) #endpoint
async def  root():#function
    return {"message": "Hello World"}#json format(key and value ,enclosed in curly braces)
