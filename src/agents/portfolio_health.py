def portfolio_health_agent(user_data=None):
    """
    Basic portfolio health analysis.
    Uses dummy data if no user_data provided.
    """

    # ---------------- SAMPLE PORTFOLIO ----------------
    portfolio = [
        {"ticker": "AAPL", "weight": 0.45},
        {"ticker": "MSFT", "weight": 0.25},
        {"ticker": "TSLA", "weight": 0.15},
        {"ticker": "NVDA", "weight": 0.10},
        {"ticker": "CASH", "weight": 0.05},
    ]

    response = []

    # ---------------- 1. CONCENTRATION RISK ----------------
    largest = max(portfolio, key=lambda x: x["weight"])

    if largest["weight"] > 0.4:
        response.append(
            f"⚠️ High concentration risk: {largest['ticker']} makes up {int(largest['weight']*100)}% of your portfolio."
        )
    else:
        response.append("✅ No major concentration risk detected.")

    # ---------------- 2. DIVERSIFICATION ----------------
    if len(portfolio) < 5:
        response.append("⚠️ Your portfolio is not well diversified (too few assets).")
    else:
        response.append("✅ Portfolio has a reasonable number of assets.")

    # ---------------- 3. TECH HEAVY CHECK ----------------
    tech_stocks = {"AAPL", "MSFT", "NVDA", "GOOGL", "META"}
    tech_weight = sum(p["weight"] for p in portfolio if p["ticker"] in tech_stocks)

    if tech_weight > 0.6:
        response.append("⚠️ Portfolio is heavily tilted towards tech sector.")
    else:
        response.append("✅ Sector allocation looks balanced.")

    # ---------------- 4. GENERAL INSIGHT ----------------
    response.append("💡 Consider rebalancing to reduce risk and improve diversification.")

    # ---------------- 5. DISCLAIMER ----------------
    response.append("⚠️ This is not financial advice.")

    # return "\n".join(response)
    # return {
    # "response": "\n".join(response)
    # }
    return {
        "agent": "portfolio_health",
        "data": {
            "response": "\n".join(response)
        }
    }