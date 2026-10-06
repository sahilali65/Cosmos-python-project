import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator")

st.title("Password Generator")
st.write("Generate a random password")

length = st.slider("Password Length", 4, 50, 12)

uppercase = st.checkbox("Uppercase Letters")
lowercase = st.checkbox("Lowercase Letters", value=True)
numbers = st.checkbox("Numbers", value=True)
symbols = st.checkbox("Symbols")

number = st.number_input(
    "Number of Passwords",
    min_value=1,
    max_value=10,
    value=1
)

def generate_password(length):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if characters == "":
        return ""

    return "".join(random.choice(characters) for _ in range(length))


if st.button("Generate Password"):

    if not (uppercase or lowercase or numbers or symbols):
        st.error("Please select at least one character type.")

    else:
        st.subheader("Generated Passwords")

        for i in range(number):
            password = generate_password(length)
            st.code(password)