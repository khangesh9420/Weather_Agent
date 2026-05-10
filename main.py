import argparse

from datetime import (
    datetime,
    timezone,
)

from dotenv import load_dotenv

import flyte

from graph.workflow import graph

from utils.helpers import (
    extract_text,
)


load_dotenv()


env = flyte.TaskEnvironment(
    name="langgraph-gemini-agent",

    secrets=[
        flyte.Secret(
            key="GOOGLE_GEMINI_API_KEY"
        )
    ],

    image=flyte.Image.from_debian_base(
        python_version=(3, 12)
    ).with_pip_packages(
        "requests>=2.31.0",
        "python-dotenv",
        "langchain-core",
        "langgraph",
        "langchain-google-genai",
        "flyte",
    ),
)


def run_agent(prompt: str):

    today = datetime.now(
        timezone.utc
    ).strftime("%Y-%m-%d")

    result = graph.invoke({
        "messages": [
            (
                "system",
                (
                    "You are a weather assistant. "
                    "Always use the "
                    "get_weather_forecast tool "
                    "when weather data is needed."
                ),
            ),

            (
                "user",
                (
                    f"{prompt}\n"
                    f"Use {today} as date if "
                    "user does not provide one."
                ),
            ),
        ]
    })

    final_message = result["messages"][-1]

    return extract_text(
        final_message.content
    )


@env.task
@flyte.trace
def flyte_weather_agent(
    prompt: str
) -> str:

    return run_agent(prompt)


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Weather Agent "
            "(LangGraph + Flyte)"
        )
    )

    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    result = run_agent(args.prompt)

    print("\n--- FINAL ANSWER ---\n")

    print(result.strip())


if __name__ == "__main__":
    main()
