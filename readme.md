

# 🧠 MindCare Companion 🤖

> A Compassionate Mental Health Support Chatbot Using LangChain, Llama 3, HuggingFace Embeddings, and Flask.

![UI Screenshot](./screenshots/chatbot_ui.png)

---

## 📌 Table of Contents

* [🧠 About Project](#-about-project)
* [🚀 Features](#-features)
* [🛠️ Tech Stack](#️-tech-stack)
* [📂 Project Structure](#-project-structure)
* [🔧 How It Works](#-how-it-works)
* [📥 Installation](#-installation)
* [💡 Use Case](#-use-case)
* [🌐 Deployment](#-deployment)
* [📷 Screenshots](#-screenshots)
* [📢 Future Scope](#-future-scope)
* [🙋 Author](#-author)

---

## 🧠 About Project

**MindCare Companion** is a personalized AI chatbot designed to offer emotional support, analyze mental health sentiments, and suggest coping mechanisms based on user conversation — all **without diagnosing** or replacing professional help.

This AI system uses your **custom knowledge base (PDFs)**, stored in a vector DB (Chroma), to give supportive, informed responses grounded in context. The chatbot simulates a real, empathetic listener.

---

## 🚀 Features

* ✨ Personalized chat trained on your documents (e.g., psychology PDFs).
* 🧾 Real-time RetrievalQA powered by **LangChain + HuggingFace Embeddings**.
* 💡 Crisis detection logic (responds cautiously to mental health risks).
* 💬 Uses **Llama 3-70B** via **Groq API** for lightning-fast reasoning.
* 🗃️ Memory-efficient, persistent ChromaDB.
* 🎨 Styled front-end via HTML+CSS (via Flask interface).
* 🔁 Modular structure (easy to scale / integrate into apps).

---

## 🛠️ Tech Stack

| Technology                | Purpose                         |
| ------------------------- | ------------------------------- |
| `LangChain`               | Retrieval QA + document loading |
| `Llama 3 (via Groq)`      | LLM model backend               |
| `HuggingFace Embeddings`  | Text vectorization              |
| `ChromaDB`                | Vector DB for storage           |
| `Gradio`                   | Web interface                   |
| `PyMuPDF` / `PyPDFLoader` | PDF parsing                     |

---

## 📂 Project Structure

```
final_project/
│
├── app.py                 # Flask app launcher
├── config.py              # API keys and config vars
│
├── chatbot/
│   ├── cores.py           # Core setup: VectorDB, QA chain
│   ├── prompts.py         # PromptTemplate logic
│
├── data/                  # Your PDF knowledge base
│   ├── mental_health_doc.pdf
│
├── chroma_db/             # Saved vector DB
│
├── src/                   # Flask frontend src
│   ├── __init__.py
│   ├── app.py
|   ├── config.py
└── README.md            # ← You are here!
└── requirements.txt
```

---

## 🔧 How It Works

1. **Load PDFs** from the `./data` folder.
2. Split into chunks → embed them with HuggingFace Embeddings.
3. Store in persistent vector DB (Chroma).
4. On user query:

   * Retrieve relevant document chunks.
   * Send + prompt to Llama 3 via Groq.
   * Apply mental-health-specific logic (e.g., empathetic responses).
5. Display via Flask UI with conversation history.

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mindcare-companion.git
cd mindcare-companion
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv medi_bot
source medi_bot/bin/activate  # or .\medi_bot\Scripts\activate
pip install -r requirements.txt
```

### 3. Add Your Environment Variables

Create a `.env` file or update `config.py`:

```python
GROQ_API_KEY = "your_api_key_here"
LLM_MODEL = "llama-3-70b-versatile"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DATA_DIR = "./data"
DB_DIR = "./chroma_db"
```

### 4. Run the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 💡 Use Case

This project is ideal for:

* 🧘‍♂️ Mental health researchers building digital companions.
* 🏥 Therapists wanting context-aware assistants (not diagnostic).
* 🎓 Students building personalized educational chatbots.
* 🗃️ Anyone wanting a chatbot grounded in *their* documents.

---

## 🌐 Deployment

You can deploy via:

* **Render / Railway / Vercel** (for Flask backend)
* **Docker** (optional Dockerfile can be added)
* Add SSL and user auth if going public.

---

## 📷 Screenshots

### 🧠 Chatbot UI Interface

![Chatbot UI](./screenshots/chatbot_ui.png)

### 📁 Folder Structure

![Folder Structure](./screenshots/folder_view.png)

---

## 📢 Future Scope

* ✅ Add chat animation / loader (typing effect)
* 🧠 Incorporate mood detection via sentiment classification
* 🧾 Add multi-format loader (Word, HTML, etc.)
* 🌍 Add multilingual support (Hindi, etc.)
* ☁️ Cloud sync + user history retention

---


---

> 🧠 *MindCare Companion is not a medical device. It is designed to provide supportive suggestions, not treatment or diagnosis.*