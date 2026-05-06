from src.agents.portfolio_health import portfolio_health_agent
# from src.agents.market_research import market_research_agent
from src.agents.market_research import MarketResearchAgent
from src.agents.stub_agent import stub_agent


# 1. Create registry once
AGENT_REGISTRY = {
    "portfolio_health": portfolio_health_agent,
    # "market_research": market_research_agent().run,
    "market_research": MarketResearchAgent().run,
}


def route_query(agent_name: str, user_query: str):

    # 2. Get agent from registry
    agent = AGENT_REGISTRY.get(agent_name)

    # 3. If real agent exists → run it
    if agent:
        return agent(user_query)

    # 4. Otherwise → stub fallback (required by assignment)
    return stub_agent(agent_name, user_query)