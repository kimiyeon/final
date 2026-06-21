from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from agents.master_agent import MasterAgent
from agents.context_agent import ContextAgent
from agents.menu_agent import MenuPlannerAgent
from agents.inventory_agent import InventoryFilterAgent
from agents.price_agent import PriceOptimizerAgent

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

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
    allergies: list
    purpose: str
    budget: int



@app.post("/generate-shopping-list")
def generate(data: UserInput):
    result = master_agent.run(data.model_dump())
    return result