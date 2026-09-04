# Multi-Agent-System-using-LangGraph


A demo multi-agent system that uses LangGraph to implement a travel-planning assistant, input Guardrails. The project includes a FastAPI frontend.

Key ideas:
- Multi-agent coordination using LangGraph


Contents
- `app.py`: FastAPI web frontend and API endpoints
- `backend.py`: core agent orchestration / travel-planner logic
- `mcp_client.py`: client helpers to interact with the MCP server
- `custom_weather_mcp_server.py`: example MCP server for weather checks
- `templates/`, `static/`: frontend UI assets (HTML, JS, CSS)

Features
- Interactive web UI for sending travel planning prompts
- Endpoint for drafting travel plans and separate approval endpoint


Prerequisites
- Python 3.10+ (recommended)
- Git (to clone the repo)
- A virtual environment tool (venv) or similar

Quick start (Windows)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1    # PowerShell
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Run the FastAPI app (development)

```powershell
# option A (run module)
python app.py

# option B (uvicorn)
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

4. Open the web UI

Visit http://127.0.0.1:8000 in your browser to use the TripMate frontend.



```

API Endpoints
- `POST /api/travel` — create or resume a travel planning thread. JSON: `{ "message": "<user prompt>", "thread_id": "optional-thread-id" }`
- `POST /api/travel/approve` — approve or request revisions for a draft. JSON: `{ "thread_id": "<id>", "approved": true|false, "feedback": "optional" }`
- `GET /health` — basic health check and features list

Configuration & environment
- Secrets and API keys are not included in the repo. Use environment variables or a `.env` file for any required keys consumed by `langgraph`, `langchain`, or other adapters.

Development notes
- The project keeps synchronous convenience wrappers in `backend.py` while running an async FastAPI server — `nest_asyncio` is applied in `app.py`.
- Tests are not included; to experiment, interact with the web UI or call the API endpoints directly.


License
- This repository follows the license in the `LICENSE` file.

Acknowledgements
- Built as a demonstration of LangGraph .

