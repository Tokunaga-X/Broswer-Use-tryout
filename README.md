# Browser-Use Learning Project

A simple test project for learning [browser-use](https://github.com/browser-use/browser-use), a powerful tool that enables AI to control browsers.

## What is browser-use?

browser-use is a Python library that allows AI agents to interact with web browsers, making it easy to automate browser tasks using natural language.

## Setup

1. Install dependencies:

```bash
pip install browser-use
playwright install
```

2. Create `.env` file and add your API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Quick Example

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    agent = Agent(
        task="Compare prices between two websites",
        llm=ChatOpenAI(model="gpt-4"),
    )
    await agent.run()

asyncio.run(main())
```

## Resources

- [Official Documentation](https://browser-use.com/)
- [GitHub Repository](https://github.com/browser-use/browser-use)
- [Examples](https://github.com/browser-use/browser-use/tree/main/examples)

## License

MIT License
