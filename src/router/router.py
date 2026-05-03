from src.agents.portfolio_health import portfolio_health_agent
from src.agents.stub_agent import stub_agent

def route_query(agent_name: str, user_query: str):
    
    if agent_name == "portfolio_health":
        return portfolio_health_agent(user_query)
    
    else:
        return stub_agent(agent_name, user_query)