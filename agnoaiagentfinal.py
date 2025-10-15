from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    role="Get financial data",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True,
                      stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# multi_ai_agent = Agent( # Commenting out multi_ai_agent
#     team=[web_search_agent, finance_agent],
#     model=Gemini(id="gemini-2.0-flash-exp"),
#     instructions=["Always include sources", "Use tables to display the data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# Calling agents directly to bypass task transfer issue
print("--- Summarizing analyst recommendations for GOOG ---")
finance_agent.print_response("Summarize analyst recommendations for GOOG", stream=True)

print("\n--- Getting the latest news for GOOG ---")
finance_agent.print_response("Get the latest news for GOOG", stream=True)

multi_ai_agent = Agent( # Commenting out multi_ai_agent
     team=[web_search_agent, finance_agent],
     model=Gemini(id="gemini-2.0-flash-exp"),
     instructions=["Always include sources", "Use tables to display the data"],
     show_tool_calls=True,
     markdown=True,
 )

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)

