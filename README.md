# LLM-Powered Prompt Router

## Overview & System Design
This application implements an intent-based routing system for Large Language Models (LLMs). Instead of relying on a single, generic prompt to handle all user requests, this service uses a two-step "Classify, then Respond" architecture to deliver highly specialized, context-aware answers.

1. **Classifier Agent:** A lightweight, low-temperature LLM call analyzes the incoming user message and outputs a strict JSON object categorizing the intent (`code`, `data`, `writing`, `career`, or `unclear`) along with a confidence score.
2. **Expert Router:** Based on the classified intent, the system dynamically selects a specialized system prompt (Persona) from a configuration dictionary. 
3. **Generator Agent:** A second LLM call is made using the specialized system prompt and the user's message to generate the final response. 

If the intent is detected as `unclear` or the classifier fails to return valid JSON, the system gracefully falls back to a clarification protocol, asking the user to specify their domain rather than guessing.

## Prerequisites
* Python 3.12+
* Docker & Docker Compose (optional, for containerized execution)
* Google Gemini API Key 

## Setup Instructions
1. Clone this repository to your local machine.
2. Rename the provided `.env.example` file to `.env`.
3. Open the `.env` file and replace the placeholder with your actual Gemini API key:
   ```text
   GEMINI_API_KEY=your_actual_api_key_here
Note: If you are evaluating this project using a Free-Tier Gemini API key, you may hit rate limits (15 RPM). You can enable an optional 5-second delay between automated tests by adding USE_FREE_TIER_DELAY=true to your .env file.

How to Run Locally (Native)
Install the required dependencies:

Bash
pip install -r requirements.txt
Execute the main application:

Bash
python main.py
This will run through 15 automated test cases, print the interactions to the console, and append the results to route_log.jsonl.

How to Run via Docker (Containerized)
To run the application inside an isolated container, simply use Docker Compose:

Bash
docker-compose up --build
The docker-compose.yml file is configured with a volume mount, ensuring that the route_log.jsonl file generated inside the container during testing is successfully saved and accessible in your local project directory.