def stub_agent(agent_name: str, user_query: str):
    # return {
    #     "response": f"{agent_name} agent is not implemented yet."
    # }
    return {
        "agent": agent_name,
        "data": {
            "response": f"{agent_name} agent is not implemented yet."
        }
    }