import json

class MenuPlannerAgent:
    def plan(self, context):
        with open("data/recipes.json", "r") as f:
            recipes = json.load(f)

        purpose = context["purpose"]

        if purpose == "diet":
            selected = recipes["diet"]
        else:
            selected = recipes["weekly"]

        meals = [meal["menu"] for meal in selected]

        ingredients = []
        for meal in selected:
            ingredients.extend(meal["ingredients"])

        return {
            "meal_plan": meals,
            "ingredients": ingredients
        }