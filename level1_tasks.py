"""Level 1 tasks for the Python Learning Dashboard."""
import streamlit as st

def string_reversal():
    """Task 1: String reversal implementation."""
    st.subheader("String Reversal")
    text = st.text_input("Enter a string to reverse:")
    if text:
        reversed_text = text[::-1]
        st.success(f"Reversed string: {reversed_text}")

def temperature_conversion():
    """Task 2: Temperature conversion implementation."""
    st.subheader("Temperature Conversion")
    col1, col2 = st.columns(2)
    
    with col1:
        celsius = st.number_input("Enter Celsius temperature:", value=0.0)
        if st.button("Convert to Fahrenheit"):
            fahrenheit = (celsius * 9/5) + 32
            st.success(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    with col2:
        fahrenheit = st.number_input("Enter Fahrenheit temperature:", value=32.0)
        if st.button("Convert to Celsius"):
            celsius = (fahrenheit - 32) * 5/9
            st.success(f"{fahrenheit}°F = {celsius:.2f}°C")

def email_validator():
    """Task 3: Email validation implementation."""
    st.subheader("Email Validator")
    email = st.text_input("Enter an email address:")
    if email:
        # Simple email validation
        if '@' in email and '.' in email.split('@')[1]:
            st.success("Valid email address! ✅")
        else:
            st.error("Invalid email address! ❌")

def calculator():
    """Task 4: Calculator implementation."""
    st.subheader("Simple Calculator")
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        num1 = st.number_input("First number:", value=0.0)
    with col2:
        operation = st.selectbox("Operation", ["+", "-", "*", "/"])
    with col3:
        num2 = st.number_input("Second number:", value=0.0)
    
    if st.button("Calculate"):
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            else:  # division
                if num2 == 0:
                    st.error("Cannot divide by zero!")
                    return
                result = num1 / num2
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

def palindrome_checker():
    """Task 5: Palindrome checker implementation."""
    st.subheader("Palindrome Checker")
    text = st.text_input("Enter a word or phrase:")
    if text:
        # Remove spaces and convert to lowercase
        cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
        is_palindrome = cleaned_text == cleaned_text[::-1]
        
        if is_palindrome:
            st.success(f"'{text}' is a palindrome! ✅")
        else:
            st.error(f"'{text}' is not a palindrome. ❌")
