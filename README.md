# Simple AI Chatbot

A minimal chatbot using Hugging Face Transformers.

## Dependencies

- transformers
- torch
- flask
- flask-cors

## Setup

1. Install dependencies:
   pip install -r requirements.txt
   pip install flask flask-cors

2. Run the backend server:
   python src/app.py

3. Open the frontend:
   Open frontend/index.html in your browser

---

## Here’s an overview of this full-stack AI chatbot project:

---

### 1. **Frontend (User Interface)**
- **Location:** frontend
- **Files:** index.html, `style.css`, script.js
- **Purpose:**  
  - Provides a chat interface for users in the browser.
  - Users type messages, which are displayed in the chat window.
  - JavaScript (script.js) sends user messages to the backend and displays bot responses.

---

### 2. **Backend (API Server)**
- **Location:** app.py
- **Framework:** Flask (Python)
- **Purpose:**  
  - Receives chat messages from the frontend via HTTP POST requests (`/chat` endpoint).
  - Uses Hugging Face Transformers (`gpt2` model) to generate AI responses.
  - Sends the generated response back to the frontend as JSON.
  - CORS is enabled so the browser can communicate with the backend.

---

### 3. **AI Model**
- **Library:** `transformers` (Hugging Face)
- **Model Used:** GPT-2 (a pre-trained text-generation model)
- **Purpose:**  
  - Generates human-like responses to user input.

---

### 4. **How It Works (Flow)**
1. **User** opens index.html and types a message.
2. **Frontend** sends the message to the backend (`/chat` endpoint) using JavaScript.
3. **Backend** receives the message, uses the AI model to generate a reply, and sends it back.
4. **Frontend** displays the bot’s reply in the chat window.

---

### 5. **Key Technologies**
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Backend:** Python, Flask, Flask-CORS
- **AI:** Hugging Face Transformers, PyTorch, GPT-2

---

### 6. **How to Run**
- Start the backend:  
  `python src/app.py`
- Open `frontend/index.html` in your browser.

---

