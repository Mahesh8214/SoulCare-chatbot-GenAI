# app.py
import gradio as gr
from chatbot.cores import initialize_llm, load_or_create_vector_db, setup_qa_chain

print("🚀 Initializing chatbot...")
llm = initialize_llm()
vector_db = load_or_create_vector_db()
qa_chain = setup_qa_chain(vector_db, llm)

def chatbot_response(message, history):
    if not message.strip():
        return "Please enter a valid message."
    return qa_chain.run(message)

with gr.Blocks(theme=gr.themes.Soft(primary_hue="teal", secondary_hue="emerald")) as app:
    gr.Markdown("""
    <div style='text-align:center; background:linear-gradient(to right,#0f766e,#0d9488); 
    padding:20px; border-radius:10px; color:white;'>
    <h1>🧠 MindCare Companion 🤖</h1>
    <p>Your compassionate mental health support chatbot</p>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""
            ### About This Chatbot
            - Offers non-judgmental listening
            - Suggests coping strategies
            """)
            gr.HTML("""
            <div style='background:#f0fdfa; padding:15px; border-radius:10px; border-left:4px solid #0d9488;'>
            <p><strong>Note:</strong> If you're in crisis, contact a licensed professional.</p>
            </div>
            """)
        with gr.Column(scale=2):
            gr.ChatInterface(
                fn=chatbot_response,
                title="MindCare Companion",
                examples=[
                    "How can I manage anxiety?",
                    "I'm feeling overwhelmed lately.",
                    "Suggest ways to cope with stress."
                ],
                submit_btn="Send",
                retry_btn="Regenerate",
                undo_btn="Delete",
                clear_btn="Clear"
            )

    gr.Markdown("""
    <div style='text-align:center; margin-top:20px; color:#64748b; font-size:0.9em;'>
    Confidential and secure | Your privacy is protected
    </div>
    """)

app.launch(favicon_path="https://emojicdn.elk.sh/🧠")
