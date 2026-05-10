# Weather Agent — LangGraph + Gemini + Flyte

An AI-powered weather assistant built using:

- LangGraph
- Google Gemini API
- Flyte

This project demonstrates how to build an agentic workflow where an LLM can:
- understand user intent
- decide when to call tools
- execute external APIs
- return natural-language answers

The agent runs inside a local Flyte Devbox environment and uses real weather data from Open-Meteo APIs.

---

# Features

- LangGraph StateGraph workflow orchestration
- Gemini tool-calling support
- Real weather forecasting API integration
- Dynamic city geocoding
- Modular production-style architecture
- Flyte task execution support
- Dockerized Flyte runtime builds
- Environment variable + Flyte secret support

---

# Project Structure

```text
.
├── graph/
│   ├── nodes.py
│   └── workflow.py
│
├── tools/
│   └── weather_tool.py
│
├── utils/
│   └── helpers.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How It Works

1. User submits a query:

```text
weather in Berlin
```

2. LangGraph sends the request to Gemini

3. Gemini decides whether the weather tool is required

4. If needed, the tool:
   - geocodes the city
   - fetches weather data
   - returns structured forecast data

5. Gemini generates the final natural-language response

---

# Tech Stack

| Component | Purpose |
|---|---|
| LangGraph | Agent workflow orchestration |
| Gemini 2.5 Flash | LLM + tool calling |
| Flyte | Task orchestration/runtime |
| Open-Meteo API | Weather data |
| Python 3.12 | Runtime |

---

# Prerequisites

Install:

- Python 3.12
- Docker
- Flyte CLI
- Git

You also need:

- Gemini API key from Google AI Studio

Get API key:

https://aistudio.google.com/app/apikey

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/khangesh9420/Weather_Agent.git

cd Weather_Agent
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv flyte-env

source flyte-env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Flyte Setup

## 1. Start Flyte Devbox

```bash
flyte start devbox
```

---

## 2. Create Flyte Config

```bash
flyte create config \
    --endpoint localhost:30080 \
    --project flytesnacks \
    --domain development \
    --builder local \
    --insecure
```

---

# Environment Variables

Export your Gemini API key:

```bash
export GOOGLE_GEMINI_API_KEY="your_actual_api_key"
```

Verify:

```bash
echo $GOOGLE_GEMINI_API_KEY
```

---

# Running the Agent

## Run Locally

```bash
python3 main.py --prompt "weather in Berlin"
```

---

## Run Using Flyte

```bash
flyte run main.py flyte_weather_agent \
    --prompt "weather in Berlin"
```

---

# Example Output

```text
Weather forecast for Berlin on 2026-05-10:

2026-05-10T00:00: 14°C
2026-05-10T01:00: 13°C
2026-05-10T02:00: 12°C
...
```

---

# Key Concepts Demonstrated

- Agentic AI workflows
- Tool calling with LLMs
- LangGraph conditional routing
- External API integration
- Flyte task orchestration
- Containerized execution
- Production-ready project structure

---

# Future Improvements

- Multi-tool agents
- Conversation memory
- Streaming responses
- FastAPI deployment
- Observability with LangSmith / AgentOps
- Kubernetes deployment
- Scheduled Flyte workflows

---

# Useful Commands

## Check Flyte Devbox

```bash
flyte status
```

---

## Restart Flyte Devbox

```bash
flyte stop

flyte start devbox
```

---

## Verify Docker

```bash
docker --version
```

---

## Verify Buildx

```bash
docker buildx version
```

---

# References

Flyte Documentation:
https://flyte.org

LangGraph Documentation:
https://langchain-ai.github.io/langgraph/

Gemini API Documentation:
https://ai.google.dev

Open-Meteo API:
https://open-meteo.com


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
<img width="1250" height="488" alt="flyte-06" src="https://github.com/user-attachments/assets/b70bd841-e903-40eb-9b83-e3064929e746" />






