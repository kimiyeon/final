from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from agents.master_agent import MasterAgent
from agents.context_agent import ContextAgent
from agents.menu_agent import MenuPlannerAgent
from agents.inventory_agent import InventoryFilterAgent
from agents.price_agent import PriceOptimizerAgent

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print("VALIDATION ERROR:")
    print(exc.errors())
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@app.get("/")
def home():
    print("SERVING FRONTEND/INDEX.HTML")
    return FileResponse("frontend/index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

master_agent = MasterAgent()
context_agent = ContextAgent()
menu_agent = MenuPlannerAgent()
inventory_agent = InventoryFilterAgent()
price_agent = PriceOptimizerAgent()


class UserInput(BaseModel):
    family_size: int
    allergies: list[str]
    purpose: str
    budget: int

@app.post("/generate-shopping-list")
def generate(data: UserInput):
    result = master_agent.run(data.model_dump())
    return result

@app.post("/debug")
async def debug(request: Request):
    body = await request.json()
    print("DEBUG BODY:", body)
    return body