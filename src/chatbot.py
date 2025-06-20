from transformers import pipeline

# Load a text-generation pipeline with a small model
chatbot = pipeline("text-generation", model="gpt2")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    print("Chatbot:", response[0]['generated_text'])
