import json

class PriceOptimizerAgent:
    def optimize(self, shopping_items):
        with open("backend/data/prices.json", "r") as f:
            prices = json.load(f)

        cart = []
        total = 0

        for item in shopping_items:
            price = prices.get(item, 1000)
            total += price
            cart.append({
                "item": item,
                "price": price
            })

        return {
            "cart": cart,
            "total": total
        }