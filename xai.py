from langchain_xai import ChatXAI

from dotenv import load_dotenv
load_dotenv()

llm = ChatXAI(
    model="grok-2-1212",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to chinese. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)