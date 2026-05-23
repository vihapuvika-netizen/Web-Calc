import streamlit as st

# Set page title and custom tab icon
st.set_page_config(
    page_title="Stunning Python Calculator",
    page_icon="🧮",
    layout="centered"
)

# inject custom CSS for a modern, glassmorphism design with Cyberpunk theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    /* Styling the main container */
    .stApp {
        background: linear-gradient(135deg, #0d081b 0%, #06040a 100%);
        color: #f5f5fa;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Title container styling */
    .title-container {
        text-align: center;
        padding: 2rem 0;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(to right, #ff007f, #00f0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-family: 'Poppins', sans-serif;
    }
    .subtitle {
        color: #8a8a9e;
        font-size: 1.1rem;
        letter-spacing: 1px;
    }
    
    /* Modern styling for streamlit widgets */
    div.stNumberInput > label, div.stSelectbox > label {
        color: #ff007f !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Style the input wrapper container to be solid white */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid rgba(255, 0, 127, 0.4) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #00f0ff !important;
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.5) !important;
    }
    
    /* Style the input field text to be solid black */
    input {
        background-color: transparent !important;
        color: #000000 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600 !important;
    }
    
    /* Style the step buttons (+ and -) to be readable */
    div.stNumberInput button {
        background-color: #f0f2f6 !important;
        color: #000000 !important;
        border: none !important;
    }
    div.stNumberInput button:hover {
        background-color: #ff007f !important;
        color: #ffffff !important;
    }
    
    /* Select dropdown styling to be white background with black text */
    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid rgba(255, 0, 127, 0.4) !important;
        border-radius: 8px !important;
    }
    
    /* Ensure dropdown text is black */
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 500 !important;
    }
    
    /* Style the dropdown list popover and options */
    ul[role="listbox"] {
        background-color: #ffffff !important;
        border: 1px solid rgba(255, 0, 127, 0.4) !important;
    }
    li[role="option"] {
        background-color: transparent !important;
        color: #000000 !important;
        font-family: 'Poppins', sans-serif !important;
    }
    li[role="option"]:hover, li[role="option"][aria-selected="true"] {
        background-color: #ff007f !important;
        color: #ffffff !important;
    }
    
    /* Result card styling */
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }
    .result-label {
        font-size: 1rem;
        color: #ff007f;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }
    .result-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00f0ff;
        margin-top: 0.5rem;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.6);
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Custom header structure using semantic HTML
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">Modern Web Calculator</h1>
        <p class="subtitle">Built with Python & Streamlit</p>
    </div>
""", unsafe_allow_html=True)

# Define calculation logic functions (exactly like our command line version)
def calculate(num1, num2, operation):
    if operation == "Addition (+)":
        return num1 + num2
    elif operation == "Subtraction (-)":
        return num1 - num2
    elif operation == "Multiplication (*)":
        return num1 * num2
    elif operation == "Division (/)":
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    return 0

# Create simple layout columns for inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0, step=1.0, format="%f")

with col2:
    num2 = st.number_input("Second Number", value=0.0, step=1.0, format="%f")

# Let user choose operations via a sleek dropdown
operation = st.selectbox(
    "Choose Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# Perform calculation
result = calculate(num1, num2, operation)

# Display the result in our custom styled glassmorphism container
st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Result</div>
        <div class="result-value">{result}</div>
    </div>
""", unsafe_allow_html=True)
