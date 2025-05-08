"""CSS styles for the Python Learning Dashboard."""

CUSTOM_CSS = """
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
"""
