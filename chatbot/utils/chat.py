import json
import random
import torch
import torch.nn as nn
import torch.optim as optim
from .nltk_utils import bag_of_words, tokenize

# Load intents
with open("chatbot/utils/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Define a simple PyTorch chatbot model
class ChatbotModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ChatbotModel, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.l1(x))
        x = self.l2(x)
        return x

# Dummy chatbot response function (replace with actual ML model later)
def chatbot_response(msg):
    sentence = tokenize(msg)  # Tokenize user input

    
    vocabulary = []  
    bow = bag_of_words(sentence, vocabulary)  # Correct usage

    response_list = []

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in msg.lower():
                response_list = intent["responses"]

    if response_list:
        return random.choice(response_list)
    
    return "I didn't understand. Can you rephrase?"
