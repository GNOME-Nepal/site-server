import json
import numpy as np
import nltk
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from .nltk_utils import tokenize, stem, bag_of_words

# Load intents
intents = json.loads(open("chat/utils/intents.json").read())

# Training Data
words = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(set(words))
classes = sorted(set(classes))

# Convert data
training = []
for doc in documents:
    bag = bag_of_words(doc[0])
    output = [0] * len(classes)
    output[classes.index(doc[1])] = 1
    training.append([bag, output])

training = np.array(training, dtype=object)

# Create model
model = Sequential([
    Dense(128, input_shape=(len(words),), activation='relu'),
    Dense(64, activation='relu'),
    Dense(len(classes), activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(np.array(training[:, 0].tolist()), np.array(training[:, 1].tolist()), epochs=200, batch_size=8)
model.save("chat/utils/chatbot_model.h5")
