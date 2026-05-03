# def portfolio_health_agent(user_query: str):
#     return {
#         "response": "This is your portfolio health summary (dummy for now)"
#     }


def portfolio_health_agent(user_query: str):
    
    # Dummy portfolio (we will improve later)
    portfolio = {
        "AAPL": 50,
        "TSLA": 30,
        "NVDA": 20
    }

    # Calculate concentration
    top_stock = max(portfolio, key=portfolio.get)
    top_value = portfolio[top_stock]

    if top_value > 50:
        risk = "high"
    elif top_value > 30:
        risk = "medium"
    else:
        risk = "low"

    return {
        "concentration_risk": {
            "top_stock": top_stock,
            "percentage": top_value,
            "risk_level": risk
        },
        "observation": f"You have a high allocation in {top_stock}. Consider diversification.",
        "disclaimer": "This is not financial advice."
    }