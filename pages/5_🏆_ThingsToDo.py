import streamlit as st
import pandas as pd
import base64
def get_image_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def add_logo():
    logo_base64 = get_image_as_base64('assets/5mYgrm-LogoMakr.png')
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{logo_base64}");
                background-repeat: no-repeat;
                padding-top: 180px;

                background-position: 20px 20px;
            }}

        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()

st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        
        /* Setting a general font size for all specified elements */
        h1, h2, p, div, span, a {
            font-family: 'Alex Brush', cursive;
            font-size: 24px; /* General size for demonstration */
        }

        /* You can also specify different sizes for different elements */
        h1 {
            font-size: 36px; /* Larger size for h1 */
        }
        h2 {
            font-size: 30px; /* Slightly smaller size for h2 */
        }
        p {
            font-size: 24px; /* Size for paragraphs */
        }
        </style>
        """, unsafe_allow_html=True)

add_logo()

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
        "<a href='https://mandys.ca/en/signature-salads/'>The Wolfe</a>",
        "<a href='https://www.atwatercocktailclub.com/'>Atwater Cocktail Club</a>",
        "<a href='https://www.vicstudios.ca/'>Pilates</a>"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)
st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        
        /* Set the font size for all specified elements */
        html, body, div, span, app, .block-container * {
            font-family: 'Alex Brush', cursive;
    
        }
        
        /* Larger font size for headers and subheaders */
        h1, h2 {
            font-size: 30px;
        }
        </style>
        <h1 style =\font-size: 24px; padding: 40px;\>Things To Do</h1>
        """, unsafe_allow_html=True)


# Function to apply markdown with color, bold text, and handwriting style font
def colored_bold_handwriting_text(text, color):
    return f"<span style=\"color:{color}; font-weight:bold;\">{text}</span>"

# Function to center and format the category header with handwriting style font
def centered_category(category):
    return f"<h2 style=\"text-align: left; font-size: 30px; padding: 40px;\">{category}</h2>"

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
