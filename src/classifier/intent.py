def classify_intent(user_query: str):
    query = user_query.lower()

    if "portfolio" in query:
        return {
            "intent": "portfolio_health",
            "agent": "portfolio_health"
        }

    elif "stock" in query or "market" in query:
        return {
            "intent": "market_research",
            "agent": "market_research"
        }

    else:
        return {
            "intent": "unknown",
            "agent": "stub"
        }