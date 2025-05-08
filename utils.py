"""Utility functions for the Python Learning Dashboard."""
import string

def check_password_strength(password: str) -> tuple[int, list[str]]:
    """
    Check the strength of a password and return feedback.
    
    Args:
        password (str): The password to check
        
    Returns:
        tuple[int, list[str]]: A tuple containing the strength score and feedback messages
    """
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength += 1
        feedback.append("✅ Length is 8 or more characters")
    else:
        feedback.append("❌ Should be at least 8 characters")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        strength += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Should contain uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        strength += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Should contain lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        strength += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Should contain numbers")
    
    # Check for special characters
    if any(c in string.punctuation for c in password):
        strength += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Should contain special characters")
    
    return strength, feedback

def generate_fibonacci(n: int) -> list[int]:
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list[int]: List containing the Fibonacci sequence
    """
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

def analyze_text_file(content: str) -> tuple[dict, dict]:
    """
    Analyze word frequency in a text file.
    
    Args:
        content (str): Text content to analyze
        
    Returns:
        tuple[dict, dict]: A tuple containing all word counts and top 10 words
    """
    words = content.lower().split()
    word_count = {}
    
    for word in words:
        word = word.strip('.,!?()[]{}":;')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    # Get top 10 words
    top_words = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10])
    
    return dict(sorted(word_count.items())), top_words
