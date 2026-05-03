def safety_check(user_query: str):
    query = user_query.lower()

    # Block dangerous things
    if "insider trading" in query:
        return False, "I cannot assist with insider trading."

    if "guaranteed return" in query:
        return False, "No investment can guarantee returns."

    if "market manipulation" in query:
        return False, "I cannot assist with market manipulation."

    # If safe
    return True, "Safe"
