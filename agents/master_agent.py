from agents.context_agent import ContextAgent
from agents.menu_agent import MenuPlannerAgent
from agents.inventory_agent import InventoryFilterAgent
from agents.price_agent import PriceOptimizerAgent


class MasterAgent:
    def __init__(self):
        self.context_agent = ContextAgent()
        self.menu_agent = MenuPlannerAgent()
        self.inventory_agent = InventoryFilterAgent()
        self.price_agent = PriceOptimizerAgent()

    def run(self, user_input):
        context = self.context_agent.analyze(user_input)

        menu = self.menu_agent.plan(context)

        filtered_items = self.inventory_agent.filter(menu["ingredients"])

        result = self.price_agent.optimize(
            filtered_items,
            budget=context["budget"],
            quantity_multiplier=menu.get("quantity_multiplier", 1.0)
        )

        return {
            "context": context,
            "meal_plan": menu["meal_plan"],
            "shopping_list": result["cart"],
            "total_cost": result["total"],
            "budget": context["budget"],
            "removed_items": result.get("removed_items", []),
            "budget": context["budget"],
            "excluded_allergy_items": menu.get("excluded_allergy_items", []),
            "family_size": menu.get("family_size"),
            "meal_count": menu.get("meal_count"),
            "quantity_multiplier": menu.get("quantity_multiplier")
        }
    
