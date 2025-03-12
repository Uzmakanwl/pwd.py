import re
import streamlit as st
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin:auto;}
    .stButton button {width:50%; background-color black; color:green; font-size: 18px;}
    .stButton button:hover {background-color: #45a049;}
</style>
            """, unsafe_allow_html=True)


#page title and description
st.title("🔐 Password Generator")
st.write("Enter your password below to check it security level. 🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1 
    else:
        feedback.append("❌ password should be **at least 8 characters long**.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("❌ password should include **both upperb and lower case letters**.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ password should include **at least one number (0-9)**.")

    #special character
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
        feedback.append("❌ Include **at least one special character (!@#$^&*)**.")

    #display password strength results
    if score == 4:
        st.success("✅ **strong password** -  your password is secure. ")
    elif score ==3:
        st.info(" ⚠️**Moderate Passwored** - consider imporiving security by adding more features")
    else:
        st.error(" ❌ **Week Password** - Follow the suggestion below to strength it. ")

        #feedback
    if feedback:
        st.error(" 🔍 **improve your password**")
        for item in feedback:
            st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

#Button working
if st.button("check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning(" please enter a password first!")
        