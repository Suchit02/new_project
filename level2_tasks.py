"""Level 2 tasks for the Python Learning Dashboard."""
import streamlit as st
from utils import check_password_strength, generate_fibonacci, analyze_text_file

def guessing_game():
    """Task 1: Number guessing game implementation."""
    st.subheader("Guessing Game (1-100)")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.random_number:
            st.success(f"🎉 Congratulations! You got it in {st.session_state.attempts} attempts!")
            if st.button("Play Again"):
                st.session_state.random_number = random.randint(1, 100)
                st.session_state.attempts = 0
                st.rerun()
        elif guess < st.session_state.random_number:
            st.warning("Too low! Try a higher number.")
        else:
            st.warning("Too high! Try a lower number.")

def custom_range_guesser():
    """Task 2: Custom range number guessing game implementation."""
    st.subheader("Custom Range Number Guesser")
    
    col1, col2 = st.columns(2)
    with col1:
        min_val = st.number_input("Minimum value:", value=1)
    with col2:
        max_val = st.number_input("Maximum value:", value=100)
    
    if min_val >= max_val:
        st.error("Maximum value must be greater than minimum value!")
        return
    
    guess = st.number_input("Enter your guess:", min_value=min_val, max_value=max_val)
    
    if 'custom_number' not in st.session_state:
        st.session_state.custom_number = random.randint(min_val, max_val)
    
    if st.button("Submit Guess"):
        if guess == st.session_state.custom_number:
            st.success("🎉 Congratulations! You got it!")
            if st.button("Play Again"):
                st.session_state.custom_number = random.randint(min_val, max_val)
                st.rerun()
        elif guess < st.session_state.custom_number:
            st.warning("Too low! Try a higher number.")
        else:
            st.warning("Too high! Try a lower number.")

def password_strength_checker():
    """Task 3: Password strength checker implementation."""
    st.subheader("Password Strength Checker")
    
    password = st.text_input("Enter a password:", type="password")
    if password:
        strength, feedback = check_password_strength(password)
        
        st.write("\n".join(feedback))
        
        col1, col2, col3 = st.columns(3)
        if strength < 2:
            with col1:
                st.error("Weak Password")
        elif strength < 4:
            with col2:
                st.warning("Medium Password")
        else:
            with col3:
                st.success("Strong Password")

def fibonacci_sequence():
    """Task 4: Fibonacci sequence generator implementation."""
    st.subheader("Fibonacci Sequence Generator")
    
    terms = st.number_input("Enter number of terms:", min_value=1, max_value=100, value=10, step=1)
    if st.button("Generate Sequence"):
        sequence = generate_fibonacci(terms)
        
        st.write(f"Fibonacci sequence up to {terms} terms:")
        st.write(sequence)
        
        # Visualize the sequence
        st.line_chart(sequence)

def word_counter():
    """Task 5: File word counter implementation."""
    st.subheader("File Word Counter")
    
    uploaded_file = st.file_uploader("Choose a text file", type=['txt'])
    
    if uploaded_file is not None:
        content = uploaded_file.getvalue().decode("utf-8")
        word_count, top_words = analyze_text_file(content)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Word Count Results:")
            for word, count in word_count.items():
                st.write(f"'{word}': {count}")
        
        with col2:
            st.write("Top 10 Most Common Words")
            if word_count:
                st.bar_chart(top_words)
