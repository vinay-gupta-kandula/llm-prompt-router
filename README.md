# LLM Prompt Router (Intent-Based Expert System)

## Overview
This project implements a **Prompt Router System** that classifies user intent and routes the request to a specialized expert persona. Instead of using a single general response, the system detects the user's intent and generates responses from a **domain-specific expert prompt**.

The system supports multiple intents such as:

- Coding assistance
- Data analysis
- Writing improvement
- Career guidance

All interactions are logged in a **JSONL file**, and the application can run both **locally and inside a Docker container**.

---

# Features

- Intent classification using keyword-based logic
- Prompt routing to expert personas
- Multiple expert roles:
  - Code Expert
  - Data Analyst
  - Writing Coach
  - Career Advisor
- Handles unclear or ambiguous user queries
- Command Line Interface (CLI)
- Structured JSON logging
- Docker container support
- Tested with **30+ input messages**

---

# System Architecture

The router follows this flow:

```

User Input
│
▼
Intent Classifier
│
▼
Detected Intent
(code / data / writing / career / unclear)
│
▼
Prompt Router
│
▼
Expert Persona Response
│
▼
Log Response to JSONL

```

---

# Project Structure

```

llm-prompt-router
│
├── classifier.py        # Intent classification logic
├── router.py            # Routes message to the correct expert
├── prompts.py           # Expert persona prompts
├── logger.py            # Logging system
├── main.py              # CLI interface
│
├── route_log.jsonl      # Interaction logs
│
├── Dockerfile           # Docker container setup
├── docker-compose.yml   # Docker compose configuration
│
├── README.md
├── .env.example
└── .gitignore

````

---

# Supported Intents

| Intent | Description |
|------|-------------|
| code | Programming questions |
| data | Data analysis or numerical calculations |
| writing | Writing improvement and grammar advice |
| career | Career guidance or interview preparation |
| unclear | Requests that do not match known categories |

---

# Running the Project

## Run Locally

Start the CLI program:

```bash
python main.py
````

Example interaction:

```
AI Intent Router System
Type 'exit' anytime to stop the program.

Your message: how to reverse a list in python

Detected Intent: code
Confidence Score: 0.88
```

---

# Example Test Inputs

The system was tested using multiple types of messages including clear, ambiguous, and typo-containing queries:

```
how do i sort a list of objects in python?
explain this sql query for me
This paragraph sounds awkward, can you help me fix it?
I'm preparing for a job interview, any tips?
what's the average of these numbers: 12, 45, 23, 67, 34
Help me make this better.
I need to write a function that takes a user id and returns their profile
hey
Can you write me a poem about clouds?
Rewrite this sentence to be more professional.
I'm not sure what to do with my career.
what is a pivot table
fxi thsi bug pls: for i in range(10) print(i)
How do I structure a cover letter?
My boss says my writing is too verbose.
```

More than **30 test interactions** were executed.

---

# Logging

All requests and responses are stored in:

```
route_log.jsonl
```

Example log entry:

```json
{
 "intent": "code",
 "confidence": 0.88,
 "user_message": "how to reverse a list in python",
 "final_response": "example solution..."
}
```

This logging system helps track **routing decisions and system responses**.

---

# Running with Docker

## Option 1 — Using Docker Compose

Build and run the container:

```bash
docker-compose up --build
```

The container will start the CLI application automatically.

Example output:

```
AI Intent Router System
Type 'exit' anytime to stop the program.
Your message:
```

---

## Option 2 — Run Docker Image Directly

You can also run the container manually:

```bash
docker run -it llm-prompt-router-prompt-router
```

This starts the container in **interactive mode**, allowing you to interact with the router through the terminal.

---

# Environment Variables

Create a `.env` file using `.env.example` as a reference.

Example:

```
OPENROUTER_API_KEY=your_api_key_here
```

⚠ **Do not commit your real API keys to GitHub.**

---

# Technologies Used

* Python
* Prompt Engineering
* JSON Logging
* Docker
* Command Line Interface (CLI)

---

# Future Improvements

Possible improvements for the system include:

* LLM-based intent classification instead of rule-based detection
* Web interface using **FastAPI or Flask**
* More expert personas
* Improved intent detection using **NLP models**
* Analytics dashboard for routing logs

---

# Author

**Vinay**

AI Prompt Router Project



