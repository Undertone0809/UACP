import os

from agent import AssistantAgent
from langchain_community.tools.tavily_search import TavilySearchResults
from promptulate import ChatOpenAI

os.environ["TAVILY_API_KEY"] = "xxx"
# os.environ["OPENAI_API_KEY"] = "xxxx"

if __name__ == "__main__":
    llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0)
    tools = [TavilySearchResults(max_results=5)]

    agent = AssistantAgent(tools=tools, llm=llm)
    agent.run("what is the hometown of the 2024 Australia open winner?")
