import streamlit as st
import random
import string
import os

# Page config
st.set_page_config(
    page_title="Python Learning Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 1rem;
    }
    
    /* Header styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
    
    .level-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    
    .user-name {
        font-size: 1.2rem;
        color: #2c3e50;
    }
    
    /* Card styling */
    .task-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
        cursor: pointer;
    }
    
    .task-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    
    .task-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .task-description {
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Task content styling */
    .task-content {
        background-color: white;
        padding: 2rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton button {
        background-color: #1f77b4;
        color: white;
        border-radius: 0.3rem;
        padding: 0.5rem 1rem;
        width: 100%;
    }
    
    .stButton button:hover {
        background-color: #1565c0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'current_task' not in st.session_state:
    st.session_state.current_task = None

# Sidebar
with st.sidebar:
    st.title("Intership Project")
    level = st.selectbox("Select Level", ["Level 1", "Level 2", "Level 3"])

# Header
st.markdown(f"""
<div class="header-container">
    <div class="level-title">{level}</div>
    <div class="user-name">Janvi Singh</div>
</div>
""", unsafe_allow_html=True)

# Task descriptions
task_descriptions = {
    "Level 1": {
        "Task 1: String Reversal": "Reverse any input string with this simple tool",
        "Task 2: Temperature Conversion": "Convert between Celsius and Fahrenheit",
        "Task 3: Email Validator": "Check if an email address is valid",
        "Task 4: Calculator": "Perform basic mathematical operations",
        "Task 5: Palindrome Checker": "Check if a word or phrase is a palindrome"
    },
    "Level 2": {
        "Task 1: Guessing Game": "Guess the number between 1 and 100",
        "Task 2: Number Guesser": "Custom range number guessing game",
        "Task 3: Password Strength Checker": "Check how strong your password is",
        "Task 4: Fibonacci Sequence": "Generate and visualize Fibonacci sequence",
        "Task 5: File Word Counter": "Count and analyze words in a text file"
    }
}

def show_task_content(task_name):
    st.markdown(f'<div class="task-content">', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Tasks"):
        st.session_state.current_task = None
        st.rerun()
    
    if level == "Level 1":
        if "String Reversal" in task_name:
            st.subheader("String Reversal")
            text = st.text_input("Enter a string to reverse:")
            if text:
                reversed_text = text[::-1]
                st.success(f"Reversed string: {reversed_text}")
        
        elif "Temperature Conversion" in task_name:
            st.subheader("Temperature Conversion")
            col1, col2 = st.columns(2)
            with col1:
                temp = st.number_input("Enter temperature:", value=0.0)
            with col2:
                unit = st.selectbox("Select unit:", ["Celsius", "Fahrenheit"])
            if st.button("Convert"):
                if unit == "Celsius":
                    result = (temp * 9/5) + 32
                    st.success(f"{temp}°C = {result:.2f}°F")
                else:
                    result = (temp - 32) * 5/9
                    st.success(f"{temp}°F = {result:.2f}°C")
        
        elif "Email Validator" in task_name:
            st.subheader("Email Validator")
            email = st.text_input("Enter an email address:")
            if email:
                if "@" in email and "." in email:
                    st.success("Valid email address!")
                else:
                    st.error("Invalid email address!")
        
        elif "Calculator" in task_name:
            st.subheader("Calculator")
            col1, col2, col3 = st.columns([2,1,2])
            with col1:
                num1 = st.number_input("First number:", value=0.0)
            with col2:
                operator = st.selectbox("", ["+", "-", "*", "/"])
            with col3:
                num2 = st.number_input("Second number:", value=0.0)
            if st.button("Calculate"):
                try:
                    if operator == "+":
                        result = num1 + num2
                    elif operator == "-":
                        result = num1 - num2
                    elif operator == "*":
                        result = num1 * num2
                    elif operator == "/" and num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Error: Division by zero"
                    st.success(f"Result: {result}")
                except:
                    st.error("Error in calculation")
        
        elif "Palindrome" in task_name:
            st.subheader("Palindrome Checker")
            text = st.text_input("Enter text to check:")
            if text:
                cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
                is_palindrome = cleaned_text == cleaned_text[::-1]
                if is_palindrome:
                    st.success(f"'{text}' is a palindrome!")
                else:
                    st.error(f"'{text}' is not a palindrome!")
    
    elif level == "Level 2":
        if "Guessing Game" in task_name:
            st.subheader("Guessing Game")
            st.info("Try to guess the number between 1 and 100!")
            
            guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Make Guess"):
                    st.session_state.attempts += 1
                    if guess == st.session_state.random_number:
                        st.balloons()
                        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
                    elif guess < st.session_state.random_number:
                        st.warning("Too low! Try a higher number.")
                    else:
                        st.warning("Too high! Try a lower number.")
            with col2:
                if st.button("New Game"):
                    st.session_state.random_number = random.randint(1, 100)
                    st.session_state.attempts = 0
                    st.rerun()
        
        elif "Password Strength" in task_name:
            st.subheader("Password Strength Checker")
            password = st.text_input("Enter a password:", type="password")
            if password:
                strength = 0
                feedback = []
                
                if len(password) >= 8:
                    strength += 1
                    feedback.append("✅ Length is 8 or more characters")
                else:
                    feedback.append("❌ Password should be at least 8 characters")
                
                if any(c.isupper() for c in password):
                    strength += 1
                    feedback.append("✅ Contains uppercase letters")
                else:
                    feedback.append("❌ Should contain uppercase letters")
                
                if any(c.islower() for c in password):
                    strength += 1
                    feedback.append("✅ Contains lowercase letters")
                else:
                    feedback.append("❌ Should contain lowercase letters")
                
                if any(c.isdigit() for c in password):
                    strength += 1
                    feedback.append("✅ Contains numbers")
                else:
                    feedback.append("❌ Should contain numbers")
                
                if any(c in string.punctuation for c in password):
                    strength += 1
                    feedback.append("✅ Contains special characters")
                else:
                    feedback.append("❌ Should contain special characters")
                
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
        
        elif "Fibonacci" in task_name:
            st.subheader("Fibonacci Sequence Generator")
            terms = st.number_input("Enter number of terms:", min_value=1, max_value=100, value=10, step=1)
            if st.button("Generate Sequence"):
                sequence = [0, 1]
                for i in range(2, terms):
                    sequence.append(sequence[i-1] + sequence[i-2])
                
                st.write(f"Fibonacci sequence up to {terms} terms:")
                st.write(sequence[:terms])
                
                # Visualize the sequence
                st.line_chart(sequence[:terms])
        
        elif "File Word Counter" in task_name:
            st.subheader("File Word Counter")
            uploaded_file = st.file_uploader("Choose a text file", type=['txt'])
            
            if uploaded_file is not None:
                content = uploaded_file.getvalue().decode("utf-8")
                words = content.lower().split()
                word_count = {}
                
                for word in words:
                    word = word.strip('.,!?()[]{}":;')
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Word Count Results:")
                    sorted_words = dict(sorted(word_count.items()))
                    for word, count in sorted_words.items():
                        st.write(f"'{word}': {count}")
                
                with col2:
                    st.write("Top 10 Most Common Words")
                    if word_count:
                        top_words = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10])
                        st.bar_chart(top_words)

    st.markdown('</div>', unsafe_allow_html=True)

# Main content
if st.session_state.current_task is None:
    st.write("### Available Tasks")
    cols = st.columns(3)
    tasks = task_descriptions.get(level, {}).items()
    for i, (task_name, description) in enumerate(tasks):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="task-card">
                <div class="task-title">{task_name}</div>
                <div class="task-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Open Task", key=f"btn_{task_name}"):
                st.session_state.current_task = task_name
                st.rerun()
else:
    show_task_content(st.session_state.current_task)
