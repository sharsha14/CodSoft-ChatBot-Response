import re

# Define a dictionary of patterns and responses
patterns = {
    r'hi|hello|hey': ["Hello!", "Hi there!", "Hey!"],
    r'how are you': ["I'm doing well, thank you.", "I'm just a computer program, but I'm here to help!"],
    r'what is your name': ["I'm a chatbot.", "I don't have a name, but you can call me ChatGPT."],
    r'bye|goodbye': ["Goodbye!", "See you later!", "Farewell!"],
    r'age|old|years': ["I don't age, but I'm here to assist you."],
    r'(?:who|what) (?:is|are) you': ["I'm an AI chatbot created to answer your questions."],
    r'(?:tell me|say) (?:a )?joke': ["Why did the computer catch a cold? Because it had too many windows open!"],
    r'(?:what is|tell me about) (?:OpenAI|GPT)': [
        "OpenAI is an artificial intelligence research organization. GPT stands for 'Generative Pre-trained Transformer'.",
        "OpenAI is known for its cutting-edge AI models like GPT-3, which I'm based on."],
}

# Function to respond to user input
def chatbot_response(user_input):
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return responses

    return ["I'm not sure how to respond to that.", "Could you please rephrase your question?"]

# Main chat loop
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response[0])
