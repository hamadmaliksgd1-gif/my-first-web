import streamlit as st

# Set the page title
st.set_page_config(page_title="My First Streamlit App", page_icon="🚀")

# Header and description
st.title("Welcome to My Streamlit App!")
st.write("This is a simple web app built with Streamlit and hosted via GitHub.")

---

# Interactive Section 1: Text Input
st.subheader("Say Hello")
user_name = st.text_input("What is your name?", placeholder="Type your name here...")

if user_name:
    st.success(f"Hello, {user_name}! Welcome to the app. 👋")

---

# Interactive Section 2: Slider & Button
st.subheader("Interactive Slider")
number = st.slider("Select a number", min_value=1, max_value=100, value=50)

if st.button("Calculate Square"):
    square = number ** 2
    st.metric(label=f"The square of {number} is:", value=square)
