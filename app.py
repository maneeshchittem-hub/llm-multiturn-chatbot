import streamlit as st
import requests


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Conversation Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 15% 10%,
            rgba(79,70,229,0.18),
            transparent 30%),
        radial-gradient(circle at 85% 10%,
            rgba(14,165,233,0.14),
            transparent 30%),
        linear-gradient(135deg,#050816,#0b1020,#101a2e);

    color: white;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 20px;
    padding-bottom: 100px;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background: #070b18;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] {
    width: 310px !important;
}

[data-testid="stSidebar"] .stButton > button {

    width: 100%;
    min-height: 44px;

    border-radius: 12px;

    background: rgba(255,255,255,0.04);

    color: #e2e8f0;

    border: 1px solid rgba(255,255,255,0.08);

    font-size: 14px;

    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stButton > button:hover {

    background: rgba(59,130,246,0.18);

    border-color: rgba(96,165,250,0.45);

    transform: translateY(-1px);
}


/* Sidebar logo */

.sidebar-brand {

    display: flex;
    align-items: center;
    gap: 12px;

    margin-top: 15px;
    margin-bottom: 15px;
}

.sidebar-logo {

    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 15px;

    background:
        linear-gradient(135deg,#2563eb,#7c3aed);

    font-size: 24px;

    box-shadow:
        0 0 25px rgba(59,130,246,0.35);
}

.sidebar-name {

    font-size: 21px;
    font-weight: 750;
    color: white;
}

.sidebar-description {

    color: #94a3b8;
    font-size: 12px;
}

.sidebar-divider {

    height: 1px;

    background: rgba(255,255,255,0.08);

    margin: 22px 0;
}

.sidebar-title {

    color: #64748b;

    font-size: 11px;

    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 1px;

    margin-top: 22px;

    margin-bottom: 10px;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    position: relative;

    overflow: hidden;

    padding: 45px 42px;

    border-radius: 25px;

    margin-bottom: 28px;

    background:
        linear-gradient(
            120deg,
            rgba(30,64,175,0.42),
            rgba(79,70,229,0.22),
            rgba(6,182,212,0.13)
        );

    border:
        1px solid rgba(129,140,248,0.20);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.28);
}

.hero-glow {

    position: absolute;

    width: 280px;
    height: 280px;

    right: -100px;
    top: -130px;

    border-radius: 50%;

    background: rgba(99,102,241,0.25);

    filter: blur(65px);
}

.hero-content {

    position: relative;

    z-index: 2;
}

.hero-icon {

    font-size: 40px;

    margin-bottom: 10px;

    animation: float 3s ease-in-out infinite;
}

@keyframes float {

    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-7px);
    }

    100% {
        transform: translateY(0);
    }
}

.hero-title {

    font-size: 38px;

    font-weight: 800;

    line-height: 1.2;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #93c5fd,
            #c4b5fd,
            #67e8f9
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.hero-subtitle {

    margin-top: 10px;

    color: #a5b4c8;

    font-size: 15px;

    max-width: 700px;

    line-height: 1.6;
}


/* ============================================================
   WELCOME
   ============================================================ */

.welcome {

    max-width: 850px;

    margin: 15px auto 25px auto;

    padding: 20px;

    text-align: center;

    border-radius: 18px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.07);
}

.welcome-title {

    font-size: 19px;

    font-weight: 700;

    color: white;
}

.welcome-text {

    margin-top: 6px;

    color: #94a3b8;

    font-size: 13px;
}


/* ============================================================
   CHAT BUBBLES
   ============================================================ */

[data-testid="stChatMessage"] {

    max-width: 900px;

    margin: 12px auto;

    background: transparent !important;

    border: none !important;
}

[data-testid="stChatMessageContent"] {

    padding: 14px 18px !important;

    border-radius: 18px !important;

    line-height: 1.65 !important;

    font-size: 15px !important;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.18);
}


/* Assistant */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
)
[data-testid="stChatMessageContent"] {

    background:
        linear-gradient(
            135deg,
            rgba(30,41,59,0.96),
            rgba(15,23,42,0.96)
        ) !important;

    color: #e2e8f0 !important;

    border:
        1px solid rgba(148,163,184,0.12);

    border-bottom-left-radius: 5px !important;
}


/* User */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
)
[data-testid="stChatMessageContent"] {

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #4f46e5
        ) !important;

    color: white !important;

    border:
        1px solid rgba(147,197,253,0.25);

    border-bottom-right-radius: 5px !important;
}


/* ============================================================
   CHAT INPUT
   ============================================================ */

[data-testid="stChatInput"] {

    max-width: 900px;

    margin: 25px auto 0 auto;
}

[data-testid="stChatInput"] > div {

    background:
        rgba(15,23,42,0.97) !important;

    border:
        1px solid rgba(129,140,248,0.30) !important;

    border-radius: 20px !important;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.30);
}

[data-testid="stChatInput"] > div:focus-within {

    border-color:
        rgba(99,102,241,0.80) !important;
}

[data-testid="stChatInput"] textarea {

    color: white !important;

    background: transparent !important;

    font-size: 15px !important;
}

[data-testid="stChatInput"] textarea::placeholder {

    color: #64748b !important;
}


/* ============================================================
   DIALOG
   ============================================================ */

[data-testid="stDialog"] {

    background: #0f172a !important;
}

[data-testid="stDialog"] h1,
[data-testid="stDialog"] h2,
[data-testid="stDialog"] h3 {

    color: white !important;
}

[data-testid="stDialog"] p {

    color: #cbd5e1 !important;
}


/* Footer */

.footer {

    text-align: center;

    color: #334155;

    font-size: 11px;

    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

if "show_history" not in st.session_state:
    st.session_state.show_history = False


# ============================================================
# BACKEND REQUEST
# ============================================================

def get_bot_response(message):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            params={
                "message": message
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Sorry, I could not generate a response."
        )

    except requests.exceptions.Timeout:

        return "⏳ The request timed out. Please try again."

    except requests.exceptions.ConnectionError:

        return (
            "🔌 Backend connection failed. "
            "Please make sure FastAPI is running."
        )

    except requests.exceptions.RequestException:

        return (
            "⚠️ There was a problem communicating "
            "with the backend."
        )

    except Exception:

        return "⚠️ Something went wrong. Please try again."


# ============================================================
# SETTINGS DIALOG
# ============================================================

@st.dialog("⚙️ Settings")
def show_settings():

    st.write("### Chat Settings")

    st.write(
        "Your chatbot is configured to maintain "
        "conversation context."
    )

    st.write("**AI Model:** Gemini")

    st.write("**Context Management:** Last messages")

    st.write("**Interface:** Streamlit")

    st.write("**Backend:** FastAPI")

    st.divider()

    st.info(
        "These settings are currently configured "
        "for your internship project."
    )


# ============================================================
# ABOUT DIALOG
# ============================================================

@st.dialog("ⓘ About")
def show_about():

    st.write("### AI Conversation Assistant")

    st.write(
        "A conversational AI chatbot built for the "
        "internship project."
    )

    st.write("#### Features")

    st.write("💬 Multi-turn conversations")

    st.write("🧠 Conversation context")

    st.write("✂️ Context-window management")

    st.write("🎯 Custom system prompt")

    st.write("⚡ Error handling")

    st.write("🤖 Gemini LLM")

    st.write("🌐 FastAPI backend")

    st.write("🎨 Streamlit interface")

    st.divider()

    st.write(
        "Built using Python, Gemini, FastAPI and Streamlit."
    )


# ============================================================
# CHAT HISTORY DIALOG
# ============================================================

@st.dialog("🕘 Chat History")
def show_history():

    if not st.session_state.history:

        st.info(
            "No previous conversations yet."
        )

        return


    st.write("### Previous Conversations")

    for i, conversation in enumerate(
        reversed(st.session_state.history)
    ):

        title = conversation["title"]

        st.write(f"**{i + 1}. {title}**")

        if st.button(
            "Open conversation",
            key=f"history_{i}"
        ):

            st.session_state.messages = conversation["messages"]

            st.rerun()

        st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
        <div class="sidebar-brand">

            <div class="sidebar-logo">
                🤖
            </div>

            <div>

                <div class="sidebar-name">
                    AI Assistant
                </div>

                <div class="sidebar-description">
                    Smart • Conversational • Context Aware
                </div>

            </div>

        </div>

        <div class="sidebar-divider"></div>
    """)


    # --------------------------------------------------------
    # NEW CONVERSATION
    # --------------------------------------------------------

    if st.button("＋  New Conversation"):

        # Save current conversation

        if st.session_state.messages:

            first_message = st.session_state.messages[0]

            title = first_message["content"]

            if len(title) > 35:
                title = title[:35] + "..."

            st.session_state.history.append({
                "title": title,
                "messages": st.session_state.messages.copy()
            })


        # Clear current conversation

        st.session_state.messages = []

        st.rerun()


    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    st.html("""
        <div class="sidebar-title">
            Navigation
        </div>
    """)


    # Chat History

    if st.button("🕘  Chat History"):

        show_history()


    # Settings

    if st.button("⚙️  Settings"):

        show_settings()


    # About

    if st.button("ⓘ  About"):

        show_about()


    # --------------------------------------------------------
    # QUICK PROMPTS
    # --------------------------------------------------------

    st.html("""
        <div class="sidebar-title">
            Quick Prompts
        </div>
    """)


    if st.button("🐍  Explain Python"):

        question = "Explain Python in simple terms."

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        answer = get_bot_response(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()


    if st.button("🧠  What is AI?"):

        question = "What is Artificial Intelligence?"

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        answer = get_bot_response(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()


    if st.button("💻  Give me a problem"):

        question = "Give me a beginner programming problem."

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        answer = get_bot_response(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()


# ============================================================
# TOP BAR
# ============================================================

st.html("""
    <div class="top-bar">

        <div class="top-left">
            💬 New Conversation
        </div>

        <div class="top-right">
            AI Assistant
        </div>

    </div>
""")


# ============================================================
# HERO
# ============================================================

st.html("""
    <div class="hero">

        <div class="hero-glow"></div>

        <div class="hero-content">

            <div class="hero-icon">
                ✨
            </div>

            <div class="hero-title">
                Hello, I'm your AI Assistant 👋
            </div>

            <div class="hero-subtitle">
                Ask me anything and I'll remember the relevant
                context throughout our conversation.
            </div>

        </div>

    </div>
""")


# ============================================================
# WELCOME
# ============================================================

if not st.session_state.messages:

    st.html("""
        <div class="welcome">

            <div class="welcome-title">
                👋 Welcome to your AI Assistant
            </div>

            <div class="welcome-text">
                Start a conversation below or choose
                a quick prompt from the sidebar.
            </div>

        </div>
    """)


# ============================================================
# DISPLAY CHAT
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_message = st.chat_input(
    "Message your AI Assistant..."
)


# ============================================================
# PROCESS MESSAGE
# ============================================================

if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })


    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(user_message)


    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner("✨ Thinking..."):

            bot_message = get_bot_response(
                user_message
            )

        st.markdown(bot_message)


    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_message
    })


# ============================================================
# FOOTER
# ============================================================

st.html("""
    <div class="footer">
        AI Conversation Assistant
    </div>
""")