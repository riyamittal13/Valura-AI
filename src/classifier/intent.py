import re

# ---------------- NORMALIZATION ----------------
def normalize(q: str) -> str:
    q = q.lower()
    q = q.replace("&", " and ")
    q = q.replace("s&p", "sp500")
    q = q.replace("index fund", "indexfund")
    return q


# ---------------- MARKET DETECTOR ----------------
def is_market_query(q: str) -> bool:
    q = re.sub(r"[^\w\s/]", " ", q)
    q = re.sub(r"\s+", " ", q)

    # ticker like AAPL
    if re.fullmatch(r"[A-Z]{2,5}", q.strip()):
        return True

    # forex pair
    if re.search(r"\b[A-Z]{3}/[A-Z]{3}\b", q.upper()):
        return True

    # index names
    if any(x in q for x in ["nikkei", "ftse", "msci"]):
        return True

    # known companies/assets
    if re.search(r"\b(nvidia|tesla|asml|apple|hsbc|barclays|gold)\b", q):
        return True

    # strong keywords
    if any(k in q for k in [
        "price", "market", "news", "stock", "stocks",
        "index", "gainers", "losers", "sp500",
        "sensex", "nifty", "dow", "nasdaq"
    ]):
        return True

    # natural language phrases
    if any(p in q for p in [
        "tell me about", "how is", "any news on",
        "what happened", "compare", "today",
        "this week", "this month"
    ]):
        return True

    return False


# ---------------- CLASSIFIER ----------------
def classify_intent(user_query: str):
    q_raw = user_query  # IMPORTANT for ticker detection
    q = normalize(user_query)

    # ---------------- CUSTOMER SUPPORT ----------------
    if any(x in q for x in [
        "login", "account", "error", "issue", "not working",
        "transaction history", "didn't go through",
        "failed", "payment issue"
    ]):
        return "customer_support"

    # ---------------- PREDICTIVE (MOVE UP) ----------------
    if any(x in q for x in [
        "forecast", "prediction", "outlook",
        "in 5 years", "in 6 months", "predict",
        "where will"
    ]):
        return "predictive_analysis"

    # ---------------- RISK (MOVE UP) ----------------
    if any(x in q for x in [
        "risk", "volatility", "downside",
        "drawdown", "beta", "stress test", "exposed"
    ]):
        return "risk_assessment"

    # ---------------- FINANCIAL PLANNING (BEFORE STRATEGY) ----------------
    if any(x in q for x in [
        "retirement", "retire", "goal", "savings",
        "education", "house", "fire",
        "on track", "plan for", "college fund",
        "how much should i save"
    ]):
        return "financial_planning"

    # ---------------- INVESTMENT STRATEGY ----------------
    if any(x in q for x in [
        "should i", "buy", "sell", "invest",
        "rebalance", "hedge",
        "which fund should i buy",
        "equity bond split"
    ]):
        return "investment_strategy"

    # ---------------- PORTFOLIO HEALTH ----------------
    if any(x in q for x in [
        "portfolio", "holdings", "my investments",
        "concentration", "diversified",
        "my returns", "performance",
        "health check", "how is my portfolio",
        "beating the market"
    ]):
        return "portfolio_health"
    
    # ---------------- MARKET (MOVE BEFORE PRODUCT) ----------------
    if is_market_query(q) or re.fullmatch(r"[A-Z]{2,5}", q_raw.strip()):
        return "market_research"

    # ---------------- GENERAL ----------------
    if any(x in q for x in [
        "what is", "difference between",
        "explain", "meaning"
    ]):
        return "general_query"

    # # ---------------- MARKET (MOVE BEFORE PRODUCT) ----------------
    # if is_market_query(q) or re.fullmatch(r"[A-Z]{2,5}", q_raw.strip()):
    #     return "market_research"

    # ---------------- PRODUCT ----------------
    if any(x in q for x in [
        "recommend", "best fund", "mutual fund",
        "etf", "low cost fund", "which fund"
    ]):
        return "product_recommendation"

    # ---------------- FINANCIAL CALCULATOR (FIXED) ----------------
    if any(x in q for x in [
        "calculate", "sip", "emi", "mortgage",
        "future value", "convert",
        "tax", "capital gains", "how much will i have"
    ]) or re.search(r"\d+.*(years|months|%)", q):
        return "financial_calculator"

    # ---------------- DEFAULT ----------------
    return "general_query"

# ---------------- WRAPPER ----------------
def classify(query, llm=None):
    intent = classify_intent(query)

    class Result:
        pass

    r = Result()
    r.agent = intent
    r.entities = {}
    return r
