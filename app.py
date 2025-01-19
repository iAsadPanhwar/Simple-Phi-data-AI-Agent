import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import phi 
from phi.playground import Playground, serve_playground_app
from src.financial_agent import financial_agent, websearch_agent
import os
load_dotenv()

app = Playground(agents = [websearch_agent, financial_agent]).get_app()

