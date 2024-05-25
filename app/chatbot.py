import nltk
from nltk.chat.util import Chat, reflections

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')

# Define the pairs for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I help you with?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to help you with your queries.",]
    ],
    [
        r"how are you?",
        ["I'm a bot, so I don't have feelings, but I'm here to help you!",]
    ],
    [
        r"what are your hours?",
        ["We are open from 9 AM to 5 PM, Monday to Friday.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! Is there anything else I can help with?",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?",]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def get_response(query):
    return chatbot.respond(query)
