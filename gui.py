import streamlit as st
from pathlib import Path
import requests
import time

# ======================
# Page config
# ======================
favicon_path = Path("Images/logo.png")

st.set_page_config(
    page_title="SV Testbench Analyzer",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=favicon_path if favicon_path.exists() else None
)

# ======================
# Session state
# ======================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "Ask"

if "language" not in st.session_state:
    st.session_state.language = "Verilog"

if "busy" not in st.session_state:
    st.session_state.busy = False

if "backend_url" not in st.session_state:
    st.session_state.backend_url = "https://osculant-danna-inclinational.ngrok-free.dev"

if "api_key" not in st.session_state:
    st.session_state.api_key = "secretSV_A123"

# ======================
# Load logo
# ======================
logo_path = Path("Images/pnsvlogo.png")
logo = logo_path.read_bytes() if logo_path.exists() else None

# ======================
# Custom CSS
# ======================
st.markdown("""
<style>
body {
    background-color: #f5f6fa;
}

header, footer {visibility: hidden;}

.app-header {
    background-color: #122958;
    padding: 2rem 2rem;
    margin: 1.5vh;
    border-radius: 10px;
}

.title {
    color: #f5c542;
    font-family: "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 3vw;
    font-weight: 600;
    line-height: 1.2;
    background: linear-gradient(90deg, #f5c542 0%, #c084fc 50%, #f5c542 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.subtitle {
    color: ##122958;
    font-family: "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 1.5vw;
    font-weight: 400;
    margin-top: 0.3rem;
}

.footer {
    background-color: gainsboro;
    color: #122958;
    text-align: center;
    padding: 0.6rem;
    font-size: 0.9rem;
    font-weight: 600;
    border-radius: 10px;
    margin-top: 20px;
}

/* Progress bar styling */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
}

/* Status text styling */
.status-text {
    font-size: 16px;
    font-weight: 500;
    color: #4a5568;
    margin: 10px 0;
    padding: 8px 12px;
    background: #f7fafc;
    border-radius: 6px;
    border-left: 4px solid #4F46E5;
}

/* Loading animation */
@keyframes pulse {
    0% { opacity: 0.6; }
    50% { opacity: 1; }
    100% { opacity: 0.6; }
}

.loading-pulse {
    animation: pulse 1.5s infinite;
}

/* Tool panel styling */
.tool-panel {
    background: white;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    margin-bottom: 20px;
}

.tool-button {
    margin: 8px 0;
    transition: all 0.3s ease;
}

.tool-button:hover {
    transform: translateY(-2px);
}

/* Chat message styling */
.chat-message {
    background: white;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.assistant-message {
    border-left: 4px solid #4F46E5;
}

.user-message {
    border-left: 4px solid #10B981;
}
</style>
""", unsafe_allow_html=True)

# ======================
# Header
# ======================
st.markdown("<div class='app-header'>", unsafe_allow_html=True)
cols = st.columns([1, 4])

with cols[0]:
    if logo:
        st.image(logo, width=300)

with cols[1]:
    st.markdown(
        "<div class='title'>Open-Source Verilog & SystemVerilog Testbench Analysis Assistant</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div class='subtitle'>Interpretation, structural parsing, suggesting practical enhancements, assisting in detection of potential syntax and logic issues and your friendly chatbot</div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)

# ======================
# Main layout - 2 COLUMNS (Left for tools, Right for chat)
# ======================
left, right = st.columns([1.2, 4])

# ======================
# TOOL PANEL (LEFT COLUMN) - THIS IS WHERE THE TOOLS ARE
# ======================
with left:
    # ======================
    # LANGUAGE SELECTOR
    # ======================
    st.markdown("#### 🌐 Select Language")
    st.caption("Choose the HDL or verification methodology")
    language_options = ["Verilog", "SystemVerilog", "UVM"]
    
    st.session_state.language = st.radio(
        "Language:",
        language_options,
        index=language_options.index(st.session_state.language),
        disabled=st.session_state.busy
    )
    
    
    # ======================
    # TOOL MODES - THIS IS YOUR TOOL MENU
    # ======================
    st.markdown("### 🛠️ Tool Modes")
    st.caption("Select how the assistant should reason")
    
    # Tool mode buttons
    mode_buttons = [
        ("🧠 Interpret Testbench", "Interpretation"),
        ("🐞 Find Potential Flaws", "Inspection"),
        ("🔌 Parse Signals & Blocks", "Parsing"),
        ("📘 Suggest Practical Enhancements", "Consultation"),
        ("💬 General Query", "Ask")
    ]
    
    for btn_text, mode in mode_buttons:
        # Highlight current mode
        is_current = st.session_state.mode == mode
        button_type = "primary" if is_current else "secondary"
        
        if st.button(
            btn_text,
            use_container_width=True,
            type=button_type,
            disabled=st.session_state.busy,
            key=f"mode_{mode}"
        ):
            st.session_state.mode = mode
            

# ======================
# CHAT WORKSPACE (RIGHT COLUMN)
# ======================
with right:
    st.markdown(f"###  Assistant - **{st.session_state.mode} Mode**")
    
    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            message_class = "user-message" if msg["role"] == "user" else "assistant-message"
            st.markdown(f'<div class="chat-message {message_class}">{msg["content"]}</div>', unsafe_allow_html=True)
    
    # User input
    user_input = st.chat_input(
        f"{st.session_state.mode} — paste SV code or ask a question",
        disabled=st.session_state.busy
    )
    
    # Summarize button
    col1, col2, col3 = st.columns([3, 1, 1])
    with col2:
        summarize_clicked = st.button(
            "📝 Summarize",
            disabled=st.session_state.busy | len(st.session_state.messages) ==0,
            use_container_width=True
        )
          # Clear chat button
        if st.button("🗑️ Clear Chat History", use_container_width=True, disabled=st.session_state.busy):
            st.session_state.messages = []
            st.rerun()
    
    # Process input
    if user_input or summarize_clicked:
        # Set busy state
        st.session_state.busy = True
        
        # Get summarize state
        summarize_state = 1 if summarize_clicked else 0
        
        # Show user message immediately
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            # Re-render to show user message
        elif summarize_state:
            st.session_state.messages.append({"role": "user", "content": st.session_state.messages[-1]["content"]})
        
        # ======================
        # PROGRESS INDICATOR SYSTEM
        # ======================
        progress_bar = st.progress(0)
        status_text = st.empty()
        try:
            # Step 1: Preparing request
            status_text.markdown('<div class="status-text loading-pulse">📝 Preparing your request...</div>', unsafe_allow_html=True)
            progress_bar.progress(10)
            time.sleep(0.3)
            
            # Prepare payload
            prompt_to_send =  st.session_state.messages[-1]["content"] if summarize_state else user_input if user_input else "" 
            
            payload = {
                "prompt": prompt_to_send,
                "mode": st.session_state.mode,
                "code_lan": st.session_state.language,
                "summarize_state": summarize_state
            }
            
            headers = {"Authorization": f"Bearer {st.session_state.api_key}"}
            
            # Step 2: Sending to backend
            status_text.markdown('<div class="status-text loading-pulse">🔄 Connecting to analysis engine...</div>', unsafe_allow_html=True)
            progress_bar.progress(30)
            
            # Step 3: Processing
            status_text.markdown('<div class="status-text loading-pulse">🧠 Analyzing code with AI engine...</div>', unsafe_allow_html=True)
            progress_bar.progress(50)
            
            # Make API call with timeout
            resp = requests.post(
                f"{st.session_state.backend_url}/sv2analyzer",
                json=payload,
                headers=headers,
                timeout= 660  
            )
            
            progress_bar.progress(80)
            
            # Step 4: Receiving response
            status_text.markdown('<div class="status-text loading-pulse">📊 Generating response...</div>', unsafe_allow_html=True)
            progress_bar.progress(90)
            
            # Check response
            if resp.status_code == 200:
                result = resp.json()
                response_text = result.get("response", "⚠️ No response from backend.")
                # Add analysis metadata if available
                if "analysis_time" in result:
                    response_text += f"\n\n*Analysis completed in {result['analysis_time']:.2f}s*"
            
            elif resp.status_code == 401:
                response_text = "❌ **Authentication Failed**\n\nPlease check your API key."
            elif resp.status_code == 404:
                response_text = "❌ **Endpoint Not Found**\n\nPlease check the backend URL."
            elif resp.status_code == 500:
                response_text = "❌ **Server Error**\n\nBackend server encountered an error."
            else:
                response_text = f"❌ **Error {resp.status_code}**\n\n{resp.text}"
                
        except requests.exceptions.Timeout:
            response_text = "⏰ **Request Timeout (120 seconds)**\n\nThe analysis is taking longer than expected."
        except requests.exceptions.ConnectionError:
            response_text = "🔌 **Connection Error**\n\nCannot connect to backend server."
        except Exception as e:
            response_text = f"❌ **Error**\n\n{str(e)}"
        finally:
            # Complete progress
            progress_bar.progress(100)
            status_text.markdown('<div class="status-text">✅ Analysis complete!</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Clear busy state
        st.session_state.busy = False
        
        # Rerun to show new message
        st.rerun()

# ======================
# Footer
# ======================
st.markdown(f"""
<div class="footer">
Copyright M7MD5303 🦅⚡ 
</div>
""", unsafe_allow_html=True)