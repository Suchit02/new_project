"""Main application file for the Python Learning Dashboard."""
import streamlit as st
import random

# Import local modules
from config import TASK_DESCRIPTIONS, PAGE_CONFIG, USER_NAME
from styles import CUSTOM_CSS
from level1_tasks import (
    string_reversal,
    temperature_conversion,
    email_validator,
    calculator,
    palindrome_checker
)
from level2_tasks import (
    guessing_game,
    custom_range_guesser,
    password_strength_checker,
    fibonacci_sequence,
    word_counter
)

# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'current_task' not in st.session_state:
    st.session_state.current_task = None

# Sidebar
with st.sidebar:
    st.title("Python Learning Dashboard")
    level = st.selectbox("Select Level", ["Level 1", "Level 2"])

# Header
st.markdown(
    f"""
    <div class="header-container">
        <div class="level-title">{level}</div>
        <div class="user-name">{USER_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True
)

def show_task_content(task_name: str) -> None:
    """Display the content for the selected task.
    
    Args:
        task_name (str): Name of the selected task
    """
    st.markdown(f'<div class="task-content">', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Tasks"):
        st.session_state.current_task = None
        st.rerun()
    
    # Level 1 tasks
    if level == "Level 1":
        if "String Reversal" in task_name:
            string_reversal()
        elif "Temperature Conversion" in task_name:
            temperature_conversion()
        elif "Email Validator" in task_name:
            email_validator()
        elif "Calculator" in task_name:
            calculator()
        elif "Palindrome" in task_name:
            palindrome_checker()
    
    # Level 2 tasks
    else:
        if "Guessing Game" in task_name:
            guessing_game()
        elif "Number Guesser" in task_name:
            custom_range_guesser()
        elif "Password Strength" in task_name:
            password_strength_checker()
        elif "Fibonacci" in task_name:
            fibonacci_sequence()
        elif "File Word Counter" in task_name:
            word_counter()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main content
if st.session_state.current_task is None:
    st.write("### Available Tasks")
    cols = st.columns(3)
    tasks = TASK_DESCRIPTIONS.get(level, {}).items()
    
    # Display task cards
    for i, (task_name, description) in enumerate(tasks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="task-card">
                    <div class="task-title">{task_name}</div>
                    <div class="task-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Open Task", key=f"btn_{task_name}"):
                st.session_state.current_task = task_name
                st.rerun()
else:
    show_task_content(st.session_state.current_task)
