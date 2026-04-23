import json

# Load knowledge base
with open("knowledge.json") as f:
    kb = json.load(f)

# Lead capture function
def mock_lead_capture(name, email, platform):
    print(f"\n Lead captured successfully: {name}, {email}, {platform}\n")

# Simple memory
memory = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

# Intent detection
def detect_intent(user_input):
    user_input = user_input.lower()

    # HIGH INTENT FIRST (IMPORTANT)
    if any(word in user_input for word in ["buy", "try", "subscribe", "pro plan", "i want"]):
        return "high_intent"

    # INQUIRY
    elif any(word in user_input for word in ["price", "pricing", "cost", "plans"]):
        return "inquiry"

    # GREETING
    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    else:
        return "other"
# RAG response
def answer_query():
    basic = kb["plans"]["basic"]
    pro = kb["plans"]["pro"]

    return f"""
📦 AutoStream Plans:

Basic Plan:
- Price: {basic['price']}
- Videos: {basic['videos']}
- Quality: {basic['quality']}

Pro Plan:
- Price: {pro['price']}
- Videos: {pro['videos']}
- Quality: {pro['quality']}
- Features: {', '.join(pro['features'])}
"""

# Chat loop
def chat():
    print("AutoStream Agent Ready! Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        intent = detect_intent(user_input)

        # Greeting
        if intent == "greeting":
            print("Agent: Hey! How can I help you today? ")

        # Inquiry → RAG
        elif intent == "inquiry":
            print("Agent:", answer_query())

        # High Intent
        elif intent == "high_intent":
            print("Agent: Awesome! Let's get you started ")

            # Collect details
            if not memory["name"]:
                memory["name"] = input("Agent: What's your name? ")

            if not memory["email"]:
                memory["email"] = input("Agent: Your email? ")

            if not memory["platform"]:
                memory["platform"] = input("Agent: Which platform do you use? ")

            # Call tool
            mock_lead_capture(
                memory["name"],
                memory["email"],
                memory["platform"]
            )

        else:
            print("Agent: Can you clarify that? ")

# Run
chat()