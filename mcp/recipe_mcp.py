import requests
import json


CATEGORY_MAP = {
    "weekly": "Beef",
    "diet": "Chicken",
    "birthday": "Dessert",
    "camping": "Seafood",
    "bbq": "Pork",
    "party": "Pasta"
}


def get_recipes(purpose="weekly"):
    category = CATEGORY_MAP.get(purpose, "Beef")

    try:
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
        response = requests.get(url, timeout=8)
        response.raise_for_status()

        data = response.json()
        meals = data.get("meals") or []

        results = []

        for meal in meals[:6]:
            detail = get_meal_detail(meal["idMeal"])
            if detail:
                results.append(detail)

        if results:
            return results

    except Exception as e:
        print("TheMealDB failed. Using local fallback.", e)

    return get_local_fallback(purpose)


def get_meal_detail(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url, timeout=8)
    response.raise_for_status()

    data = response.json()
    meals = data.get("meals") or []

    if not meals:
        return None

    meal = meals[0]

    ingredients = []

    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        if ingredient and ingredient.strip():
            ingredients.append(normalize_ingredient(ingredient))

    return {
        "menu": meal.get("strMeal", "Unknown Meal"),
        "ingredients": ingredients[:8]
    }


def normalize_ingredient(name):
    return (
        name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def get_local_fallback(purpose):
    with open("data/recipes.json", "r") as f:
        recipes = json.load(f)

    return recipes.get(purpose, recipes["weekly"])