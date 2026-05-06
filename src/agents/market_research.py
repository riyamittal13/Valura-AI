class MarketResearchAgent:
    def __init__(self):
        pass

    def run(self, query: str, entities: dict = None):
        """
        Returns structured market insights for user queries
        """

        # keep it deterministic + safe + fast
        response = {
            "intent": "market_research",
            "summary": f"Market overview for: {query}",
            
            "insights": [
                "Market sentiment is currently driven by macroeconomic trends.",
                "Tech and large-cap stocks are showing higher volatility.",
                "Diversification remains key in current market conditions."
            ],

            "suggestions": [
                "Consider reviewing exposure to high-volatility sectors.",
                "Look into index-based diversification if concentrated.",
                "Avoid overreacting to short-term market noise."
            ],

            "disclaimer": "This is not financial advice. This is for educational purposes only."
        }

        # return response
        return {
            "agent": "market_research",
            "data": response
        }