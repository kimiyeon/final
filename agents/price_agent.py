from mcp.price_mcp import get_prices


class PriceOptimizerAgent:
    def optimize(self, shopping_items, budget=None, quantity_multiplier=1.0):
        prices = get_prices()

        cart = []

        for item in shopping_items:
            base_price = prices.get(item, 1000)
            adjusted_price = int(base_price * quantity_multiplier)

            cart.append({
                "item": item,
                "name": item,
                "base_price": base_price,
                "price": adjusted_price,
                "quantity_multiplier": quantity_multiplier
            })

        # 가격 낮은 것부터 담아서 예산 안에 최대한 많이 포함
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
            "budget_warning": len(removed) > 0
        }