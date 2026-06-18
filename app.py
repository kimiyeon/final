from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents.context_agent import ContextAgent
from agents.menu_agent import MenuPlannerAgent
from agents.inventory_agent import InventoryFilterAgent
from agents.price_agent import PriceOptimizerAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

context_agent = ContextAgent()
menu_agent = MenuPlannerAgent()
inventory_agent = InventoryFilterAgent()
price_agent = PriceOptimizerAgent()


class UserInput(BaseModel):
    family: list
    allergies: list
    purpose: str
    budget: int


@app.get("/")
def home():
    return {"message": "Smart Grocery Agent Running"}


@app.post("/generate-shopping-list")
def generate(data: UserInput):
    context = context_agent.analyze(data.model_dump())

    menu = menu_agent.plan(context)

    filtered = inventory_agent.filter(menu["ingredients"])

    result = price_agent.optimize(filtered)

    return {
        "context": context,
        "meal_plan": menu["meal_plan"],
        "shopping_list": result["cart"],
        "total_cost": result["total"]
    }