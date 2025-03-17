# from langchain_xai import ChatXAI
from langchain_openai import ChatOpenAI
from browser_use import Browser, Agent

import os
os.environ["HTTP_PROXY"]  = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

from dotenv import load_dotenv
load_dotenv()

import asyncio

# llm = ChatXAI(model="grok-2-1212")
llm = ChatOpenAI(
    base_url="",
    api_key='',
    model="gpt-4o",
    )

agent = Agent(
        task="GO to https://neworld.tv/auth/login, use the following info to login: email:1419991347@qq.com, password: caijinqi, then summary the page content for me.",
        llm=llm,
    )

async def main():
    result = await agent.run()
    print(result)

asyncio.run(main())
