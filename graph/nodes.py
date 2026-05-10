from dotenv import load_dotenv
load_dotenv()
import os

from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import (
    BaseMessage,
    ToolMessage,
)

from langchain_core.runnables import RunnableConfig

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)

from langgraph.graph.message import add_messages

from tools.weather_tool import (
    get_weather_forecast,
)


class AgentState(TypedDict):

    messages: Annotated[
        Sequence[BaseMessage],
        add_messages
    ]


TOOLS = [get_weather_forecast]

TOOLS_BY_NAME = {
    t.name: t for t in TOOLS
}


def create_model():

    api_key = os.getenv(
        "GOOGLE_GEMINI_API_KEY"
    )

    if not api_key:
        raise RuntimeError(
            "GOOGLE_GEMINI_API_KEY not set"
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_retries=2,
        google_api_key=api_key,
    )

    return llm.bind_tools(TOOLS)


def call_model(
    state: AgentState,
    config: RunnableConfig
):

    model = create_model()

    messages = state["messages"]

    response = model.invoke(
        messages,
        config=config,
    )

    return {
        "messages": messages + [response]
    }


def call_tool(state: AgentState):

    last_message = state["messages"][-1]

    tool_call = last_message.tool_calls[0]

    result = TOOLS_BY_NAME[
        tool_call["name"]
    ].invoke(tool_call["args"])

    tool_message = ToolMessage(
        content=result,
        tool_call_id=tool_call["id"],
    )

    return {
        "messages": (
            state["messages"] +
            [tool_message]
        )
    }
