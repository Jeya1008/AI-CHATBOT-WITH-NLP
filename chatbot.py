import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", "hola", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "exit"],
    "name": ["your name", "who are you", "what are you called"],
    "help": ["help", "what can you do", "how to use"],
    "feeling": ["how are you", "how's it going"],
    "thanks": ["thank you", "thanks", "appreciate"],
}

responses = {
    "greeting": "Hello! 👋 How can I assist you today?",
    "farewell": "Goodbye! 👋 Have a great day.",
    "name": "I'm a smart chatbot built using spaCy.",
    "help": "I can respond to greetings, tell you who I am, and answer simple questions.",
    "feeling": "I'm just code, but I'm running smoothly! 😊",
    "thanks": "You're welcome! 🙏",
    "unknown": "I'm not sure I understand. Try rephrasing your question.",
}

# Match user input to intent
def classify_intent(text):
    doc = nlp(text.lower())
    for intent, keywords in intents.items():
        for token in doc:
            if token.text in keywords:
                return intent
        if any(kw in text.lower() for kw in keywords):
            return intent
    return "unknown"

def main():
    print("🤖 Smart Chatbot ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit", "bye"]:
            print("Bot:", responses["farewell"])
            break
        intent = classify_intent(user_input)
        print("Bot:", responses[intent])

if __name__ == "__main__":
    main()
