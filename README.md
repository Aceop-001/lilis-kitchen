# 🍳 Lili’s Kitchen

Lili’s Kitchen is an automated open-source discovery and collection project powered by Grok Bot.

> **Grok Bot discovers open-source projects. Lili’s Kitchen organizes them.**

The idea behind Lili’s Kitchen is simple: there are thousands of amazing open-source projects on GitHub, but finding the genuinely useful ones can take a lot of time. This project aims to make that process easier by discovering interesting repositories, organizing them into categories, and keeping them all in one place.

Grok Bot automatically searches for promising open-source projects and discovers new tools worth exploring. Lili’s Kitchen acts as the library, organizing these discoveries into a structured vault so they are easier to browse, revisit, and use.

The collection covers a wide range of areas, including AI agents, agent skills, local AI models, coding assistants, MCP servers, developer tools, automation, databases, cybersecurity, web development, self-hosted applications, and much more.

The vault currently contains hundreds of repositories, from established open-source projects to newer tools that may be worth keeping an eye on. The goal is not simply to collect as many links as possible, but to make useful projects easier to discover and keep the collection organized as it grows.

## 🎯 The Purpose

- **Discover:** Find interesting and useful open-source projects across GitHub.
- **Organize:** Group repositories into clear categories so they are easy to explore.
- **Collect:** Keep useful projects in one central place instead of losing track of them.
- **Update:** Automate daily discoveries and synchronize them with the existing collection.
- **Explore:** Help developers, builders, and AI enthusiasts find tools and ideas for their next project.

Lili’s Kitchen is an ongoing project that grows with every discovery. Whether you're looking for an AI tool, a coding assistant, a self-hosted application, or an interesting project to experiment with, the goal is to give you a useful starting point.

Discover open source. Stay curious. Build something awesome. 🚀

## 🧑‍🍳 Lili’s Kitchen Agent Skill

The vault is also published as a machine-readable catalog ([`catalog/catalog.json`](catalog/catalog.json), plus a small [`catalog/index.json`](catalog/index.json) and per-category files in [`catalog/categories/`](catalog/categories/)) together with an installable [Agent Skill](https://agentskills.io) at [`skills/lilis-kitchen/`](skills/lilis-kitchen/SKILL.md). An agent that needs a tool, library, framework, MCP server or skill can search the collection and get back linked recommendations with description, language and stars.

**Install (Claude Code, or any agent that reads Agent Skills folders):**

```bash
git clone https://github.com/Aceop-001/lilis-kitchen.git
mkdir -p ~/.claude/skills
cp -r lilis-kitchen/skills/lilis-kitchen ~/.claude/skills/   # personal; or .claude/skills/ inside a project
```

**Use it:** ask your agent things like “Find a browser automation tool for my coding agent”, “Is there an MCP server for GitHub?”, or “Which open-source AI agent framework should I use?”. The agent loads the skill and runs its search script. You can also run it directly (Python 3, no dependencies):

```bash
python3 ~/.claude/skills/lilis-kitchen/scripts/search.py "ai agent framework" --limit 3
```

```text
Lili's Kitchen catalog search: 'ai agent framework' (metadata refreshed 2026-10-22T15:03:39+05:30)
Matches span categories: 🤖 AI agents and agent frameworks (2); 📖 RAG, vector search, and knowledge management (1)

1. mastra-ai/mastra  (score 18.3)
   https://github.com/mastra-ai/mastra
   Mastra is the modern TypeScript framework for AI-powered applications and agents.
   Stars: 29,000 · Language: TypeScript · Category: 🤖 AI agents and agent frameworks
...
```

(Abridged: results 2 and 3 follow in the same format. Scores, star counts and the refresh time change as the catalog is updated.)

**How it stays current:** the catalog is regenerated from the vault by the same daily publishing run that refreshes this README, after the vault sync succeeds, and is committed only when it changes.

**Limitations:** the skill needs shell access with `python3` or a web-fetch tool (it cannot reach the internet on its own); search is keyword-based; results cover only this curated collection; star counts are a daily snapshot, rounded like the README (e.g. 28,997 is stored as 29,000). The skill only recommends projects and never installs them. There is no hosted API or MCP server yet.

## 📚 The Vault

**349 unique repositories** across **17 categories**.

**Last metadata refresh:** 2026-10-31 05:48 IST

**Main project areas:** 🤖 AI agents and agent frameworks · 🧩 Agent skills, reusable instructions, and tool integrations · 🧠 LLM inference, local AI, and model serving · 📖 RAG, vector search, and knowledge management · 💻 AI coding assistants and developer productivity · ⚡ Automation, workflows, and scripting · 🔌 APIs, MCP servers, and integrations · 💾 Databases, storage, backups, and synchronization · 🔐 Security, privacy, and reverse engineering · 🧰 Programming languages, compilers, and developer tooling · 🌐 Web development and application frameworks · 🏠 Self-hosted applications and infrastructure · 🔍 Observability, testing, and debugging · 📊 Data engineering and analytics · 🎓 Research tools, documentation, and learning resources · 🐚 Useful command-line tools and small utilities · 🗽 Digital independence and long-term personal infrastructure

Star counts and primary languages come from GitHub at refresh time. Descriptions come from GitHub; entries marked *(vault note)* use the vault’s own summary because GitHub has none.

### 🗂️ Table of Contents

1. [🤖 AI agents and agent frameworks](#-ai-agents-and-agent-frameworks) (21)
2. [🧩 Agent skills, reusable instructions, and tool integrations](#-agent-skills-reusable-instructions-and-tool-integrations) (12)
3. [🧠 LLM inference, local AI, and model serving](#-llm-inference-local-ai-and-model-serving) (21)
4. [📖 RAG, vector search, and knowledge management](#-rag-vector-search-and-knowledge-management) (19)
5. [💻 AI coding assistants and developer productivity](#-ai-coding-assistants-and-developer-productivity) (18)
6. [⚡ Automation, workflows, and scripting](#-automation-workflows-and-scripting) (14)
7. [🔌 APIs, MCP servers, and integrations](#-apis-mcp-servers-and-integrations) (13)
8. [💾 Databases, storage, backups, and synchronization](#-databases-storage-backups-and-synchronization) (18)
9. [🔐 Security, privacy, and reverse engineering](#-security-privacy-and-reverse-engineering) (37)
10. [🧰 Programming languages, compilers, and developer tooling](#-programming-languages-compilers-and-developer-tooling) (20)
11. [🌐 Web development and application frameworks](#-web-development-and-application-frameworks) (22)
12. [🏠 Self-hosted applications and infrastructure](#-self-hosted-applications-and-infrastructure) (22)
13. [🔍 Observability, testing, and debugging](#-observability-testing-and-debugging) (19)
14. [📊 Data engineering and analytics](#-data-engineering-and-analytics) (19)
15. [🎓 Research tools, documentation, and learning resources](#-research-tools-documentation-and-learning-resources) (22)
16. [🐚 Useful command-line tools and small utilities](#-useful-command-line-tools-and-small-utilities) (29)
17. [🗽 Digital independence and long-term personal infrastructure](#-digital-independence-and-long-term-personal-infrastructure) (23)

---

## 🤖 AI agents and agent frameworks

Frameworks and toolkits for building autonomous AI agents and multi-agent workflows.

### 1. [agno-agi/agno](https://github.com/agno-agi/agno)

The self-driving agent platform

⭐ Stars: 43k  
💻 Language: Python  
🔗 [github.com/agno-agi/agno](https://github.com/agno-agi/agno)

### 2. [browser-use/browser-use](https://github.com/browser-use/browser-use)

Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.

⭐ Stars: 119.6k  
💻 Language: Python  
🔗 [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)

### 3. [crewaiinc/crewai](https://github.com/crewaiinc/crewai)

Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work t…

⭐ Stars: 60.3k  
💻 Language: Python  
🔗 [github.com/crewaiinc/crewai](https://github.com/crewaiinc/crewai)

### 4. [google/adk-python](https://github.com/google/adk-python)

An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

⭐ Stars: 22.1k  
💻 Language: Python  
🔗 [github.com/google/adk-python](https://github.com/google/adk-python)

### 5. [huggingface/smolagents](https://github.com/huggingface/smolagents)

🤗 smolagents: a barebones library for agents that think in code.

⭐ Stars: 30.1k  
💻 Language: Python  
🔗 [github.com/huggingface/smolagents](https://github.com/huggingface/smolagents)

### 6. [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

Build resilient agents.

⭐ Stars: 44.2k  
💻 Language: Python  
🔗 [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

### 7. [letta-ai/letta](https://github.com/letta-ai/letta)

Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.

⭐ Stars: 25.3k  
💻 Language: Unknown  
🔗 [github.com/letta-ai/letta](https://github.com/letta-ai/letta)

### 8. [mastra-ai/mastra](https://github.com/mastra-ai/mastra)

Mastra is the modern TypeScript framework for AI-powered applications and agents.

⭐ Stars: 29.2k  
💻 Language: TypeScript  
🔗 [github.com/mastra-ai/mastra](https://github.com/mastra-ai/mastra)

### 9. [mem0ai/mem0](https://github.com/mem0ai/mem0)

The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production.

⭐ Stars: 68.1k  
💻 Language: Python  
🔗 [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)

### 10. [microsoft/autogen](https://github.com/microsoft/autogen)

A programming framework for agentic AI

⭐ Stars: 61.6k  
💻 Language: Python  
🔗 [github.com/microsoft/autogen](https://github.com/microsoft/autogen)

### 11. [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)

Integrate cutting-edge LLM technology quickly and easily into your apps

⭐ Stars: 28.7k  
💻 Language: C#  
🔗 [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)

### 12. [omnara-ai/omnara](https://github.com/omnara-ai/omnara)

The open-source managed agent platform. A self-hostable alternative to Claude Managed Agents and OpenAI's Agents API.

⭐ Stars: 3.3k  
💻 Language: Go  
🔗 [github.com/omnara-ai/omnara](https://github.com/omnara-ai/omnara)

### 13. [openai/openai-agents-python](https://github.com/openai/openai-agents-python)

A lightweight, powerful framework for multi-agent workflows

⭐ Stars: 30.4k  
💻 Language: Python  
🔗 [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)

### 14. [openhands/openhands](https://github.com/openhands/openhands)

🙌 OpenHands: AI-Driven Development

⭐ Stars: 92.3k  
💻 Language: TypeScript  
🔗 [github.com/openhands/openhands](https://github.com/openhands/openhands)

### 15. [openmathmodel/open-math-harness](https://github.com/openmathmodel/open-math-harness)

The harness of Open Math OS, infrastructure for Math 2.0. Built for everyday math research.

⭐ Stars: 207  
💻 Language: Rust  
🔗 [github.com/openmathmodel/open-math-harness](https://github.com/openmathmodel/open-math-harness)

### 16. [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck)

A Tiny biped duck robot 🦆

⭐ Stars: 13.2k  
💻 Language: Rust  
🔗 [github.com/pollen-robotics/microduck](https://github.com/pollen-robotics/microduck)

### 17. [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)

How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

⭐ Stars: 21k  
💻 Language: Python  
🔗 [github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)

### 18. [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

DSPy: The framework for programming—not prompting—language models

⭐ Stars: 38.9k  
💻 Language: Python  
🔗 [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

### 19. [swe-agent/swe-agent](https://github.com/swe-agent/swe-agent)

SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersec…

⭐ Stars: 20.7k  
💻 Language: Python  
🔗 [github.com/swe-agent/swe-agent](https://github.com/swe-agent/swe-agent)

### 20. [wangzan101/mika](https://github.com/wangzan101/mika)

Mika — 你手机上的私人 AI 助理，替你操作 App、上网、把事办成。An on-device AI agent for Android that operates apps and the web to get things done for you.

⭐ Stars: 1.3k  
💻 Language: Kotlin  
🔗 [github.com/wangzan101/mika](https://github.com/wangzan101/mika)

### 21. [xingjian-bai/opal](https://github.com/xingjian-bai/opal)

OPAL: a reactive optimizer. A coding agent rewrites the optimizer while your model trains.

⭐ Stars: 252  
💻 Language: Python  
🔗 [github.com/xingjian-bai/opal](https://github.com/xingjian-bai/opal)


---

## 🧩 Agent skills, reusable instructions, and tool integrations

Reusable agent skills, instruction sets, and tool integrations that extend what agents can do.

### 1. [agentsmd/agents.md](https://github.com/agentsmd/agents.md)

AGENTS.md — a simple, open format for guiding coding agents

⭐ Stars: 25.2k  
💻 Language: TypeScript  
🔗 [github.com/agentsmd/agents.md](https://github.com/agentsmd/agents.md)

### 2. [anthropics/claude-code](https://github.com/anthropics/claude-code)

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing rout…

⭐ Stars: 154k  
💻 Language: TypeScript  
🔗 [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)

### 3. [anthropics/skills](https://github.com/anthropics/skills)

Public repository for Agent Skills

⭐ Stars: 185.3k  
💻 Language: Python  
🔗 [github.com/anthropics/skills](https://github.com/anthropics/skills)

### 4. [composiohq/awesome-claude-skills](https://github.com/composiohq/awesome-claude-skills)

A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

⭐ Stars: 78.4k  
💻 Language: Python  
🔗 [github.com/composiohq/awesome-claude-skills](https://github.com/composiohq/awesome-claude-skills)

### 5. [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

An open-source AI agent that brings the power of Gemini directly into your terminal.

⭐ Stars: 108.6k  
💻 Language: TypeScript  
🔗 [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

### 6. [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding compan…

⭐ Stars: 56.9k  
💻 Language: Python  
🔗 [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

### 7. [obra/superpowers](https://github.com/obra/superpowers)

An agentic skills framework & software development methodology that works.

⭐ Stars: 309.4k  
💻 Language: Shell  
🔗 [github.com/obra/superpowers](https://github.com/obra/superpowers)

### 8. [openai/codex](https://github.com/openai/codex)

Lightweight coding agent that runs in your terminal

⭐ Stars: 131.9k  
💻 Language: Rust  
🔗 [github.com/openai/codex](https://github.com/openai/codex)

### 9. [patrickjs/awesome-cursorrules](https://github.com/patrickjs/awesome-cursorrules)

📄 Configuration files that enhance Cursor AI editor experience with custom rules and behaviors

⭐ Stars: 41.1k  
💻 Language: JavaScript  
🔗 [github.com/patrickjs/awesome-cursorrules](https://github.com/patrickjs/awesome-cursorrules)

### 10. [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)

A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code

⭐ Stars: 15.6k  
💻 Language: Unknown  
🔗 [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)

### 11. [voltagent/awesome-claude-code-subagents](https://github.com/voltagent/awesome-claude-code-subagents)

A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases

⭐ Stars: 26.2k  
💻 Language: Shell  
🔗 [github.com/voltagent/awesome-claude-code-subagents](https://github.com/voltagent/awesome-claude-code-subagents)

### 12. [wshobson/agents](https://github.com/wshobson/agents)

Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi

⭐ Stars: 42k  
💻 Language: Python  
🔗 [github.com/wshobson/agents](https://github.com/wshobson/agents)


---

## 🧠 LLM inference, local AI, and model serving

Tools for running, serving, and optimizing AI models locally or on your own infrastructure.

### 1. [berriai/litellm](https://github.com/berriai/litellm)

The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails…

⭐ Stars: 62.4k  
💻 Language: Python  
🔗 [github.com/berriai/litellm](https://github.com/berriai/litellm)

### 2. [comfy-org/comfyui](https://github.com/comfy-org/comfyui)

The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in th…

⭐ Stars: 144.2k  
💻 Language: Python  
🔗 [github.com/comfy-org/comfyui](https://github.com/comfy-org/comfyui)

### 3. [exo-explore/exo](https://github.com/exo-explore/exo)

Run frontier AI locally.

⭐ Stars: 48.1k  
💻 Language: Python  
🔗 [github.com/exo-explore/exo](https://github.com/exo-explore/exo)

### 4. [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

LLM inference in C/C++

⭐ Stars: 132.9k  
💻 Language: C++  
🔗 [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

### 5. [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

Port of OpenAI's Whisper model in C/C++

⭐ Stars: 54.8k  
💻 Language: C++  
🔗 [github.com/ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

### 6. [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)

Large Language Model Text Generation Inference *(archived)*

⭐ Stars: 10.9k  
💻 Language: Python  
🔗 [github.com/huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)

### 7. [huggingface/transformers](https://github.com/huggingface/transformers)

🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models…

⭐ Stars: 168.4k  
💻 Language: Python  
🔗 [github.com/huggingface/transformers](https://github.com/huggingface/transformers)

### 8. [huggingface/trl](https://github.com/huggingface/trl)

Train transformer language models with reinforcement learning.

⭐ Stars: 19.6k  
💻 Language: Python  
🔗 [github.com/huggingface/trl](https://github.com/huggingface/trl)

### 9. [justaresearcher/gpu-unlock-ada](https://github.com/justaresearcher/gpu-unlock-ada)

GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmware generated locally

⭐ Stars: 4.6k  
💻 Language: C  
🔗 [github.com/justaresearcher/gpu-unlock-ada](https://github.com/justaresearcher/gpu-unlock-ada)

### 10. [ml-explore/mlx](https://github.com/ml-explore/mlx)

MLX: An array framework for Apple silicon

⭐ Stars: 29k  
💻 Language: C++  
🔗 [github.com/ml-explore/mlx](https://github.com/ml-explore/mlx)

### 11. [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)

Run LLMs with MLX

⭐ Stars: 7.5k  
💻 Language: Python  
🔗 [github.com/ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)

### 12. [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)

Distribute and run LLMs with a single file.

⭐ Stars: 26.5k  
💻 Language: C++  
🔗 [github.com/mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)

### 13. [NVIDIA/spark-local-inference](https://github.com/NVIDIA/spark-local-inference)

Local LLM inference server for NVIDIA SM120/SM121 GPUs (incl. DGX Spark) that compiles models with PyTorch at build time and serves them… *(vault note)* *(renamed from nvidia/flare-local-inference)*

⭐ Stars: 703  
💻 Language: Rust  
🔗 [github.com/NVIDIA/spark-local-inference](https://github.com/NVIDIA/spark-local-inference)

### 14. [nvidia/tensorrt-llm](https://github.com/nvidia/tensorrt-llm)

TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizat…

⭐ Stars: 15k  
💻 Language: Python  
🔗 [github.com/nvidia/tensorrt-llm](https://github.com/nvidia/tensorrt-llm)

### 15. [ollama/ollama](https://github.com/ollama/ollama)

Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

⭐ Stars: 185.4k  
💻 Language: Go  
🔗 [github.com/ollama/ollama](https://github.com/ollama/ollama)

### 16. [open-webui/open-webui](https://github.com/open-webui/open-webui)

User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

⭐ Stars: 157.3k  
💻 Language: Python  
🔗 [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)

### 17. [openbmb/minicpm-ocr](https://github.com/openbmb/minicpm-ocr)

Fast, accurate OCR with correctness assessment.

⭐ Stars: 670  
💻 Language: TypeScript  
🔗 [github.com/openbmb/minicpm-ocr](https://github.com/openbmb/minicpm-ocr)

### 18. [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang is a high-performance serving framework for large language models and multimodal models.

⭐ Stars: 38.3k  
💻 Language: Python  
🔗 [github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)

### 19. [systran/faster-whisper](https://github.com/systran/faster-whisper)

Faster Whisper transcription with CTranslate2

⭐ Stars: 26.3k  
💻 Language: Python  
🔗 [github.com/systran/faster-whisper](https://github.com/systran/faster-whisper)

### 20. [unslothai/unsloth](https://github.com/unslothai/unsloth)

Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.

⭐ Stars: 78.8k  
💻 Language: Python  
🔗 [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)

### 21. [vllm-project/vllm](https://github.com/vllm-project/vllm)

A high-throughput and memory-efficient inference and serving engine for LLMs

⭐ Stars: 95.9k  
💻 Language: Python  
🔗 [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm)


---

## 📖 RAG, vector search, and knowledge management

Retrieval-augmented generation, vector databases, and knowledge-management systems.

### 1. [chroma-core/chroma](https://github.com/chroma-core/chroma)

Search infrastructure for AI

⭐ Stars: 29.6k  
💻 Language: Rust  
🔗 [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma)

### 2. [datalab-to/marker](https://github.com/datalab-to/marker)

Convert PDF to markdown + JSON quickly with high accuracy

⭐ Stars: 40.7k  
💻 Language: Python  
🔗 [github.com/datalab-to/marker](https://github.com/datalab-to/marker)

### 3. [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and a…

⭐ Stars: 26.9k  
💻 Language: Python  
🔗 [github.com/deepset-ai/haystack](https://github.com/deepset-ai/haystack)

### 4. [docling-project/docling](https://github.com/docling-project/docling)

Get your documents ready for gen AI

⭐ Stars: 69.9k  
💻 Language: Python  
🔗 [github.com/docling-project/docling](https://github.com/docling-project/docling)

### 5. [facebookresearch/faiss](https://github.com/facebookresearch/faiss)

A library for efficient similarity search and clustering of dense vectors.

⭐ Stars: 41.2k  
💻 Language: C++  
🔗 [github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss)

### 6. [hkuds/lightrag](https://github.com/hkuds/lightrag)

\[EMNLP2025\] LightRAG: Simple and Fast Retrieval-Augmented Generation

⭐ Stars: 40.4k  
💻 Language: Python  
🔗 [github.com/hkuds/lightrag](https://github.com/hkuds/lightrag)

### 7. [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to creat…

⭐ Stars: 93.2k  
💻 Language: Go  
🔗 [github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)

### 8. [lancedb/lancedb](https://github.com/lancedb/lancedb)

Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less.

⭐ Stars: 11.8k  
💻 Language: Rust  
🔗 [github.com/lancedb/lancedb](https://github.com/lancedb/lancedb)

### 9. [langchain-ai/langchain](https://github.com/langchain-ai/langchain)

The agent engineering platform.

⭐ Stars: 148.7k  
💻 Language: Python  
🔗 [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

### 10. [logseq/logseq](https://github.com/logseq/logseq)

A privacy-first, open-source platform for knowledge management and collaboration. Download link: http://github.com/logseq/logseq/releases…

⭐ Stars: 45.4k  
💻 Language: Clojure  
🔗 [github.com/logseq/logseq](https://github.com/logseq/logseq)

### 11. [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications.

⭐ Stars: 59.7k  
💻 Language: Rust  
🔗 [github.com/meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

### 12. [microsoft/graphrag](https://github.com/microsoft/graphrag)

A modular graph-based Retrieval-Augmented Generation (RAG) system

⭐ Stars: 36.5k  
💻 Language: Python  
🔗 [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)

### 13. [milvus-io/milvus](https://github.com/milvus-io/milvus)

Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

⭐ Stars: 46.5k  
💻 Language: Go  
🔗 [github.com/milvus-io/milvus](https://github.com/milvus-io/milvus)

### 14. [pgvector/pgvector](https://github.com/pgvector/pgvector)

Open-source vector similarity search for Postgres

⭐ Stars: 23.5k  
💻 Language: C  
🔗 [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)

### 15. [qdrant/qdrant](https://github.com/qdrant/qdrant)

Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cl…

⭐ Stars: 35.3k  
💻 Language: Rust  
🔗 [github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)

### 16. [run-llama/llama_index](https://github.com/run-llama/llama_index)

LlamaIndex is the document processing platform for AI

⭐ Stars: 52.8k  
💻 Language: Python  
🔗 [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)

### 17. [typesense/typesense](https://github.com/typesense/typesense)

Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch ⚡ 🔍 ✨ Fast, typo tolerant, in-memory fuzz…

⭐ Stars: 27.1k  
💻 Language: C++  
🔗 [github.com/typesense/typesense](https://github.com/typesense/typesense)

### 18. [unstructured-io/unstructured](https://github.com/unstructured-io/unstructured)

Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean…

⭐ Stars: 15.6k  
💻 Language: HTML  
🔗 [github.com/unstructured-io/unstructured](https://github.com/unstructured-io/unstructured)

### 19. [weaviate/weaviate](https://github.com/weaviate/weaviate)

Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with struc…

⭐ Stars: 16.9k  
💻 Language: Go  
🔗 [github.com/weaviate/weaviate](https://github.com/weaviate/weaviate)


---

## 💻 AI coding assistants and developer productivity

AI coding assistants and tools that make developers more productive.

### 1. [aider-ai/aider](https://github.com/aider-ai/aider)

aider is AI pair programming in your terminal

⭐ Stars: 49.8k  
💻 Language: Python  
🔗 [github.com/aider-ai/aider](https://github.com/aider-ai/aider)

### 2. [anomalyco/opencode](https://github.com/anomalyco/opencode)

The open source coding agent.

⭐ Stars: 223.3k  
💻 Language: TypeScript  
🔗 [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)

### 3. [cline/cline](https://github.com/cline/cline)

Autonomous coding agent as an SDK, IDE extension, or CLI assistant.

⭐ Stars: 71.1k  
💻 Language: TypeScript  
🔗 [github.com/cline/cline](https://github.com/cline/cline)

### 4. [continuedev/continue](https://github.com/continuedev/continue)

open-source coding agent

⭐ Stars: 36.4k  
💻 Language: TypeScript  
🔗 [github.com/continuedev/continue](https://github.com/continuedev/continue)

### 5. [dandavison/delta](https://github.com/dandavison/delta)

A syntax-highlighting pager for git, diff, grep, rg --json, and blame output

⭐ Stars: 32.6k  
💻 Language: Rust  
🔗 [github.com/dandavison/delta](https://github.com/dandavison/delta)

### 6. [dominikmartn/harp](https://github.com/dominikmartn/harp)

Run many Claude Code and Codex agents side by side, in one sidebar that tells you which one needs you. An unofficial fork of Warp.

⭐ Stars: 694  
💻 Language: Rust  
🔗 [github.com/dominikmartn/harp](https://github.com/dominikmartn/harp)

### 7. [helix-editor/helix](https://github.com/helix-editor/helix)

A post-modern modal text editor.

⭐ Stars: 46.7k  
💻 Language: Rust  
🔗 [github.com/helix-editor/helix](https://github.com/helix-editor/helix)

### 8. [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

simple terminal UI for git commands

⭐ Stars: 83.5k  
💻 Language: Go  
🔗 [github.com/jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

### 9. [jetbrains/thinkrail](https://github.com/jetbrains/thinkrail)

Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need

⭐ Stars: 6.6k  
💻 Language: TypeScript  
🔗 [github.com/jetbrains/thinkrail](https://github.com/jetbrains/thinkrail)

### 10. [microsoft/vscode](https://github.com/microsoft/vscode)

Visual Studio Code

⭐ Stars: 194.4k  
💻 Language: TypeScript  
🔗 [github.com/microsoft/vscode](https://github.com/microsoft/vscode)

### 11. [neovim/neovim](https://github.com/neovim/neovim)

Vim-fork focused on extensibility and usability

⭐ Stars: 103.3k  
💻 Language: Vim Script  
🔗 [github.com/neovim/neovim](https://github.com/neovim/neovim)

### 12. [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)

A framework for managing and maintaining multi-language pre-commit hooks.

⭐ Stars: 15.7k  
💻 Language: Python  
🔗 [github.com/pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)

### 13. [roocodeinc/roo-code](https://github.com/roocodeinc/roo-code)

Roo Code gives you a whole dev team of AI agents in your code editor. *(archived)*

⭐ Stars: 24.3k  
💻 Language: TypeScript  
🔗 [github.com/roocodeinc/roo-code](https://github.com/roocodeinc/roo-code)

### 14. [rudderlabs/devbox](https://github.com/rudderlabs/devbox)

Open source autonomous engineering harness in your cloud. One sandbox per task, no real secrets inside.

⭐ Stars: 236  
💻 Language: TypeScript  
🔗 [github.com/rudderlabs/devbox](https://github.com/rudderlabs/devbox)

### 15. [tabbyml/tabby](https://github.com/tabbyml/tabby)

Self-hosted AI coding assistant

⭐ Stars: 33.9k  
💻 Language: Rust  
🔗 [github.com/tabbyml/tabby](https://github.com/tabbyml/tabby)

### 16. [tals/corgi](https://github.com/tals/corgi)

Happy helper for your terminal

⭐ Stars: 188  
💻 Language: TypeScript  
🔗 [github.com/tals/corgi](https://github.com/tals/corgi)

### 17. [yamadashy/repomix](https://github.com/yamadashy/repomix)

📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your co…

⭐ Stars: 29.1k  
💻 Language: TypeScript  
🔗 [github.com/yamadashy/repomix](https://github.com/yamadashy/repomix)

### 18. [zed-industries/zed](https://github.com/zed-industries/zed)

Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

⭐ Stars: 92.4k  
💻 Language: Rust  
🔗 [github.com/zed-industries/zed](https://github.com/zed-industries/zed)


---

## ⚡ Automation, workflows, and scripting

Workflow automation, task runners, and scripting tools.

### 1. [activepieces/activepieces](https://github.com/activepieces/activepieces)

AI Agents & MCPs & AI Workflow Automation • (\~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Age…

⭐ Stars: 25.3k  
💻 Language: TypeScript  
🔗 [github.com/activepieces/activepieces](https://github.com/activepieces/activepieces)

### 2. [ansible/ansible](https://github.com/ansible/ansible)

Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate eve…

⭐ Stars: 71.2k  
💻 Language: Python  
🔗 [github.com/ansible/ansible](https://github.com/ansible/ansible)

### 3. [apache/airflow](https://github.com/apache/airflow)

Apache Airflow - A platform to programmatically author, schedule, and monitor workflows

⭐ Stars: 47.3k  
💻 Language: Python  
🔗 [github.com/apache/airflow](https://github.com/apache/airflow)

### 4. [casey/just](https://github.com/casey/just)

🤖 Just a command runner

⭐ Stars: 36.5k  
💻 Language: Rust  
🔗 [github.com/casey/just](https://github.com/casey/just)

### 5. [go-task/task](https://github.com/go-task/task)

A fast, cross-platform build tool inspired by Make, designed for modern workflows.

⭐ Stars: 16.3k  
💻 Language: Go  
🔗 [github.com/go-task/task](https://github.com/go-task/task)

### 6. [home-assistant/core](https://github.com/home-assistant/core)

:house\_with\_garden: Open source home automation that puts local control and privacy first.

⭐ Stars: 91.9k  
💻 Language: Python  
🔗 [github.com/home-assistant/core](https://github.com/home-assistant/core)

### 7. [huginn/huginn](https://github.com/huginn/huginn)

Create agents that monitor and act on your behalf. Your agents are standing by!

⭐ Stars: 50.2k  
💻 Language: Ruby  
🔗 [github.com/huginn/huginn](https://github.com/huginn/huginn)

### 8. [microsoft/playwright](https://github.com/microsoft/playwright)

Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.

⭐ Stars: 98.9k  
💻 Language: TypeScript  
🔗 [github.com/microsoft/playwright](https://github.com/microsoft/playwright)

### 9. [n8n-io/n8n](https://github.com/n8n-io/n8n)

Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ in…

⭐ Stars: 209.2k  
💻 Language: TypeScript  
🔗 [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)

### 10. [node-red/node-red](https://github.com/node-red/node-red)

Low-code programming for event-driven applications

⭐ Stars: 23.8k  
💻 Language: JavaScript  
🔗 [github.com/node-red/node-red](https://github.com/node-red/node-red)

### 11. [prefecthq/prefect](https://github.com/prefecthq/prefect)

Prefect is a workflow orchestration framework for building resilient data pipelines in Python.

⭐ Stars: 24.1k  
💻 Language: Python  
🔗 [github.com/prefecthq/prefect](https://github.com/prefecthq/prefect)

### 12. [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer)

JavaScript API for Chrome and Firefox

⭐ Stars: 95.8k  
💻 Language: TypeScript  
🔗 [github.com/puppeteer/puppeteer](https://github.com/puppeteer/puppeteer)

### 13. [temporalio/temporal](https://github.com/temporalio/temporal)

Temporal service

⭐ Stars: 24.1k  
💻 Language: Go  
🔗 [github.com/temporalio/temporal](https://github.com/temporalio/temporal)

### 14. [windmill-labs/windmill](https://github.com/windmill-labs/windmill)

Code-first platform for workflows, apps and AI agents, on the fastest self-hostable orchestrator (benchmarked against Airflow, Prefect an…

⭐ Stars: 18.3k  
💻 Language: Rust  
🔗 [github.com/windmill-labs/windmill](https://github.com/windmill-labs/windmill)


---

## 🔌 APIs, MCP servers, and integrations

API tooling, Model Context Protocol (MCP) servers, and service integrations.

### 1. [github/github-mcp-server](https://github.com/github/github-mcp-server)

GitHub's official MCP Server

⭐ Stars: 34.1k  
💻 Language: Go  
🔗 [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server)

### 2. [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch)

Open-Source API Development Ecosystem • https://hoppscotch.io • Offline, On-Prem & Cloud • Web, Desktop & CLI • Open-Source Alternative t…

⭐ Stars: 80.7k  
💻 Language: TypeScript  
🔗 [github.com/hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch)

### 3. [kong/kong](https://github.com/kong/kong)

🦍 The API and AI Gateway

⭐ Stars: 44.3k  
💻 Language: Lua  
🔗 [github.com/kong/kong](https://github.com/kong/kong)

### 4. [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

Playwright MCP server

⭐ Stars: 38.9k  
💻 Language: TypeScript  
🔗 [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

### 5. [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

Deterministic testing tools for MCP servers

⭐ Stars: 11.2k  
💻 Language: TypeScript  
🔗 [github.com/modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

### 6. [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)

Specification and documentation for the Model Context Protocol

⭐ Stars: 9.6k  
💻 Language: TypeScript  
🔗 [github.com/modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)

### 7. [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

The official Python SDK for Model Context Protocol servers and clients

⭐ Stars: 24.7k  
💻 Language: Python  
🔗 [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

### 8. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

Model Context Protocol Servers

⭐ Stars: 91.7k  
💻 Language: TypeScript  
🔗 [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

### 9. [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

The official TypeScript SDK for Model Context Protocol servers and clients

⭐ Stars: 13.7k  
💻 Language: TypeScript  
🔗 [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

### 10. [oai/openapi-specification](https://github.com/oai/openapi-specification)

The OpenAPI Specification Repository

⭐ Stars: 31.3k  
💻 Language: Markdown  
🔗 [github.com/oai/openapi-specification](https://github.com/oai/openapi-specification)

### 11. [prefecthq/fastmcp](https://github.com/prefecthq/fastmcp)

🚀 The fast, Pythonic way to build MCP servers and clients.

⭐ Stars: 28.2k  
💻 Language: Python  
🔗 [github.com/prefecthq/fastmcp](https://github.com/prefecthq/fastmcp)

### 12. [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

A collection of MCP servers.

⭐ Stars: 97.1k  
💻 Language: Unknown  
🔗 [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

### 13. [usebruno/bruno](https://github.com/usebruno/bruno)

Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)

⭐ Stars: 48k  
💻 Language: JavaScript  
🔗 [github.com/usebruno/bruno](https://github.com/usebruno/bruno)


---

## 💾 Databases, storage, backups, and synchronization

Databases, storage engines, backup tools, and file synchronization.

### 1. [benbjohnson/litestream](https://github.com/benbjohnson/litestream)

Streaming replication for SQLite.

⭐ Stars: 14.6k  
💻 Language: Go  
🔗 [github.com/benbjohnson/litestream](https://github.com/benbjohnson/litestream)

### 2. [borgbackup/borg](https://github.com/borgbackup/borg)

Deduplicating archiver with compression and authenticated encryption.

⭐ Stars: 13.9k  
💻 Language: Python  
🔗 [github.com/borgbackup/borg](https://github.com/borgbackup/borg)

### 3. [clickhouse/clickhouse](https://github.com/clickhouse/clickhouse)

ClickHouse® is a real-time analytics database management system

⭐ Stars: 50.7k  
💻 Language: C++  
🔗 [github.com/clickhouse/clickhouse](https://github.com/clickhouse/clickhouse)

### 4. [duckdb/duckdb](https://github.com/duckdb/duckdb)

DuckDB is a high-performance analytical database system

⭐ Stars: 42.7k  
💻 Language: C++  
🔗 [github.com/duckdb/duckdb](https://github.com/duckdb/duckdb)

### 5. [kividbio/kividb](https://github.com/kividbio/kividb)

A fast, multi-threaded Redis® and Valkey alternative written in Rust: drop-in compatible, with full-text and vector search built in

⭐ Stars: 916  
💻 Language: Rust  
🔗 [github.com/kividbio/kividb](https://github.com/kividbio/kividb)

### 6. [kopia/kopia](https://github.com/kopia/kopia)

Cross-platform backup tool for Windows, macOS & Linux with fast, incremental backups, client-side end-to-end encryption, compression and…

⭐ Stars: 14.5k  
💻 Language: Go  
🔗 [github.com/kopia/kopia](https://github.com/kopia/kopia)

### 7. [minio/minio](https://github.com/minio/minio)

MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. *(archived)*

⭐ Stars: 61.3k  
💻 Language: Go  
🔗 [github.com/minio/minio](https://github.com/minio/minio)

### 8. [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)

Open Source realtime backend in 1 file *(archived)*

⭐ Stars: 61.6k  
💻 Language: Go  
🔗 [github.com/pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)

### 9. [postgres/postgres](https://github.com/postgres/postgres)

Mirror of the official PostgreSQL GIT repository. Note that this is just a \*mirror\* - we don't work with pull requests on github. To cont…

⭐ Stars: 22.6k  
💻 Language: C  
🔗 [github.com/postgres/postgres](https://github.com/postgres/postgres)

### 10. [rclone/rclone](https://github.com/rclone/rclone)

"rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, A…

⭐ Stars: 60.7k  
💻 Language: Go  
🔗 [github.com/rclone/rclone](https://github.com/rclone/rclone)

### 11. [redis/redis](https://github.com/redis/redis)

For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data s…

⭐ Stars: 77.1k  
💻 Language: C  
🔗 [github.com/redis/redis](https://github.com/redis/redis)

### 12. [restic/restic](https://github.com/restic/restic)

Fast, secure, efficient backup program

⭐ Stars: 36.9k  
💻 Language: Go  
🔗 [github.com/restic/restic](https://github.com/restic/restic)

### 13. [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs)

SeaweedFS is a distributed storage system for object storage (S3), file systems, and Iceberg tables, designed to handle billions of files…

⭐ Stars: 35.8k  
💻 Language: Go  
🔗 [github.com/seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs)

### 14. [sqlite/sqlite](https://github.com/sqlite/sqlite)

Official Git mirror of the SQLite source tree

⭐ Stars: 10.9k  
💻 Language: C  
🔗 [github.com/sqlite/sqlite](https://github.com/sqlite/sqlite)

### 15. [supabase/supabase](https://github.com/supabase/supabase)

The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

⭐ Stars: 114.3k  
💻 Language: TypeScript  
🔗 [github.com/supabase/supabase](https://github.com/supabase/supabase)

### 16. [syncthing/syncthing](https://github.com/syncthing/syncthing)

Open Source Continuous File Synchronization

⭐ Stars: 89.9k  
💻 Language: Go  
🔗 [github.com/syncthing/syncthing](https://github.com/syncthing/syncthing)

### 17. [tursodatabase/libsql](https://github.com/tursodatabase/libsql)

libSQL is a fork of SQLite that is both Open Source, and Open Contributions.

⭐ Stars: 17.3k  
💻 Language: C  
🔗 [github.com/tursodatabase/libsql](https://github.com/tursodatabase/libsql)

### 18. [valkey-io/valkey](https://github.com/valkey-io/valkey)

A flexible distributed key-value database that is optimized for caching and other realtime workloads.

⭐ Stars: 27.6k  
💻 Language: C  
🔗 [github.com/valkey-io/valkey](https://github.com/valkey-io/valkey)


---

## 🔐 Security, privacy, and reverse engineering

Security, privacy, and reverse-engineering tools.

### 1. [Snapintosh/Snapintosh](https://github.com/Snapintosh/Snapintosh)

EL2 hypervisor and toolchain that boots macOS on the ASUS A16 (Snapdragon X2 Elite), with an Adreno Metal/IOGPU stack *(renamed from acelogic/snapintosh)*

⭐ Stars: 1.1k  
💻 Language: Python  
🔗 [github.com/Snapintosh/Snapintosh](https://github.com/Snapintosh/Snapintosh)

### 2. [aquasecurity/trivy](https://github.com/aquasecurity/trivy)

Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more

⭐ Stars: 38.9k  
💻 Language: Go  
🔗 [github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)

### 3. [bitwarden/server](https://github.com/bitwarden/server)

Bitwarden infrastructure/backend (API, database, Docker, etc).

⭐ Stars: 20.5k  
💻 Language: C#  
🔗 [github.com/bitwarden/server](https://github.com/bitwarden/server)

### 4. [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden\_rs

⭐ Stars: 70k  
💻 Language: Rust  
🔗 [github.com/dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

### 5. [filosottile/age](https://github.com/filosottile/age)

A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.

⭐ Stars: 24.1k  
💻 Language: Go  
🔗 [github.com/filosottile/age](https://github.com/filosottile/age)

### 6. [frida/frida](https://github.com/frida/frida)

Main repo for hosting release binaries

⭐ Stars: 22.6k  
💻 Language: Meson  
🔗 [github.com/frida/frida](https://github.com/frida/frida)

### 7. [getsops/sops](https://github.com/getsops/sops)

Simple and flexible tool for managing secrets

⭐ Stars: 23.6k  
💻 Language: Go  
🔗 [github.com/getsops/sops](https://github.com/getsops/sops)

### 8. [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

Find secrets with Gitleaks 🔑

⭐ Stars: 30.5k  
💻 Language: Go  
🔗 [github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

### 9. [gothamor/gta-vcs-recomp](https://github.com/gothamor/gta-vcs-recomp)

A native Windows and Linux port of Grand Theft Auto: Vice City Stories (PS2, USA, SLUS-21590), made by recompiling the game's PS2 executa…

⭐ Stars: 118  
💻 Language: C++  
🔗 [github.com/gothamor/gta-vcs-recomp](https://github.com/gothamor/gta-vcs-recomp)

### 10. [hashicorp/vault](https://github.com/hashicorp/vault)

A tool for secrets management, encryption as a service, and privileged access management

⭐ Stars: 36.5k  
💻 Language: Go  
🔗 [github.com/hashicorp/vault](https://github.com/hashicorp/vault)

### 11. [hevnsnt/cvengine](https://github.com/hevnsnt/cvengine)

AI-first external attack surface assessment with continuous discovery, evidence-based vulnerability validation, and developer-agent MCP i…

⭐ Stars: 537  
💻 Language: Python  
🔗 [github.com/hevnsnt/cvengine](https://github.com/hevnsnt/cvengine)

### 12. [interplains/zero-breach-toolkit](https://github.com/interplains/zero-breach-toolkit)

Free, open-source, offline checks for traces of known mercenary spyware. Works on Windows, macOS and Linux, Android phones and iPhone bac…

⭐ Stars: 3.9k  
💻 Language: Python  
🔗 [github.com/interplains/zero-breach-toolkit](https://github.com/interplains/zero-breach-toolkit)

### 13. [juanfont/headscale](https://github.com/juanfont/headscale)

An open source, self-hosted implementation of the Tailscale control server

⭐ Stars: 45.2k  
💻 Language: Go  
🔗 [github.com/juanfont/headscale](https://github.com/juanfont/headscale)

### 14. [katrielmoses/voidaccess](https://github.com/katrielmoses/voidaccess)

Self-hosted dark web OSINT platform. Automated threat intelligence from query to graph in 13 steps. Free alternative to Recorded Future,…

⭐ Stars: 962  
💻 Language: Python  
🔗 [github.com/katrielmoses/voidaccess](https://github.com/katrielmoses/voidaccess)

### 15. [keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

KeePassXC is a cross-platform community-driven port of the Windows application “KeePass Password Safe”.

⭐ Stars: 29.6k  
💻 Language: C++  
🔗 [github.com/keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)

### 16. [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.

⭐ Stars: 46.5k  
💻 Language: Python  
🔗 [github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

### 17. [nationalsecurityagency/ghidra](https://github.com/nationalsecurityagency/ghidra)

Ghidra is a software reverse engineering (SRE) framework

⭐ Stars: 96.2k  
💻 Language: Java  
🔗 [github.com/nationalsecurityagency/ghidra](https://github.com/nationalsecurityagency/ghidra)

### 18. [nmap/nmap](https://github.com/nmap/nmap)

Nmap - the Network Mapper. Github mirror of official SVN repository.

⭐ Stars: 13.9k  
💻 Language: C  
🔗 [github.com/nmap/nmap](https://github.com/nmap/nmap)

### 19. [nvidia/garak](https://github.com/nvidia/garak)

the LLM vulnerability scanner

⭐ Stars: 9.8k  
💻 Language: Python  
🔗 [github.com/nvidia/garak](https://github.com/nvidia/garak)

### 20. [openai/php2shell-checker](https://github.com/openai/php2shell-checker)

Node script plus Codex skills that check a website or local PHP binary against the patched-version cutoff for the php2shell vulnerabiliti… *(vault note)*

⭐ Stars: 1.5k  
💻 Language: JavaScript  
🔗 [github.com/openai/php2shell-checker](https://github.com/openai/php2shell-checker)

### 21. [openbao/openbao](https://github.com/openbao/openbao)

OpenBao is a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys.

⭐ Stars: 8.8k  
💻 Language: Go  
🔗 [github.com/openbao/openbao](https://github.com/openbao/openbao)

### 22. [openssl/openssl](https://github.com/openssl/openssl)

General purpose TLS and crypto library

⭐ Stars: 31.1k  
💻 Language: C  
🔗 [github.com/openssl/openssl](https://github.com/openssl/openssl)

### 23. [opentrap/opentrap](https://github.com/opentrap/opentrap)

A free, open-source alternative to Burp Suite: an intercepting proxy and web app security testing suite with Repeater, Intruder, Collabor…

⭐ Stars: 596  
💻 Language: Java  
🔗 [github.com/opentrap/opentrap](https://github.com/opentrap/opentrap)

### 24. [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML-based DSL, enabl…

⭐ Stars: 32.5k  
💻 Language: Go  
🔗 [github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

### 25. [protectai/llm-guard](https://github.com/protectai/llm-guard)

The Security Toolkit for LLM Interactions *(archived)*

⭐ Stars: 3.2k  
💻 Language: Python  
🔗 [github.com/protectai/llm-guard](https://github.com/protectai/llm-guard)

### 26. [prototux/aare](https://github.com/prototux/aare)

A proof-of-concept opensource implementation of Android Auto's client side (phone side)

⭐ Stars: 285  
💻 Language: Kotlin  
🔗 [github.com/prototux/aare](https://github.com/prototux/aare)

### 27. [radareorg/radare2](https://github.com/radareorg/radare2)

UNIX-like reverse engineering framework and command-line toolset

⭐ Stars: 25.2k  
💻 Language: C  
🔗 [github.com/radareorg/radare2](https://github.com/radareorg/radare2)

### 28. [rizinorg/cutter](https://github.com/rizinorg/cutter)

Free and Open Source Reverse Engineering Platform powered by rizin

⭐ Stars: 20.1k  
💻 Language: C++  
🔗 [github.com/rizinorg/cutter](https://github.com/rizinorg/cutter)

### 29. [semgrep/semgrep](https://github.com/semgrep/semgrep)

Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.

⭐ Stars: 17.4k  
💻 Language: C  
🔗 [github.com/semgrep/semgrep](https://github.com/semgrep/semgrep)

### 30. [shagg88/cogbox](https://github.com/shagg88/cogbox)

This is an open source, all-in-one, static recompilation project that I built from the ground up for the Xbox 360 Gears of War series.

⭐ Stars: 238  
💻 Language: C++  
🔗 [github.com/shagg88/cogbox](https://github.com/shagg88/cogbox)

### 31. [tailscale/tailscale](https://github.com/tailscale/tailscale)

The easiest, most secure way to use WireGuard and 2FA.

⭐ Stars: 38.4k  
💻 Language: Go  
🔗 [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale)

### 32. [theorem-labs/oss-verify-proofs](https://github.com/theorem-labs/oss-verify-proofs)

Theorem statements about OSS-Fuzz fuzz targets as compiled RISC-V binaries, and machine-checked Rocq proofs of them

⭐ Stars: 187  
💻 Language: Rocq Prover  
🔗 [github.com/theorem-labs/oss-verify-proofs](https://github.com/theorem-labs/oss-verify-proofs)

### 33. [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

Find, verify, and analyze leaked credentials

⭐ Stars: 28.8k  
💻 Language: Go  
🔗 [github.com/trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

### 34. [valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp)

Static recompilation of The Legend of Zelda: Tears of the Kingdom to native Windows x86-64, with a Vulkan renderer. Game files not included.

⭐ Stars: 1.5k  
💻 Language: C  
🔗 [github.com/valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp)

### 35. [villagers654/venture](https://github.com/villagers654/venture)

A Meta Quest emulator for PC VR. Play the Quest games you own on Windows and Linux.

⭐ Stars: 197  
💻 Language: C++  
🔗 [github.com/villagers654/venture](https://github.com/villagers654/venture)

### 36. [wireshark/wireshark](https://github.com/wireshark/wireshark)

Read-only mirror of Wireshark's Git repository at https://gitlab.com/wireshark/wireshark. You're welcome to submit pull requests there.

⭐ Stars: 10.1k  
💻 Language: C  
🔗 [github.com/wireshark/wireshark](https://github.com/wireshark/wireshark)

### 37. [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg)

An open-source user mode debugger for Windows. Optimized for reverse engineering and malware analysis.

⭐ Stars: 50.1k  
💻 Language: C++  
🔗 [github.com/x64dbg/x64dbg](https://github.com/x64dbg/x64dbg)


---

## 🧰 Programming languages, compilers, and developer tooling

Programming languages, compilers, and developer tooling.

### 1. [astral-sh/ruff](https://github.com/astral-sh/ruff)

An extremely fast Python linter and code formatter, written in Rust.

⭐ Stars: 50.3k  
💻 Language: Rust  
🔗 [github.com/astral-sh/ruff](https://github.com/astral-sh/ruff)

### 2. [astral-sh/uv](https://github.com/astral-sh/uv)

An extremely fast Python package and project manager, written in Rust.

⭐ Stars: 91.4k  
💻 Language: Rust  
🔗 [github.com/astral-sh/uv](https://github.com/astral-sh/uv)

### 3. [biomejs/biome](https://github.com/biomejs/biome)

A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP.

⭐ Stars: 26k  
💻 Language: Rust  
🔗 [github.com/biomejs/biome](https://github.com/biomejs/biome)

### 4. [bytecodealliance/wasmtime](https://github.com/bytecodealliance/wasmtime)

A lightweight WebAssembly runtime that is fast, secure, and standards-compliant

⭐ Stars: 18.8k  
💻 Language: Rust  
🔗 [github.com/bytecodealliance/wasmtime](https://github.com/bytecodealliance/wasmtime)

### 5. [colinhacks/reylo](https://github.com/colinhacks/reylo)

Import .sql files into TypeScript with full type inference and zero codegen.

⭐ Stars: 1.4k  
💻 Language: Rust  
🔗 [github.com/colinhacks/reylo](https://github.com/colinhacks/reylo)

### 6. [denoland/deno](https://github.com/denoland/deno)

A modern runtime for JavaScript and TypeScript.

⭐ Stars: 108.8k  
💻 Language: Rust  
🔗 [github.com/denoland/deno](https://github.com/denoland/deno)

### 7. [golang/go](https://github.com/golang/go)

The Go programming language

⭐ Stars: 139.5k  
💻 Language: Go  
🔗 [github.com/golang/go](https://github.com/golang/go)

### 8. [jdx/mise](https://github.com/jdx/mise)

dev tools, env vars, task runner

⭐ Stars: 35.6k  
💻 Language: Rust  
🔗 [github.com/jdx/mise](https://github.com/jdx/mise)

### 9. [llvm/llvm-project](https://github.com/llvm/llvm-project)

The LLVM Project is a collection of modular and reusable compiler and toolchain technologies.

⭐ Stars: 41.3k  
💻 Language: LLVM  
🔗 [github.com/llvm/llvm-project](https://github.com/llvm/llvm-project)

### 10. [microsoft/typescript](https://github.com/microsoft/typescript)

TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

⭐ Stars: 111.7k  
💻 Language: Go  
🔗 [github.com/microsoft/typescript](https://github.com/microsoft/typescript)

### 11. [nixos/nixpkgs](https://github.com/nixos/nixpkgs)

Nix Packages collection & NixOS

⭐ Stars: 26.7k  
💻 Language: Nix  
🔗 [github.com/nixos/nixpkgs](https://github.com/nixos/nixpkgs)

### 12. [nodejs/node](https://github.com/nodejs/node)

Node.js JavaScript runtime ✨🐢🚀✨

⭐ Stars: 123.1k  
💻 Language: JavaScript  
🔗 [github.com/nodejs/node](https://github.com/nodejs/node)

### 13. [oven-sh/bun](https://github.com/oven-sh/bun)

Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one

⭐ Stars: 96.5k  
💻 Language: Rust  
🔗 [github.com/oven-sh/bun](https://github.com/oven-sh/bun)

### 14. [python/cpython](https://github.com/python/cpython)

The Python programming language

⭐ Stars: 77.7k  
💻 Language: Python  
🔗 [github.com/python/cpython](https://github.com/python/cpython)

### 15. [rust-lang/rust](https://github.com/rust-lang/rust)

Empowering everyone to build reliable and efficient software.

⭐ Stars: 120.9k  
💻 Language: Rust  
🔗 [github.com/rust-lang/rust](https://github.com/rust-lang/rust)

### 16. [tractordev/webframe](https://github.com/tractordev/webframe)

Run a web page like a program

⭐ Stars: 222  
💻 Language: Go  
🔗 [github.com/tractordev/webframe](https://github.com/tractordev/webframe)

### 17. [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)

An incremental parsing system for programming tools

⭐ Stars: 27.3k  
💻 Language: Rust  
🔗 [github.com/tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)

### 18. [vortexso4/weft](https://github.com/vortexso4/weft)

Voxel sandbox engine in Rust and Vulkan where the base game is itself a mod built only on the public SDK. *(vault note)*

⭐ Stars: 125  
💻 Language: Rust  
🔗 [github.com/vortexso4/weft](https://github.com/vortexso4/weft)

### 19. [webassembly/spec](https://github.com/webassembly/spec)

WebAssembly specification, reference interpreter, and test suite.

⭐ Stars: 3.5k  
💻 Language: WebAssembly  
🔗 [github.com/webassembly/spec](https://github.com/webassembly/spec)

### 20. [ziglang/zig](https://github.com/ziglang/zig)

Moved to Codeberg

⭐ Stars: 43.3k  
💻 Language: Zig  
🔗 [github.com/ziglang/zig](https://github.com/ziglang/zig)


---

## 🌐 Web development and application frameworks

Web development and application frameworks.

### 1. [bigskysoftware/htmx](https://github.com/bigskysoftware/htmx)

\</\> htmx - high power tools for HTML

⭐ Stars: 49.6k  
💻 Language: JavaScript  
🔗 [github.com/bigskysoftware/htmx](https://github.com/bigskysoftware/htmx)

### 2. [django/django](https://github.com/django/django)

The Web framework for perfectionists with deadlines.

⭐ Stars: 91.5k  
💻 Language: Python  
🔗 [github.com/django/django](https://github.com/django/django)

### 3. [electron/electron](https://github.com/electron/electron)

:electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS

⭐ Stars: 123.7k  
💻 Language: C++  
🔗 [github.com/electron/electron](https://github.com/electron/electron)

### 4. [fastapi/fastapi](https://github.com/fastapi/fastapi)

FastAPI framework, high performance, easy to learn, fast to code, ready for production

⭐ Stars: 104.3k  
💻 Language: Python  
🔗 [github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

### 5. [flutter/flutter](https://github.com/flutter/flutter)

Flutter makes it easy and fast to build beautiful apps for mobile and beyond

⭐ Stars: 180.7k  
💻 Language: Dart  
🔗 [github.com/flutter/flutter](https://github.com/flutter/flutter)

### 6. [gohugoio/hugo](https://github.com/gohugoio/hugo)

The world’s fastest framework for building websites.

⭐ Stars: 90.3k  
💻 Language: Go  
🔗 [github.com/gohugoio/hugo](https://github.com/gohugoio/hugo)

### 7. [honojs/hono](https://github.com/honojs/hono)

Web framework built on Web Standards

⭐ Stars: 32.8k  
💻 Language: TypeScript  
🔗 [github.com/honojs/hono](https://github.com/honojs/hono)

### 8. [humpalumps/ultra-water](https://github.com/humpalumps/ultra-water)

Real-time FFT ocean renderer for three.js (WebGL2): shore breakers, foam, caustics, underwater rendering and buoyancy at 200+ fps

⭐ Stars: 436  
💻 Language: JavaScript  
🔗 [github.com/humpalumps/ultra-water](https://github.com/humpalumps/ultra-water)

### 9. [laravel/framework](https://github.com/laravel/framework)

Laravel is a web application framework with expressive, elegant syntax.

⭐ Stars: 35k  
💻 Language: PHP  
🔗 [github.com/laravel/framework](https://github.com/laravel/framework)

### 10. [rails/rails](https://github.com/rails/rails)

Ruby on Rails

⭐ Stars: 58.9k  
💻 Language: Ruby  
🔗 [github.com/rails/rails](https://github.com/rails/rails)

### 11. [react/react](https://github.com/react/react)

The library for web and native user interfaces.

⭐ Stars: 251.8k  
💻 Language: JavaScript  
🔗 [github.com/react/react](https://github.com/react/react)

### 12. [shadcn-ui/ui](https://github.com/shadcn-ui/ui)

Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and mak…

⭐ Stars: 127k  
💻 Language: TypeScript  
🔗 [github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui)

### 13. [sveltejs/svelte](https://github.com/sveltejs/svelte)

web development for the rest of us

⭐ Stars: 88.5k  
💻 Language: JavaScript  
🔗 [github.com/sveltejs/svelte](https://github.com/sveltejs/svelte)

### 14. [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)

A utility-first CSS framework for rapid UI development.

⭐ Stars: 98k  
💻 Language: TypeScript  
🔗 [github.com/tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)

### 15. [tauri-apps/tauri](https://github.com/tauri-apps/tauri)

Build smaller, faster, and more secure desktop and mobile applications with a web frontend.

⭐ Stars: 112.3k  
💻 Language: Rust  
🔗 [github.com/tauri-apps/tauri](https://github.com/tauri-apps/tauri)

### 16. [vercel/ai](https://github.com/vercel/ai)

The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered application…

⭐ Stars: 27.6k  
💻 Language: TypeScript  
🔗 [github.com/vercel/ai](https://github.com/vercel/ai)

### 17. [vercel/next.js](https://github.com/vercel/next.js)

The React Framework

⭐ Stars: 143.2k  
💻 Language: JavaScript  
🔗 [github.com/vercel/next.js](https://github.com/vercel/next.js)

### 18. [vitejs/vite](https://github.com/vitejs/vite)

Next generation frontend tooling. It's fast!

⭐ Stars: 83.6k  
💻 Language: TypeScript  
🔗 [github.com/vitejs/vite](https://github.com/vitejs/vite)

### 19. [vuejs/core](https://github.com/vuejs/core)

🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.

⭐ Stars: 54.8k  
💻 Language: TypeScript  
🔗 [github.com/vuejs/core](https://github.com/vuejs/core)

### 20. [wesbos/3d-model-anything](https://github.com/wesbos/3d-model-anything)

Capture iPhone LiDAR and photos, reconstruct editable Three.js rooms, and explore them in a browser.

⭐ Stars: 2.5k  
💻 Language: Swift  
🔗 [github.com/wesbos/3d-model-anything](https://github.com/wesbos/3d-model-anything)

### 21. [wevm/ondine](https://github.com/wevm/ondine)

Fast and simple diagrams.

⭐ Stars: 439  
💻 Language: Rust  
🔗 [github.com/wevm/ondine](https://github.com/wevm/ondine)

### 22. [withastro/astro](https://github.com/withastro/astro)

The web framework for content-driven websites.

⭐ Stars: 63.6k  
💻 Language: TypeScript  
🔗 [github.com/withastro/astro](https://github.com/withastro/astro)


---

## 🏠 Self-hosted applications and infrastructure

Self-hosted applications and infrastructure you can run yourself.

### 1. [adguardteam/adguardhome](https://github.com/adguardteam/adguardhome)

Network-wide ads & trackers blocking DNS server

⭐ Stars: 38k  
💻 Language: TypeScript  
🔗 [github.com/adguardteam/adguardhome](https://github.com/adguardteam/adguardhome)

### 2. [caddyserver/caddy](https://github.com/caddyserver/caddy)

Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

⭐ Stars: 78.6k  
💻 Language: Go  
🔗 [github.com/caddyserver/caddy](https://github.com/caddyserver/caddy)

### 3. [coollabsio/coolify](https://github.com/coollabsio/coolify)

An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stac…

⭐ Stars: 65.3k  
💻 Language: PHP  
🔗 [github.com/coollabsio/coolify](https://github.com/coollabsio/coolify)

### 4. [dokku/dokku](https://github.com/dokku/dokku)

A docker-powered PaaS that helps you build and manage the lifecycle of applications

⭐ Stars: 32.2k  
💻 Language: Go  
🔗 [github.com/dokku/dokku](https://github.com/dokku/dokku)

### 5. [freshrss/freshrss](https://github.com/freshrss/freshrss)

A free, self-hostable news aggregator…

⭐ Stars: 16.5k  
💻 Language: PHP  
🔗 [github.com/freshrss/freshrss](https://github.com/freshrss/freshrss)

### 6. [goauthentik/authentik](https://github.com/goauthentik/authentik)

The authentication glue you need.

⭐ Stars: 26.2k  
💻 Language: Python  
🔗 [github.com/goauthentik/authentik](https://github.com/goauthentik/authentik)

### 7. [immich-app/immich](https://github.com/immich-app/immich)

High performance self-hosted photo and video management solution.

⭐ Stars: 117.7k  
💻 Language: TypeScript  
🔗 [github.com/immich-app/immich](https://github.com/immich-app/immich)

### 8. [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)

The Free Software Media System - Server Backend & API

⭐ Stars: 58.8k  
💻 Language: C#  
🔗 [github.com/jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)

### 9. [k3s-io/k3s](https://github.com/k3s-io/k3s)

Lightweight Kubernetes

⭐ Stars: 34.3k  
💻 Language: Go  
🔗 [github.com/k3s-io/k3s](https://github.com/k3s-io/k3s)

### 10. [keycloak/keycloak](https://github.com/keycloak/keycloak)

Open Source Identity and Access Management For Modern Applications and Services

⭐ Stars: 37.6k  
💻 Language: Java  
🔗 [github.com/keycloak/keycloak](https://github.com/keycloak/keycloak)

### 11. [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)

Production-Grade Container Scheduling and Management

⭐ Stars: 128.5k  
💻 Language: Go  
🔗 [github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)

### 12. [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)

A fancy self-hosted monitoring tool

⭐ Stars: 93.1k  
💻 Language: JavaScript  
🔗 [github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)

### 13. [miniflux/v2](https://github.com/miniflux/v2)

Minimalist and opinionated feed reader

⭐ Stars: 9.9k  
💻 Language: Go  
🔗 [github.com/miniflux/v2](https://github.com/miniflux/v2)

### 14. [nextcloud/server](https://github.com/nextcloud/server)

☁️ Nextcloud server, a safe home for all your data

⭐ Stars: 37.4k  
💻 Language: PHP  
🔗 [github.com/nextcloud/server](https://github.com/nextcloud/server)

### 15. [nginx/nginx](https://github.com/nginx/nginx)

The official NGINX Open Source repository.

⭐ Stars: 32k  
💻 Language: C  
🔗 [github.com/nginx/nginx](https://github.com/nginx/nginx)

### 16. [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)

Add AirPrint / AirScan support to your old printer, using just a cheap ESP32-S3

⭐ Stars: 210  
💻 Language: C  
🔗 [github.com/ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)

### 17. [opentofu/opentofu](https://github.com/opentofu/opentofu)

OpenTofu lets you declaratively manage your cloud infrastructure.

⭐ Stars: 30.7k  
💻 Language: Go  
🔗 [github.com/opentofu/opentofu](https://github.com/opentofu/opentofu)

### 18. [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

A community-supported supercharged document management system: scan, index and archive all your documents

⭐ Stars: 47.4k  
💻 Language: Python  
🔗 [github.com/paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

### 19. [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole)

A black hole for Internet advertisements

⭐ Stars: 61.6k  
💻 Language: Shell  
🔗 [github.com/pi-hole/pi-hole](https://github.com/pi-hole/pi-hole)

### 20. [portainer/portainer](https://github.com/portainer/portainer)

Making Docker and Kubernetes management easy.

⭐ Stars: 38.8k  
💻 Language: TypeScript  
🔗 [github.com/portainer/portainer](https://github.com/portainer/portainer)

### 21. [rolottr/bambu-bar](https://github.com/rolottr/bambu-bar)

Native macOS menu bar app for Bambu Lab 3D printers. Live progress, time left, temperatures, AMS spools and errors, print controls, sever…

⭐ Stars: 147  
💻 Language: Swift  
🔗 [github.com/rolottr/bambu-bar](https://github.com/rolottr/bambu-bar)

### 22. [traefik/traefik](https://github.com/traefik/traefik)

The Cloud Native Application Proxy

⭐ Stars: 65.4k  
💻 Language: Go  
🔗 [github.com/traefik/traefik](https://github.com/traefik/traefik)


---

## 🔍 Observability, testing, and debugging

Observability, testing, and debugging tools.

### 1. [arize-ai/phoenix](https://github.com/arize-ai/phoenix)

AI Observability & Evaluation

⭐ Stars: 12.1k  
💻 Language: Python  
🔗 [github.com/arize-ai/phoenix](https://github.com/arize-ai/phoenix)

### 2. [brendangregg/flamegraph](https://github.com/brendangregg/flamegraph)

Stack trace visualizer

⭐ Stars: 19.8k  
💻 Language: Perl  
🔗 [github.com/brendangregg/flamegraph](https://github.com/brendangregg/flamegraph)

### 3. [confident-ai/deepeval](https://github.com/confident-ai/deepeval)

The LLM Evaluation Framework

⭐ Stars: 19.2k  
💻 Language: Python  
🔗 [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval)

### 4. [getsentry/sentry](https://github.com/getsentry/sentry)

Developer-first error tracking and performance monitoring

⭐ Stars: 45.7k  
💻 Language: Python  
🔗 [github.com/getsentry/sentry](https://github.com/getsentry/sentry)

### 5. [grafana/grafana](https://github.com/grafana/grafana)

The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Pro…

⭐ Stars: 77.6k  
💻 Language: TypeScript  
🔗 [github.com/grafana/grafana](https://github.com/grafana/grafana)

### 6. [grafana/k6](https://github.com/grafana/k6)

A modern load testing tool, using Go and JavaScript

⭐ Stars: 32.1k  
💻 Language: Go  
🔗 [github.com/grafana/k6](https://github.com/grafana/k6)

### 7. [grafana/loki](https://github.com/grafana/loki)

Like Prometheus, but for logs.

⭐ Stars: 29.1k  
💻 Language: Go  
🔗 [github.com/grafana/loki](https://github.com/grafana/loki)

### 8. [iovisor/bcc](https://github.com/iovisor/bcc)

BCC - Tools for BPF-based Linux IO analysis, networking, monitoring, and more

⭐ Stars: 22.7k  
💻 Language: C  
🔗 [github.com/iovisor/bcc](https://github.com/iovisor/bcc)

### 9. [jaegertracing/jaeger](https://github.com/jaegertracing/jaeger)

CNCF Jaeger, a Distributed Tracing Platform

⭐ Stars: 23.4k  
💻 Language: Go  
🔗 [github.com/jaegertracing/jaeger](https://github.com/jaegertracing/jaeger)

### 10. [langfuse/langfuse](https://github.com/langfuse/langfuse)

🪢 Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform.

⭐ Stars: 36.8k  
💻 Language: TypeScript  
🔗 [github.com/langfuse/langfuse](https://github.com/langfuse/langfuse)

### 11. [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)

OpenTelemetry Collector

⭐ Stars: 7.7k  
💻 Language: Go  
🔗 [github.com/open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)

### 12. [prometheus/prometheus](https://github.com/prometheus/prometheus)

The Prometheus monitoring system and time series database.

⭐ Stars: 66.9k  
💻 Language: Go  
🔗 [github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)

### 13. [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, De…

⭐ Stars: 26.7k  
💻 Language: TypeScript  
🔗 [github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

### 14. [pytest-dev/pytest](https://github.com/pytest-dev/pytest)

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing

⭐ Stars: 14.7k  
💻 Language: Python  
🔗 [github.com/pytest-dev/pytest](https://github.com/pytest-dev/pytest)

### 15. [rr-debugger/rr](https://github.com/rr-debugger/rr)

Record and Replay Framework

⭐ Stars: 10.7k  
💻 Language: C++  
🔗 [github.com/rr-debugger/rr](https://github.com/rr-debugger/rr)

### 16. [signoz/signoz](https://github.com/signoz/signoz)

SigNoz is an open-source, OpenTelemetry-native observability platform for your team and their AI agents. Get logs, metrics, and traces in…

⭐ Stars: 32.5k  
💻 Language: TypeScript  
🔗 [github.com/signoz/signoz](https://github.com/signoz/signoz)

### 17. [victoriametrics/victoriametrics](https://github.com/victoriametrics/victoriametrics)

VictoriaMetrics: fast, cost-effective monitoring solution and time series database

⭐ Stars: 18k  
💻 Language: Go  
🔗 [github.com/victoriametrics/victoriametrics](https://github.com/victoriametrics/victoriametrics)

### 18. [vitest-dev/vitest](https://github.com/vitest-dev/vitest)

Next generation testing framework powered by Vite.

⭐ Stars: 17.3k  
💻 Language: TypeScript  
🔗 [github.com/vitest-dev/vitest](https://github.com/vitest-dev/vitest)

### 19. [winnin/farol](https://github.com/winnin/farol)

Know the risk of merging a pull request, and where it lives. Free, open-source CLI and GitHub Action: after your AI review, farol shows t…

⭐ Stars: 169  
💻 Language: TypeScript  
🔗 [github.com/winnin/farol](https://github.com/winnin/farol)


---

## 📊 Data engineering and analytics

Data engineering, pipelines, and analytics.

### 1. [airbytehq/airbyte](https://github.com/airbytehq/airbyte)

Open-source data movement for ELT pipelines and AI agents — from APIs, databases & files to warehouses, lakes, and AI applications. Both…

⭐ Stars: 22.3k  
💻 Language: Python  
🔗 [github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)

### 2. [apache/arrow](https://github.com/apache/arrow)

Apache Arrow is the universal columnar format and multi-language toolbox for fast data interchange and in-memory analytics

⭐ Stars: 17.3k  
💻 Language: C++  
🔗 [github.com/apache/arrow](https://github.com/apache/arrow)

### 3. [apache/iceberg](https://github.com/apache/iceberg)

Apache Iceberg

⭐ Stars: 9.4k  
💻 Language: Java  
🔗 [github.com/apache/iceberg](https://github.com/apache/iceberg)

### 4. [apache/spark](https://github.com/apache/spark)

Apache Spark - A unified analytics engine for large-scale data processing

⭐ Stars: 44.4k  
💻 Language: Scala  
🔗 [github.com/apache/spark](https://github.com/apache/spark)

### 5. [apache/superset](https://github.com/apache/superset)

Apache Superset is a Data Visualization and Data Exploration Platform

⭐ Stars: 75.4k  
💻 Language: Python  
🔗 [github.com/apache/superset](https://github.com/apache/superset)

### 6. [dagster-io/dagster](https://github.com/dagster-io/dagster)

An orchestration platform for the development, production, and observation of data assets.

⭐ Stars: 16.4k  
💻 Language: Python  
🔗 [github.com/dagster-io/dagster](https://github.com/dagster-io/dagster)

### 7. [dbt-labs/dbt](https://github.com/dbt-labs/dbt)

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

⭐ Stars: 14.1k  
💻 Language: Rust  
🔗 [github.com/dbt-labs/dbt](https://github.com/dbt-labs/dbt)

### 8. [delta-io/delta](https://github.com/delta-io/delta)

An open-source storage framework that enables building a Lakehouse architecture with compute engines including Spark, PrestoDB, Flink, Tr…

⭐ Stars: 9.1k  
💻 Language: Scala  
🔗 [github.com/delta-io/delta](https://github.com/delta-io/delta)

### 9. [dlt-hub/dlt](https://github.com/dlt-hub/dlt)

data load tool (dlt) is an open source Python library that makes data loading easy 🛠️

⭐ Stars: 6k  
💻 Language: Python  
🔗 [github.com/dlt-hub/dlt](https://github.com/dlt-hub/dlt)

### 10. [evidence-dev/evidence](https://github.com/evidence-dev/evidence)

Business intelligence as code: build fast, interactive data visualizations in SQL and markdown

⭐ Stars: 7.1k  
💻 Language: TypeScript  
🔗 [github.com/evidence-dev/evidence](https://github.com/evidence-dev/evidence)

### 11. [fivetran/great_expectations](https://github.com/fivetran/great_expectations)

Always know what to expect from your data.

⭐ Stars: 11.9k  
💻 Language: Python  
🔗 [github.com/fivetran/great_expectations](https://github.com/fivetran/great_expectations)

### 12. [hugues31/duckpad](https://github.com/hugues31/duckpad)

The data transformation tool the open-source community deserves.

⭐ Stars: 275  
💻 Language: Python  
🔗 [github.com/hugues31/duckpad](https://github.com/hugues31/duckpad)

### 13. [jupyter/notebook](https://github.com/jupyter/notebook)

Jupyter Interactive Notebook

⭐ Stars: 13.5k  
💻 Language: Jupyter Notebook  
🔗 [github.com/jupyter/notebook](https://github.com/jupyter/notebook)

### 14. [marimo-team/marimo](https://github.com/marimo-team/marimo)

A reactive notebook for Python — run reproducible experiments, query with SQL, execute as a script, deploy as an app, and version with gi…

⭐ Stars: 23.4k  
💻 Language: Python  
🔗 [github.com/marimo-team/marimo](https://github.com/marimo-team/marimo)

### 15. [metabase/metabase](https://github.com/metabase/metabase)

The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data :bar\_chart:

⭐ Stars: 50k  
💻 Language: Clojure  
🔗 [github.com/metabase/metabase](https://github.com/metabase/metabase)

### 16. [pandas-dev/pandas](https://github.com/pandas-dev/pandas)

Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects,…

⭐ Stars: 50.3k  
💻 Language: Python  
🔗 [github.com/pandas-dev/pandas](https://github.com/pandas-dev/pandas)

### 17. [pola-rs/polars](https://github.com/pola-rs/polars)

Extremely fast Query Engine for DataFrames, written in Rust

⭐ Stars: 40.2k  
💻 Language: Rust  
🔗 [github.com/pola-rs/polars](https://github.com/pola-rs/polars)

### 18. [streamlit/streamlit](https://github.com/streamlit/streamlit)

Streamlit — A faster way to build and share data apps.

⭐ Stars: 46.2k  
💻 Language: Python  
🔗 [github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)

### 19. [surendrapandar/minilytics](https://github.com/surendrapandar/minilytics)

Opensource Revenue-first analytics for indie hackers & solo founders

⭐ Stars: 784  
💻 Language: TypeScript  
🔗 [github.com/surendrapandar/minilytics](https://github.com/surendrapandar/minilytics)


---

## 🎓 Research tools, documentation, and learning resources

Research tools, documentation, and learning resources.

### 1. [archivebox/archivebox](https://github.com/archivebox/archivebox)

🗃 Open source self-hosted web archiving. Takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more...

⭐ Stars: 28.9k  
💻 Language: Python  
🔗 [github.com/archivebox/archivebox](https://github.com/archivebox/archivebox)

### 2. [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)

An autonomous agent that conducts deep research on any data using any LLM providers

⭐ Stars: 30.4k  
💻 Language: Python  
🔗 [github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)

### 3. [axiommath/cfsg](https://github.com/axiommath/cfsg)

A Lean formalization of the Classification of Finite Simple Groups

⭐ Stars: 146  
💻 Language: Lean  
🔗 [github.com/axiommath/cfsg](https://github.com/axiommath/cfsg)

### 4. [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards.

⭐ Stars: 376.3k  
💻 Language: Python  
🔗 [github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

### 5. [meta/docusaurus](https://github.com/meta/docusaurus)

Easy to maintain open source documentation websites. *(renamed from facebook/docusaurus)*

⭐ Stars: 66.6k  
💻 Language: TypeScript  
🔗 [github.com/meta/docusaurus](https://github.com/meta/docusaurus)

### 6. [freecodecamp/freecodecamp](https://github.com/freecodecamp/freecodecamp)

freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

⭐ Stars: 458.2k  
💻 Language: TypeScript  
🔗 [github.com/freecodecamp/freecodecamp](https://github.com/freecodecamp/freecodecamp)

### 7. [gildas-lormeau/singlefile](https://github.com/gildas-lormeau/singlefile)

Web Extension for saving a faithful copy of a complete web page in a single HTML file

⭐ Stars: 22.8k  
💻 Language: JavaScript  
🔗 [github.com/gildas-lormeau/singlefile](https://github.com/gildas-lormeau/singlefile)

### 8. [ivarvong/lantern](https://github.com/ivarvong/lantern)

Animated, steppable code explainers. Zero-dependency TypeScript, SVG output, browser and Cloudflare Workers.

⭐ Stars: 244  
💻 Language: TypeScript  
🔗 [github.com/ivarvong/lantern](https://github.com/ivarvong/lantern)

### 9. [jgm/pandoc](https://github.com/jgm/pandoc)

Universal markup converter

⭐ Stars: 46.8k  
💻 Language: Haskell  
🔗 [github.com/jgm/pandoc](https://github.com/jgm/pandoc)

### 10. [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university)

A complete computer science study plan to become a software engineer.

⭐ Stars: 363.6k  
💻 Language: Unknown  
🔗 [github.com/jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university)

### 11. [karpathy/nanogpt](https://github.com/karpathy/nanogpt)

The simplest, fastest repository for training/finetuning medium-sized GPTs.

⭐ Stars: 64.3k  
💻 Language: Python  
🔗 [github.com/karpathy/nanogpt](https://github.com/karpathy/nanogpt)

### 12. [mkdocs/mkdocs](https://github.com/mkdocs/mkdocs)

Project documentation with Markdown.

⭐ Stars: 22.5k  
💻 Language: Python  
🔗 [github.com/mkdocs/mkdocs](https://github.com/mkdocs/mkdocs)

### 13. [ossu/computer-science](https://github.com/ossu/computer-science)

🎓 Path to a free self-taught education in Computer Science!

⭐ Stars: 210.5k  
💻 Language: HTML  
🔗 [github.com/ossu/computer-science](https://github.com/ossu/computer-science)

### 14. [public-apis/public-apis](https://github.com/public-apis/public-apis)

A collective list of free APIs

⭐ Stars: 493.6k  
💻 Language: Python  
🔗 [github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)

### 15. [rasbt/llms-from-scratch](https://github.com/rasbt/llms-from-scratch)

Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

⭐ Stars: 107.6k  
💻 Language: Jupyter Notebook  
🔗 [github.com/rasbt/llms-from-scratch](https://github.com/rasbt/llms-from-scratch)

### 16. [rust-lang/mdbook](https://github.com/rust-lang/mdbook)

Create book from markdown files. Like Gitbook but implemented in Rust

⭐ Stars: 22.3k  
💻 Language: Rust  
🔗 [github.com/rust-lang/mdbook](https://github.com/rust-lang/mdbook)

### 17. [sindresorhus/awesome](https://github.com/sindresorhus/awesome)

😎 Awesome lists about all kinds of interesting topics \[NOTE: Pull requests are temporarily disabled until I have a chance to catch up wit…

⭐ Stars: 527.5k  
💻 Language: Unknown  
🔗 [github.com/sindresorhus/awesome](https://github.com/sindresorhus/awesome)

### 18. [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)

Documentation that simply works

⭐ Stars: 27.6k  
💻 Language: Python  
🔗 [github.com/squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)

### 19. [stanford-oval/storm](https://github.com/stanford-oval/storm)

An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations.

⭐ Stars: 31.8k  
💻 Language: Python  
🔗 [github.com/stanford-oval/storm](https://github.com/stanford-oval/storm)

### 20. [tldr-pages/tldr](https://github.com/tldr-pages/tldr)

Collaborative cheatsheets for console commands 📚.

⭐ Stars: 64.1k  
💻 Language: Markdown  
🔗 [github.com/tldr-pages/tldr](https://github.com/tldr-pages/tldr)

### 21. [typst/typst](https://github.com/typst/typst)

A markup-based typesetting system that is powerful and easy to learn.

⭐ Stars: 56.9k  
💻 Language: Rust  
🔗 [github.com/typst/typst](https://github.com/typst/typst)

### 22. [zotero/zotero](https://github.com/zotero/zotero)

Zotero is a free, easy-to-use tool to help you collect, organize, annotate, cite, and share your research sources.

⭐ Stars: 15.8k  
💻 Language: JavaScript  
🔗 [github.com/zotero/zotero](https://github.com/zotero/zotero)


---

## 🐚 Useful command-line tools and small utilities

Handy command-line tools and small utilities.

### 1. [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)

A smarter cd command. Supports all major shells.

⭐ Stars: 40.4k  
💻 Language: Rust  
🔗 [github.com/ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)

### 2. [anomalyco/hokum](https://github.com/anomalyco/hokum)

Notifications for Wayland that look like they belong on a computer from this decade. Drawn with Rune.

⭐ Stars: 214  
💻 Language: Rust  
🔗 [github.com/anomalyco/hokum](https://github.com/anomalyco/hokum)

### 3. [aristocratos/btop](https://github.com/aristocratos/btop)

A monitor of resources

⭐ Stars: 35.2k  
💻 Language: C++  
🔗 [github.com/aristocratos/btop](https://github.com/aristocratos/btop)

### 4. [atuinsh/atuin](https://github.com/atuinsh/atuin)

✨ Making your shell magical

⭐ Stars: 32.2k  
💻 Language: Rust  
🔗 [github.com/atuinsh/atuin](https://github.com/atuinsh/atuin)

### 5. [burntsushi/ripgrep](https://github.com/burntsushi/ripgrep)

ripgrep recursively searches directories for a regex pattern while respecting your gitignore

⭐ Stars: 69.6k  
💻 Language: Rust  
🔗 [github.com/burntsushi/ripgrep](https://github.com/burntsushi/ripgrep)

### 6. [charmbracelet/gum](https://github.com/charmbracelet/gum)

A tool for glamorous shell scripts 🎀

⭐ Stars: 24.6k  
💻 Language: Go  
🔗 [github.com/charmbracelet/gum](https://github.com/charmbracelet/gum)

### 7. [clementtsang/bottom](https://github.com/clementtsang/bottom)

Yet another cross-platform graphical process/system monitor.

⭐ Stars: 14.1k  
💻 Language: Rust  
🔗 [github.com/clementtsang/bottom](https://github.com/clementtsang/bottom)

### 8. [eza-community/eza](https://github.com/eza-community/eza)

A modern alternative to ls

⭐ Stars: 23.7k  
💻 Language: Rust  
🔗 [github.com/eza-community/eza](https://github.com/eza-community/eza)

### 9. [ffmpeg/ffmpeg](https://github.com/ffmpeg/ffmpeg)

Mirror of https://git.ffmpeg.org/ffmpeg.git

⭐ Stars: 66.1k  
💻 Language: C  
🔗 [github.com/ffmpeg/ffmpeg](https://github.com/ffmpeg/ffmpeg)

### 10. [heydeer/pngdeer](https://github.com/heydeer/pngdeer)

Smaller images, same picture. Compress PNGs to PNG or WebP with automatic quality. PNG output is 8–12% smaller than TinyPNG at equal qual…

⭐ Stars: 386  
💻 Language: Rust  
🔗 [github.com/heydeer/pngdeer](https://github.com/heydeer/pngdeer)

### 11. [htop-dev/htop](https://github.com/htop-dev/htop)

htop - an interactive process viewer

⭐ Stars: 8.4k  
💻 Language: C  
🔗 [github.com/htop-dev/htop](https://github.com/htop-dev/htop)

### 12. [hugo-dz/spritefusion-sprite-normals](https://github.com/hugo-dz/spritefusion-sprite-normals)

A tool to generate normal maps from any sprite and animated sprite sheet.

⭐ Stars: 711  
💻 Language: Rust  
🔗 [github.com/hugo-dz/spritefusion-sprite-normals](https://github.com/hugo-dz/spritefusion-sprite-normals)

### 13. [imagemagick/imagemagick](https://github.com/imagemagick/imagemagick)

ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and…

⭐ Stars: 17.8k  
💻 Language: C  
🔗 [github.com/imagemagick/imagemagick](https://github.com/imagemagick/imagemagick)

### 14. [johncassil/dontallow](https://github.com/johncassil/dontallow)

Auto-dismiss the macOS 'Allow X to find devices on local networks?' prompt. Presses Don't Allow for you, zero CPU idle, survives reboots.

⭐ Stars: 89  
💻 Language: Swift  
🔗 [github.com/johncassil/dontallow](https://github.com/johncassil/dontallow)

### 15. [jqlang/jq](https://github.com/jqlang/jq)

Command-line JSON processor

⭐ Stars: 36k  
💻 Language: C  
🔗 [github.com/jqlang/jq](https://github.com/jqlang/jq)

### 16. [junegunn/fzf](https://github.com/junegunn/fzf)

:cherry\_blossom: A command-line fuzzy finder

⭐ Stars: 83.9k  
💻 Language: Go  
🔗 [github.com/junegunn/fzf](https://github.com/junegunn/fzf)

### 17. [koalaman/shellcheck](https://github.com/koalaman/shellcheck)

ShellCheck, a static analysis tool for shell scripts

⭐ Stars: 40.3k  
💻 Language: Haskell  
🔗 [github.com/koalaman/shellcheck](https://github.com/koalaman/shellcheck)

### 18. [lonthq/overtone-captions](https://github.com/lonthq/overtone-captions)

Captions cut for every screen shape, from one file. A caption format, a video.js plugin, and a CLI that turns audio into word-timed capti…

⭐ Stars: 46  
💻 Language: TypeScript  
🔗 [github.com/lonthq/overtone-captions](https://github.com/lonthq/overtone-captions)

### 19. [mikefarah/yq](https://github.com/mikefarah/yq)

yq is a portable command-line YAML, JSON, XML, CSV, TOML, HCL and properties processor

⭐ Stars: 16.2k  
💻 Language: Go  
🔗 [github.com/mikefarah/yq](https://github.com/mikefarah/yq)

### 20. [obsproject/obs-studio](https://github.com/obsproject/obs-studio)

OBS Studio - Free and open source software for live streaming and screen recording

⭐ Stars: 78.6k  
💻 Language: C  
🔗 [github.com/obsproject/obs-studio](https://github.com/obsproject/obs-studio)

### 21. [sharkdp/bat](https://github.com/sharkdp/bat)

A cat(1) clone with wings.

⭐ Stars: 61k  
💻 Language: Rust  
🔗 [github.com/sharkdp/bat](https://github.com/sharkdp/bat)

### 22. [sharkdp/fd](https://github.com/sharkdp/fd)

A simple, fast and user-friendly alternative to 'find'

⭐ Stars: 44.9k  
💻 Language: Rust  
🔗 [github.com/sharkdp/fd](https://github.com/sharkdp/fd)

### 23. [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine)

A command-line benchmarking tool

⭐ Stars: 29.2k  
💻 Language: Rust  
🔗 [github.com/sharkdp/hyperfine](https://github.com/sharkdp/hyperfine)

### 24. [starship/starship](https://github.com/starship/starship)

☄🌌️ The minimal, blazing-fast, and infinitely customizable prompt for any shell!

⭐ Stars: 60.5k  
💻 Language: Rust  
🔗 [github.com/starship/starship](https://github.com/starship/starship)

### 25. [tealdeer-rs/tealdeer](https://github.com/tealdeer-rs/tealdeer)

A very fast implementation of tldr in Rust.

⭐ Stars: 6.6k  
💻 Language: Rust  
🔗 [github.com/tealdeer-rs/tealdeer](https://github.com/tealdeer-rs/tealdeer)

### 26. [tmux/tmux](https://github.com/tmux/tmux)

tmux source code

⭐ Stars: 50.1k  
💻 Language: C  
🔗 [github.com/tmux/tmux](https://github.com/tmux/tmux)

### 27. [xampprocky/tokei](https://github.com/xampprocky/tokei)

Count your code, quickly.

⭐ Stars: 15k  
💻 Language: Rust  
🔗 [github.com/xampprocky/tokei](https://github.com/xampprocky/tokei)

### 28. [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

A feature-rich command-line audio/video downloader

⭐ Stars: 204k  
💻 Language: Python  
🔗 [github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

### 29. [zellij-org/zellij](https://github.com/zellij-org/zellij)

A terminal workspace with batteries included

⭐ Stars: 35.9k  
💻 Language: Rust  
🔗 [github.com/zellij-org/zellij](https://github.com/zellij-org/zellij)


---

## 🗽 Digital independence and long-term personal infrastructure

Projects for digital independence and long-term personal infrastructure.

### 1. [anonaddy/anonaddy](https://github.com/anonaddy/anonaddy)

Anonymous email forwarding

⭐ Stars: 4.9k  
💻 Language: PHP  
🔗 [github.com/anonaddy/anonaddy](https://github.com/anonaddy/anonaddy)

### 2. [appflowy-io/appflowy](https://github.com/appflowy-io/appflowy)

Bring projects, wikis, and teams together with AI. AppFlowy is the AI collaborative workspace where you achieve more without losing contr…

⭐ Stars: 78k  
💻 Language: Dart  
🔗 [github.com/appflowy-io/appflowy](https://github.com/appflowy-io/appflowy)

### 3. [beemdevelopment/aegis](https://github.com/beemdevelopment/aegis)

A free, secure and open source app for Android to manage your 2-step verification tokens.

⭐ Stars: 13.4k  
💻 Language: Java  
🔗 [github.com/beemdevelopment/aegis](https://github.com/beemdevelopment/aegis)

### 4. [element-hq/synapse](https://github.com/element-hq/synapse)

Synapse: Matrix homeserver written in Python/Twisted + Rust

⭐ Stars: 4.7k  
💻 Language: Python  
🔗 [github.com/element-hq/synapse](https://github.com/element-hq/synapse)

### 5. [ely-open-source/elyoffice](https://github.com/ely-open-source/elyoffice)

Ely Office: offline-first desktop apps in Rust and GPUI

⭐ Stars: 1.1k  
💻 Language: Rust  
🔗 [github.com/ely-open-source/elyoffice](https://github.com/ely-open-source/elyoffice)

### 6. [ente/ente](https://github.com/ente/ente)

💚 End-to-end encrypted cloud for everything.

⭐ Stars: 29.8k  
💻 Language: Dart  
🔗 [github.com/ente/ente](https://github.com/ente/ente)

### 7. [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools)

Command line Kiwix tools: kiwix-serve, kiwix-manage, ...

⭐ Stars: 976  
💻 Language: C++  
🔗 [github.com/kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools)

### 8. [kovidgoyal/calibre](https://github.com/kovidgoyal/calibre)

The official source code repository for the calibre ebook manager

⭐ Stars: 26.3k  
💻 Language: Python  
🔗 [github.com/kovidgoyal/calibre](https://github.com/kovidgoyal/calibre)

### 9. [laurent22/joplin](https://github.com/laurent22/joplin)

Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS.

⭐ Stars: 57k  
💻 Language: TypeScript  
🔗 [github.com/laurent22/joplin](https://github.com/laurent22/joplin)

### 10. [lemmynet/lemmy](https://github.com/lemmynet/lemmy)

🐀 A decentralised discussion platform for communities.

⭐ Stars: 14.7k  
💻 Language: Rust  
🔗 [github.com/lemmynet/lemmy](https://github.com/lemmynet/lemmy)

### 11. [mastodon/mastodon](https://github.com/mastodon/mastodon)

Your self-hosted, globally interconnected microblogging community

⭐ Stars: 50.5k  
💻 Language: Ruby  
🔗 [github.com/mastodon/mastodon](https://github.com/mastodon/mastodon)

### 12. [mirkobrombin/raven](https://github.com/mirkobrombin/raven)

A Windows your apps recognize.

⭐ Stars: 565  
💻 Language: C++  
🔗 [github.com/mirkobrombin/raven](https://github.com/mirkobrombin/raven)

### 13. [mozilla/gecko-dev](https://github.com/mozilla/gecko-dev)

SUPERSEDED by https://github.com/mozilla-firefox/firefox. Read-only Git mirror of the Mercurial gecko repositories at https://hg.mozilla.org *(archived)*

⭐ Stars: 3.7k  
💻 Language: JavaScript  
🔗 [github.com/mozilla/gecko-dev](https://github.com/mozilla/gecko-dev)

### 14. [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps)

🍃 Organic Maps is a free Android & iOS offline maps app for more than 6M travelers, tourists, hikers, and cyclists. It uses crowd-sourced…

⭐ Stars: 15.8k  
💻 Language: C++  
🔗 [github.com/organicmaps/organicmaps](https://github.com/organicmaps/organicmaps)

### 15. [osmandapp/osmand](https://github.com/osmandapp/osmand)

OsmAnd

⭐ Stars: 6.1k  
💻 Language: Java  
🔗 [github.com/osmandapp/osmand](https://github.com/osmandapp/osmand)

### 16. [signalapp/signal-android](https://github.com/signalapp/signal-android)

A private messenger for Android.

⭐ Stars: 29.6k  
💻 Language: Kotlin  
🔗 [github.com/signalapp/signal-android](https://github.com/signalapp/signal-android)

### 17. [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv)

A fast, ad-free home screen for Google TV, LG webOS and Samsung Tizen. One button to undo.

⭐ Stars: 5.5k  
💻 Language: Java  
🔗 [github.com/simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv)

### 18. [simple-login/app](https://github.com/simple-login/app)

The SimpleLogin back-end and web app

⭐ Stars: 7.1k  
💻 Language: Python  
🔗 [github.com/simple-login/app](https://github.com/simple-login/app)

### 19. [standardnotes/app](https://github.com/standardnotes/app)

Think fearlessly with end-to-end encrypted notes and files. For issues, visit https://standardnotes.com/forum or https://standardnotes.co…

⭐ Stars: 6.7k  
💻 Language: TypeScript  
🔗 [github.com/standardnotes/app](https://github.com/standardnotes/app)

### 20. [thunderbird/thunderbird-android](https://github.com/thunderbird/thunderbird-android)

Thunderbird for Android – Open Source Email App for Android (fka K-9 Mail)

⭐ Stars: 14.2k  
💻 Language: Kotlin  
🔗 [github.com/thunderbird/thunderbird-android](https://github.com/thunderbird/thunderbird-android)

### 21. [toeverything/affine](https://github.com/toeverything/affine)

There can be more than Notion and Miro. AFFiNE(pronounced \[ə‘fain\]) is a next-gen knowledge base that brings planning, sorting and creati…

⭐ Stars: 74k  
💻 Language: TypeScript  
🔗 [github.com/toeverything/affine](https://github.com/toeverything/affine)

### 22. [tutao/tutanota](https://github.com/tutao/tutanota)

Tuta is an email service with a strong focus on security and privacy that lets you encrypt emails, contacts and calendar entries on all y…

⭐ Stars: 8.1k  
💻 Language: TypeScript  
🔗 [github.com/tutao/tutanota](https://github.com/tutao/tutanota)

### 23. [twofas/2fas-android](https://github.com/twofas/2fas-android)

Source code for 2FAS Auth Android app

⭐ Stars: 1.6k  
💻 Language: Kotlin  
🔗 [github.com/twofas/2fas-android](https://github.com/twofas/2fas-android)

---

## 🤝 Contributing

Know a useful open-source project that belongs here? See [CONTRIBUTING.md](CONTRIBUTING.md) for how to suggest a repository.
