from mcp.price_mcp import compare_prices


class PriceOptimizerAgent:
    def optimize(self, shopping_items, budget=None, quantity_multiplier=1.0):
        cart = []

        for item in shopping_items:
            estimate = compare_prices(item)

            cart.append({
                "item": item,
                "name": item,
                "category": estimate["category"],
                "price": estimate["estimated_price"],
                "best_store": estimate["best_store"],
                "confidence": estimate["confidence"],
                "reason": estimate["reason"],
                "source": estimate["source"],
            })

        cart.sort(key=lambda x: x["price"])

        selected = []
        removed = []
        total = 0

        for item in cart:
            if budget is None or total + item["price"] <= budget:
                selected.append(item)
                total += item["price"]
            else:
                removed.append(item)

        return {
            "cart": selected,
            "removed_items": removed,
            "total": total,
            "budget": budget,
            "budget_warning": len(removed) > 0,
        }