import streamlit as st
from cryptography.fernet import Fernet
import base64

# 1. Page Styling (The Spidey Suit)
st.set_page_config(page_title="Spidey-Sense Decoder", page_icon="🕷️")

st.markdown("""
    <style>
    .stApp {
        background-color: #001a33; /* Deep Blue */
    }
    h1, h2, h3 {
        color: #E60000 !important; /* Spidey Red */
        font-family: 'Bangers', cursive;
    }
    .stButton>button {
        background-color: #E60000;
        color: white;
        border-radius: 20px;
        border: 2px solid #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🕷️ WEB-ENCRYPTED MESSAGING 🕸️")
st.subheader("Cyber Love Letter")

# 2. The Secret Key Logic
# In a real app, you'd hide this, but for your fun project, 
# we'll use a "fixed" key based on a word you both know.
def generate_key(secret_word):
    # This turns a simple word into a 32-byte key for encryption
    key = base64.urlsafe_b64encode(secret_word.ljust(32)[:32].encode())
    return key

# Set your "Secret Key" here 
user_key = generate_key("J262427")
cipher = Fernet(user_key)

# 3. The UI Layout
tab1, tab2 = st.tabs(["🔒 LOCK A MESSAGE", "🔓 UNLOCK A WEB"])

with tab1:
    st.write("Type a message to turn it into a secret web:")
    secret_text = st.text_area("Your Message:", placeholder="e.g. Meet me at the bakery...")
    if st.button("Generate Secret Web"):
        if secret_text:
            encrypted_text = cipher.encrypt(secret_text.encode()).decode()
            st.success("Message Locked! Copy this code to send them:")
            st.code(encrypted_text)
        else:
            st.warning("With great power comes... the need to actually type a message!")

with tab2:
    st.write("Paste the secret web code here to read it:")
    incoming_web = st.text_input("Enter Secret Code:")
    if st.button("Activate Spidey-Sense"):
        try:
            decrypted_text = cipher.decrypt(incoming_web.encode()).decode()
            st.balloons()
            st.markdown(f"### 🛡️ Decoded Message:\n**{decrypted_text}**")
        except:
            st.error("Invalid Code! The web was tampered with or the key is wrong.")

st.markdown("---")
st.write("🔒 *Encrypted with Cyber-Security Grade AES-128*")
