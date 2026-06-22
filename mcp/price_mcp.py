def compare_prices(item: str, family_size: int = 1, purpose: str = "weekly") -> dict:
    normalized = item.lower().replace(" ", "_")

    rules = [
        {
            "keywords": ["sirloin", "steak"],
            "category": "meat",
            "prices": {"coupang": 18000, "emart": 20000, "homeplus": 19000},
        },
        {
            "keywords": ["soy_sauce", "oyster_sauce", "sauce"],
            "category": "sauce",
            "prices": {"coupang": 3500, "emart": 4000, "homeplus": 3800},
        },
        {
            "keywords": ["garlic"],
            "category": "vegetable",
            "prices": {"coupang": 2500, "emart": 2800, "homeplus": 2600},
        },
        {
            "keywords": ["red_pepper", "bell_pepper", "pepper"],
            "category": "vegetable",
            "prices": {"coupang": 3000, "emart": 3500, "homeplus": 3200},
        },
        {
            "keywords": ["cumin", "oregano", "black_pepper"],
            "category": "seasoning",
            "prices": {"coupang": 2500, "emart": 3000, "homeplus": 2800},
        },
        {
            "keywords": ["sherry", "wine"],
            "category": "seasoning",
            "prices": {"coupang": 5000, "emart": 6000, "homeplus": 5500},
        },
    ]

    for rule in rules:
        for keyword in rule["keywords"]:
            if keyword in normalized:
                prices = rule["prices"]
                best_store = min(prices, key=prices.get)

                return {
                    "item": item,
                    "category": rule["category"],
                    "prices": prices,
                    "best_store": best_store,
                    "estimated_price": prices[best_store],
                    "confidence": "high" if keyword == normalized else "medium",
                    "reason": f"Matched keyword: {keyword}",
                    "source": "price-mcp",
                }

    prices = {"coupang": 2000, "emart": 2500, "homeplus": 2200}
    best_store = min(prices, key=prices.get)

    return {
        "item": item,
        "category": "unknown",
        "prices": prices,
        "best_store": best_store,
        "estimated_price": prices[best_store],
        "confidence": "low",
        "reason": "No exact rule matched. Used default grocery estimate.",
        "source": "price-mcp",
    }


def get_prices():
    return {
        "source": "price-mcp",
        "description": "MCP wrapper for grocery price estimation and store comparison",
    }