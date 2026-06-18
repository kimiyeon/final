import json

class InventoryFilterAgent:
    def filter(self, ingredients):
        with open("data/fridge.json", "r") as f:
            fridge = json.load(f)["items"]

        remaining = [item for item in ingredients if item not in fridge]
        return remaining