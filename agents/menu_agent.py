from mcp.recipe_mcp import get_recipes

ALLERGY_MAP = {
    "닭고기": ["chicken", "chicken_breast"],
    "치킨": ["chicken", "chicken_breast"],
    "chicken": ["chicken", "chicken_breast"],

    "우유": ["milk", "cheese", "greek_yogurt", "cream"],
    "유제품": ["milk", "cheese", "greek_yogurt", "cream"],
    "milk": ["milk", "cheese", "greek_yogurt", "cream"],
    "dairy": ["milk", "cheese", "greek_yogurt", "cream"],

    "계란": ["egg"],
    "달걀": ["egg"],
    "egg": ["egg"],

    "땅콩": ["peanut"],
    "견과류": ["peanut", "almond", "walnut", "cashew"],
    "peanut": ["peanut"],
    "nuts": ["peanut", "almond", "walnut", "cashew"],

    "새우": ["shrimp", "prawn"],
    "해산물": ["shrimp", "prawn", "salmon", "fish", "tuna"],
    "seafood": ["shrimp", "prawn", "salmon", "fish", "tuna"]
}


class MenuPlannerAgent:
    def plan(self, context):
        purpose = context["purpose"]
        recipes = get_recipes(purpose)

        blocked = self.get_blocked_items(context.get("allergies", []))

        meals = []
        ingredients = []

        for meal in recipes:
            meal_ingredients = set(meal["ingredients"])

            if meal_ingredients & blocked:
                continue

            meals.append(meal["menu"])
            ingredients.extend(meal["ingredients"])

            if len(meals) >= 3:
                break

        if not meals:
            meals = ["No safe meal found"]
            ingredients = []

        return {
            "meal_plan": meals,
            "ingredients": list(dict.fromkeys(ingredients)),
            "excluded_allergy_items": list(blocked)
        }

    def get_blocked_items(self, allergies):
        blocked = set()

        for allergy in allergies:
            allergy = allergy.strip().lower()

            for key, items in ALLERGY_MAP.items():
                if key.lower() in allergy:
                    blocked.update(items)

        return blocked