# autostream-agent
AI-powered conversational agent that converts user queries into qualified leads using intent detection, RAG, and controlled tool execution.

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the project:
   python main.py

## Architecture Explanation

This project implements a conversational AI agent using a modular pipeline design. I chose a structured agent-based approach inspired by LangGraph concepts, where the system flows through multiple stages such as intent detection, knowledge retrieval, and tool execution.

The agent first classifies user input into predefined intents such as greeting, inquiry, and high-intent. For knowledge-based queries, a Retrieval-Augmented Generation (RAG) approach is used, where responses are generated from a local JSON knowledge base instead of hardcoding answers.

State management is handled using a custom AgentState class, which stores user intent and collected details such as name, email, and platform across multiple conversation turns. This ensures continuity and avoids repeated questions.

Tool execution is carefully controlled. The lead capture function is triggered only after all required user details are collected, preventing premature execution. This mimics real-world production systems where validation is critical.

The architecture is simple, scalable, and easy to extend with real LLMs or APIs.

## WhatsApp Integration

This agent can be integrated with WhatsApp using Twilio's API and webhooks.

Incoming messages from WhatsApp are received via a webhook endpoint. The message is then passed to the agent logic for processing . The agent generates a response, which is sent back to the user through Twilio’s messaging API.

To maintain conversation state across multiple messages, a database like MongoDB can be used. Each user session can be tracked using their phone number as a unique identifier.

This setup enables real-time, scalable deployment of the AI agent on WhatsApp.
