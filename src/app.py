from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)
chatbot = pipeline("text-generation", model="gpt2")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    if user_message.lower() in ["exit", "quit"]:
        return jsonify({'reply': 'Goodbye!'})
    response = chatbot(user_message, max_length=100, num_return_sequences=1)
    reply = response[0]['generated_text']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
