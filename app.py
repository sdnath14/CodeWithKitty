
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from io import BytesIO
import google.generativeai as genai

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# ------------------------- CONFIGURATION -------------------------
# Set page configuration
st.set_page_config(page_title="Sneha's ChatBot", layout="wide")

# Configure Gemini API securely
genai.configure(api_key=st.secrets["gemini"]["api_key"])  # Define this in .streamlit/secrets.toml

# ------------------------- SIDEBAR -------------------------
with st.sidebar:
    # Sidebar Navigation Menu
    selected = option_menu(
        menu_title="Kitty's ChatBot",
        options=["About Me", "Projects","Ask Kitty (Chatbot)", "Contact Me"],
        icons=["person-circle", "folder", "file-earmark-person", "robot", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

    # # Display image below navigation menu
    # sidebar_image = Image.open("me.png")  # Ensure this image is in your project folder
    # st.image(sidebar_image, use_container_width=True)


# ------------------------- ABOUT ME -------------------------


if selected == "About Me":
    from PIL import Image
    from io import BytesIO
    import base64

    # Load and encode profile image
    image = Image.open("me.jpeg")  # Replace with your image filename
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode()

    # Define fixed colors
    bg_color = "#ffffff"
    text_color = "#000000"
    accent_color = "#ff4d4d"

    # Page styling
    st.markdown(f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}

    .animated-title {{
        font-size: 58px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, {accent_color}, #ff6666, {accent_color});
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 4s ease infinite;
        font-family: 'Courier New', monospace;
        
    }}

    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .section-header {{
        color: {accent_color};
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 10px;
    }}

    .ring-container {{
        position: relative;
        width: 220px;
        height: 220px;
        margin: 30px auto;
        animation: float 4s ease-in-out infinite;
    }}

    .ring-border {{
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 6px solid transparent;
        border-top: 6px solid {accent_color};
        animation: spin 2s linear infinite;
    }}

    .ring-container img {{
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        position: absolute;
        top: 20px;
        left: 20px;
        box-shadow: 0 0 20px {accent_color};
    }}

    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-12px); }}
        100% {{ transform: translateY(0px); }}
    }}

    .social-icons {{
        text-align: center;
        margin-top: 20px;
    }}

    .social-icons a {{
        display: inline-block;
        margin: 10px;
        transition: transform 0.3s, box-shadow 0.3s;
    }}

    .social-icons a:hover {{
        transform: scale(1.1);
        box-shadow: 0 0 10px {accent_color};
    }}

    .about-text {{
        font-size: 17px;
        text-align: center;
        margin: auto;
        max-width: 650px;
        line-height: 1.7;
    }}
    </style>

   <h1 class="animated-title">Welcome to my Project Showcase Website and meet My partner kitty</h1>

    """, unsafe_allow_html=True)

    

    # Spinning profile image
    st.markdown(f"""
    <div class="ring-container">
        <div class="ring-border"></div>
        <img src="data:image/png;base64,{img_base64}" />
    </div>
    """, unsafe_allow_html=True)

    # About Me section
    st.markdown('<div class="section-header">💫 About Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class=about-text>
         👋 Hi! It's Kitty's here...<br>
    🎉 Welcome to Kitty's Website<br>
    🧠 Kitty is Sneha's coding partner<br>
    💬 Ask anything to me – I'm here to help!
    </div>
    """, unsafe_allow_html=True)

    # Social Links section
    st.markdown('<div class="section-header">🌐 Connect with Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.instagram.com/_s.dnath_/" target="_blank">
            <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white">
        </a>
        <a href="https://www.linkedin.com/in/sneha-debnath-11a631258/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white">
        </a>
        <a href="https://in.pinterest.com/snehadebnath145/" target="_blank">
            <img src="https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=Pinterest&logoColor=white">
        </a>
        <a href="https://x.com/Sdnath14S" target="_blank">
            <img src="https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white">
        </a>
        <a href="mailto:snehadebnath145@gmail.com">
            <img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white">
        </a>
    </div>
    """, unsafe_allow_html=True)






# # ------------------------- PROJECTS -------------------------
elif selected == "Projects":
    st.title("💼 My Projects")
    st.subheader("🎥 Project Walkthroughs")
    st.write("Watch short demos and walkthroughs of my featured projects.")

    # 🍳 Recipe Diary Project
    with st.expander("🍳 Recipe Diary Demo"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video("videos/Recipe.mov")
        st.markdown("### 🍳 Recipe Diary")
        st.write("Generates food recipes with images using AI.")
        st.markdown("**Tech Stack:** Python, FastAPI, HTML, CSS, JavaScript")
        st.markdown("[🔗 GitHub](https://github.com/sdnath14/PAN-Diary.git)")

    # 💰 Expense Tracker Project
    with st.expander("💰 Expense Tracker Demo"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video("videos/Expense Tracker.mov")
        st.markdown("### 💰 Expense Tracker")
        st.write("CRUD app for tracking expenses built with Spring Boot and Thymeleaf.")
        st.markdown("**Tech Stack:** Java, Spring Boot, H2, Thymeleaf")
        st.markdown("[🔗 GitHub](https://github.com/sdnath14/Expense_Tracker.git)")

    # 🧠 AI Article Generator Project
    with st.expander("🧠 AI Article Generator Demo"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video("videos/Article.mov")
        st.markdown("### 🧠 AI Article Generator")
        st.write("Generates full-length articles using AI with images and summaries.")
        st.markdown("**Tech Stack:** Python, Streamlit, Gemini API, Pexels API, News API")
        st.markdown("[🔗 GitHub](https://github.com/sdnath14/ARTICLE-AI.git)")

    # 📰 News App Project
    with st.expander("📰 News App Demo"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video("videos/NewsAPP.mov")
        st.markdown("### 📰 News App")
        st.write("Displays real-time news articles with a clean Flask-based UI.")
        st.markdown("**Tech Stack:** Python, Flask, HTML5, CSS3, SCSS, NewsAPI")
        st.markdown("[🔗 GitHub](https://github.com/sdnath14/News_app.git)")

    # 💬 Chat App Project
    with st.expander("💬 Chat App Demo"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video("videos/ChatApp.mov")
        st.markdown("### 💬 Chat App")
        st.write("A real-time chat system using Java, WebSocket, and Thymeleaf.")
        st.markdown("**Tech Stack:** Java, Spring Boot, Thymeleaf, WebSocket")
        st.markdown("[🔗 GitHub](https://github.com/sdnath14/ChatApp.git)")



# ------------------------- CHATBOT -------------------------


elif selected == "Ask Kitty (Chatbot)":
    st.title("🐱 Ask Me Anything")
    st.markdown("Ask about my experience, skills, projects, or anything from my resume!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Type your question here...")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                chat = model.start_chat(history=[])

                prompt = f"""
You're a chatbot assistant for Sneha's portfolio site.
Here’s some background:

- Name: Sneha
- Background: Aspiring Java Developer, skilled in Spring Boot, FastAPI, LangChain,python and she is a web developer 
she knows node js ,react ,javascript also.
- Projects:
  - Book Recommender (LangChain + Qdrant)
  - Real-time Chat App (Spring Boot + WebSockets)
  - Portfolio Site (Streamlit)
  -NewsAPP using Flask and Scss.
  _Fluffs pan diary a recipe ai generator with pic and steps .a cute recipe app.with js,fastapi,html,css,
  -her portfolio website with next js and css.
- Interests: AI, backend, scalable systems
- your name is Kitty when someone asks you who are you? then you are snehas coding partner and pet.
-you are also programmed by her.and 

User's question:
{user_input}
"""
                response = chat.send_message(prompt)
                reply_text = response.text

                # Store messages
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("assistant", reply_text))

            except Exception as e:
                st.error(f"❌ Error: {e}")

    # ✅ Only show chat history (once per message)
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)


# ------------------------- CONTACT -------------------------
elif selected == "Contact Me":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit = st.form_submit_button("Send")

    if submit:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            try:
                sender_email = st.secrets["email"]["sender"]
                sender_password = st.secrets["email"]["password"]
                receiver_email = st.secrets["email"]["receiver"]

                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg["Subject"] = f"New message from {name} via Portfolio Contact Form"

                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                msg.attach(MIMEText(body, "plain"))

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())

                st.success("✅ Thanks! Your message has been sent successfully.")

            except Exception as e:
                st.error(f"❌ Sorry, there was an error sending your message: {e}")

    
