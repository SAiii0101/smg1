from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# You can also train the chatbot on your custom data
# trainer.train([
#     'How are you?',
#     'I am good, thank you!',
#     'What is your name?',
#     'My name is SimpleBot.'
# ])

# Interactive chat loop
print("SimpleBot: Hello! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print("SimpleBot:", response)
