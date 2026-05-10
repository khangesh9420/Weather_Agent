# Weather Agent — LangGraph + Gemini, built on Flyte

An AI agent that answers weather queries using a LangGraph state machine
and Google's Gemini API. Built and run inside a Flyte Devbox environment.

## What is this?
A simple agentic workflow that demonstrates the core pattern of modern AI
agents: an LLM that can decide when to call a tool, execute it, and
incorporate the result into its final answer.

## Why Flyte Devbox?
Flyte Devbox provides a ready-to-use cloud development environment with
the dependencies, GPU access, and isolation needed for AI workflows —
no local setup overhead.

## Project Structure
.
├── graph/
│   ├── nodes.py            # LLM node and tool routing logic
│   └── workflow.py         # LangGraph StateGraph definition
├── tools/
│   └── weather_tool.py     # Weather lookup function exposed as a tool
├── utils/
│   └── helpers.py          # Shared helpers
├── main.py                 # Entry point — invokes the compiled graph
└── requirements.txt

## Prerequisites
- Python 3.12
- A Google API key (for Gemini)
- A weather data source (or stubbed responses for testing)
- A Flyte account — sign up free at https://flyte.org

## Setup

### 1. Spin up a Flyte Devbox
Sign in at flyte.org and launch a new devbox. Clone the repo inside it.

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set environment variables
export GOOGLE_API_KEY="your-key-here"

### 4. Run the agent
python main.py

## How It Works
1. User submits a query like "What's the weather in Bochum?"
2. main.py invokes the compiled LangGraph workflow
3. The LLM node (Gemini) inspects the query and the tool schema
4. If a weather lookup is needed, it emits a tool call
5. The tool node runs weather_tool.py and returns structured data
6. Gemini incorporates the result and returns a natural-language answer

## Key Concepts Demonstrated
- LangGraph StateGraph for explicit agent control flow
- Tool calling with Gemini via the Google Generative AI SDK
- Clean separation of graph / tools / utils for testability
- Cloud-native development with Flyte Devbox

## Next Steps
- Add conversation memory across turns
- Multi-tool routing (current weather, forecast, alerts)
- Deploy as a FastAPI endpoint
- Add observability with AgentOps or LangSmith

## References
- Flyte: https://flyte.org
- LangGraph: https://langchain-ai.github.io/langgraph/
- Gemini API: https://ai.google.dev

<img width="614" height="551" alt="weather_agent_flyte" src="https://github.com/user-attachments/assets/146a8d53-00bd-4123-b0c1-8ac5e8f25457" />

## Handson
<img width="2517" height="565" alt="flyte_01" src="https://github.com/user-attachments/assets/fb2b864b-6cba-4aa9-aa69-6f4f47e92e68" />
--------------------------------------------------------------------------------------------------------------------------------------
<img width="2507" height="371" alt="flyte-02" src="https://github.com/user-attachments/assets/899f9959-7843-4e37-af41-62abfd008d16" />
--------------------------------------------------------------------------------------------------------------------------------------
<img width="2459" height="1022" alt="flyte-03" src="https://github.com/user-attachments/assets/1ad1e98b-e406-44ae-b377-0630b8663f6c" />
--------------------------------------------------------------------------------------------------------------------------------------
<img width="1478" height="299" alt="flyte-04" src="https://github.com/user-attachments/assets/54f80bbb-7b43-47f6-bf70-d8508684247e" />
--------------------------------------------------------------------------------------------------------------------------------------
<img width="1234" height="600" alt="flyte-05" src="https://github.com/user-attachments/assets/84fcec6e-6023-4fa4-aecf-d6bf08752a40" />
--------------------------------------------------------------------------------------------------------------------------------------





