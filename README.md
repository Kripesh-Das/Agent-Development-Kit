# Agent Development Kit (ADK) - 12 Example Agents

This repository demonstrates a variety of agent patterns and use-cases using the [Google Agent Development Kit (ADK)](https://pypi.org/project/google-adk/). Each folder contains a self-contained example agent, ranging from simple LLM wrappers to multi-agent orchestration and persistent session management.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Examples Overview](#examples-overview)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## Project Structure

```
.
├── 1_hello_world/                # Basic hello world agent
├── 2_tools/                      # Agent using external tools
├── 3_LLMS/                       # LLM-based agents (e.g., joke agent)
├── 4_OPS/                        # Operational agents (e.g., email generator)
├── 5_session_state_runner/       # Stateful session agent
├── 6_storage/                    # Agent with persistent storage (SQLite)
├── 7_multi_agent/                # Multi-agent manager and sub-agents
├── 8_custom_tool/                # Custom tool integration
├── 9_custom_callback/            # Custom callback example
├── 10_sequential_agent/          # Sequential pipeline agent
├── 11_router_agent/              # Router agent for task delegation
├── 12_loop_agent/                # Looping agent (e.g., LinkedIn post reviewer)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kripesh-Das/Agent-Development-Kit.git
   cd Agent-Development-Kit
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy the `.env` files from each agent's folder (if present) and fill in your API keys as needed.
   - Example:
     ```
     GOOGLE_API_KEY=your-google-api-key
     ```

---

## Usage

Each example can be run independently.  
Navigate to the desired folder and run the main script, for example:

```bash
cd 3_LLMS/joke_agent
python agent.py
```

Some agents may require running a web server:

```bash
adk web
```

Refer to each folder's `agent.py` or `main.py` for specific usage.

---

## Examples Overview

- **1_hello_world:** Minimal agent that responds with "Hello, World!"
- **2_tools:** Demonstrates tool integration with agents.
- **3_LLMS:** LLM-powered agents (e.g., joke generator).
- **4_OPS:** Agents for operational tasks (e.g., email generation).
- **5_session_state_runner:** Shows how to maintain session state in memory.
- **6_storage:** Persistent session storage using SQLite.
- **7_multi_agent:** Orchestrates multiple sub-agents for complex tasks.
- **8_custom_tool:** How to add and use custom tools.
- **9_custom_callback:** Custom callback logic for agent events.
- **10_sequential_agent:** Pipeline of agents for sequential processing.
- **11_router_agent:** Routes tasks to the appropriate agent.
- **12_loop_agent:** Agents that loop over tasks (e.g., reviewing LinkedIn posts).

---

## Environment Variables

Most agents require API keys or configuration via `.env` files.  
Common variables include:

- `GOOGLE_API_KEY`
- `GOOGLE_GENAI_USE_VERTEXAI`

**Never share your API keys publicly.**

---

## License

This project is for educational and demonstration purposes.  
See [LICENSE](LICENSE) for details.

---

**Happy experimenting with ADK agents!**
