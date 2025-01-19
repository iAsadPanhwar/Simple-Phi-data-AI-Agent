from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 
from dotenv import load_dotenv
import openai
import os
load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# web search agent
websearch_agent = Agent(
    name = "web search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructiond = ["Always show the source of the information"],
    show_tool_calls = True,
    markdown = True
)

# financial agent
financial_agent = Agent(
    name = "Financial Agent",
    role = "Get financial data",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations= True, stock_fundamentals= True, company_news= True )],
    instructions = ["Use tables to display the data"],
    show_tool_calls = True,
    markdown = True
)

# add the agents to the model
multi_ai_agent = Agent(
    team = [websearch_agent, financial_agent],
    instructions = ["Always show the source of the information", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summariza analyst recommentation and share the latest news for NVIDIA", stream = True)
