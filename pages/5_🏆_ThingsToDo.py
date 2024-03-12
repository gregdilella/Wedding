import streamlit as st
import pandas as pd

data = {
    "Category": ["Brunch", "Mandy's Salad", "Drinks", "Exercise"],
    "Greg": ["Bossa Sandwich", "Asian Dressing with Mandarins", "Philemon", "Fight Gym"],
    "Lisa": ["Arthurs", "Habibi", "Atwater Cocktail Club", "Pilates"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Start of Streamlit app
st.title('Things To Do')

# Function to apply markdown with color, bold text, and handwriting style font
def colored_bold_handwriting_text(text, color):
    # Ensure single and double quotes are used correctly here
    return f"<span style=\"color:{color}; font-weight:bold; font-family:'Great Vibes', cursive;\">{text}</span>"

# Function to center and format the category header with handwriting style font
def centered_category(category):
    # Ensure single and double quotes are used correctly here
    return f"<h2 style=\"text-align: left; font-family:'Great Vibes', cursive;\">{category}</h2>"

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
