class ContextAgent:
    def analyze(self, user_input):
        return {
            "family": user_input["family"],
            "allergies": user_input["allergies"],
            "purpose": user_input["purpose"],
            "budget": user_input["budget"]
        }