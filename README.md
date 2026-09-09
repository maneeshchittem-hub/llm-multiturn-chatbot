# 🤖 AI Conversation Assistant

A conversational AI chatbot built using Python, Google Gemini, FastAPI, and Streamlit.

The chatbot supports multi-turn conversations and remembers previous messages using conversation history and context-window management.

# 🚀 Features

- 💬 Multi-turn conversations
- 🧠 Conversation memory
- ✂️ Context-window management
- 🎯 Custom system prompt
- 🤖 Google Gemini API
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🕘 Chat history
- ⚙️ Settings and About sections
- 🛡️ Error handling
- 🔐 Secure API key management

# 🛠️ Technologies

- Python
- Google Gemini API
- Google GenAI SDK
- FastAPI
- Uvicorn
- Streamlit
- Requests
- Python-dotenv

# 📁 Project Structure

llm-multiturn-chatbot/
│
├── app.py
├── api.py
├── chatbot.py
├── requirements.txt
├── README.md
└── .gitignore

# ⚙️ Setup
1. Clone the repository
git clone https://github.com/maneeshchittem-hub/llm-multiturn-chatbot.git
2. Open the project
cd llm-multiturn-chatbot
3. Create virtual environment
python -m venv venv
4. Activate virtual environment
 Windows PowerShell:\venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
🔑 API Key Setup

Create a .env file in the project folder.

Add:

GEMINI_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

The .env file is already excluded using .gitignore.

## 🚀 Deployment

### Frontend
The Streamlit frontend is deployed using Streamlit Community Cloud.

### Backend
The FastAPI backend is deployed using Render.

**Backend:**  
https://llm-multiturn-chatbot-api.onrender.com/

### Architecture

User
↓
Streamlit Cloud (Frontend)
↓
Render (FastAPI Backend)
↓
Google Gemini APIend

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Start FastAPI:

uvicorn api:app --reload

Backend:

http://127.0.0.1:8000
Terminal 2 — Start Frontend

Open a second terminal in the project folder.

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Start Streamlit:

streamlit run app.py

Open the Streamlit URL shown in the terminal, usually:

http://localhost:8501
## 🔄 How It Works
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Google Gemini API
  ↓
AI Response
  ↓
Streamlit Frontend
  ↓
User
# 🧠 Context Management

The chatbot maintains conversation history so the AI can understand previous messages.

For longer conversations, older messages are truncated while recent messages are kept within the context window.

💬 Example
User: My name is Maneesh.

AI: Nice to meet you, Maneesh!

User: What is my name?

AI: Your name is Maneesh.
🛡️ Error Handling

# The application handles:

API failures
Connection errors
Request timeouts
Backend errors
Invalid responses

Users receive clear error messages instead of the application crashing.

🔐 Security
API keys are stored in .env
.env is included in .gitignore
API keys are never committed to GitHub
👨‍💻 Author:Maneesh Chittem

### 🌐 Live Demo

**Frontend:**  
https://ai-conversation-assistant.streamlit.app

**Backend API:**  
https://llm-multiturn-chatbot-api.onrender.com
