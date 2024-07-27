import nltk
from nltk.tokenize import word_tokenize

# Initialize NLTK
nltk.download('punkt')

# Predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    }

def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        response = responses.get(user_input, "Chatbot: I didn't understand. Can you rephrase?")
        print("Chatbot:", response)

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    chatbot()
