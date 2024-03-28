import streamlit as st
import pandas as pd

# Data
data = {
    "Category": ["Brunch", "Mandy's Salad", "Drinks", "Exercise"],
    "Greg": [
        "<a href='https://www.bossa.ca/menu'>Bossa Sandwich</a>",
        "<a href='https://mandys.ca/en/signature-salads/'>Crunchy Sesame</a>",
        "<a href='https://www.philemonbar.com/'>Philemon</a>",
        "<a href='https://h2oma.com/'>Fight Gym</a>"
    ],
    "Lisa": [
        "<a href='https://arthursmtl.com/'>Arthurs</a>",
        "<a href='https://mandys.ca/en/signature-salads/'>The Wolf</a>",
        "<a href='https://www.atwatercocktailclub.com/'>Atwater Cocktail Club</a>",
        "<a href='https://www.vicstudios.ca/'>Pilates</a>"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Start of Streamlit app
st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        
        h1, h2, span, a {
            font-family: 'Alex Brush', cursive;
        }
        </style>
        <h1>Things To Do</h1>
        """, unsafe_allow_html=True)

# Function to apply markdown with color, bold text, and handwriting style font
def colored_bold_handwriting_text(text, color):
    return f"<span style=\"color:{color}; font-weight:bold;\">{text}</span>"

# Function to center and format the category header with handwriting style font
def centered_category(category):
    return f"<h2 style=\"text-align: left;\">{category}</h2>"

# Iterate over the DataFrame rows and display category and preferences
for index, row in df.iterrows():
    # Center the category header
    st.markdown(centered_category(row['Category']), unsafe_allow_html=True)
    
    # Create two columns for Greg and Lisa's choices
    col1, col2 = st.columns(2)
    
    with col1:
        # Apply the markdown with HTML for Greg's choices in dark green
        greg_text = colored_bold_handwriting_text("Greg's choice:", "darkgreen") + f"<br>{row['Greg']}"
        st.markdown(greg_text, unsafe_allow_html=True)
        
    with col2:
        # Apply the markdown with HTML for Lisa's choices in blush (using a hex code)
        lisa_text = colored_bold_handwriting_text("Lisa's choice:", "#ff758c") + f"<br>{row['Lisa']}"
        st.markdown(lisa_text, unsafe_allow_html=True)
