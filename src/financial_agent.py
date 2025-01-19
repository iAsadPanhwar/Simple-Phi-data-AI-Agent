from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 


# web search agent
websearch_agent = Agent(
    name = "web search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructiond = ["Always show the source of the information"],
    show_tool_calls = True,
    markdown = True
)

# financial agent

financial_agent = Agent(
    name = "Financial Agent",
    role = "Get financial data",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools()],
    instructions = ["Always show the source of the information"],
    show_tool_calls = True,
    markdown = True
)
