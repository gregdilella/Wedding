import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import pandas as pd
from pathlib import Path
import json
import datetime
from pathlib import Path

st.set_page_config(page_title="Lisa and Greg", page_icon="⚭")

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
        </style>
        <h1 style="font-family:'Alex Brush', cursive;">Lisa and Greg's Wedding Portal</h1>
        """, unsafe_allow_html=True)

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "WhatsAppVideo.json"
LOGO = ASSETS / "5xUEXG-LogoMakr.png"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)

col1, col2 = st.columns(2)

# Place the Lottie animation in the first column
with col1:
    # st.subheader("You're Invited to Our Wedding Celebration!")
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        </style>
        <div style="font-size: 24px; font-family:'Alex Brush', cursive;">
        We are thrilled to announce a very special day in our lives and would be honored to have you join us in celebration.  Mark your calendars for the 29th of June 2024, at the Mount Stephen!
        </div>""", unsafe_allow_html=True)


def get_video_base64(video_path):
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode()
# Convert your video to base64
video_base64 = get_video_base64('assets/WhatsAppVideo.mp4')
# Place the subheader and markdown in the second column

from PIL import Image, ImageDraw, ImageOps
imagewedding = Image.open('assets/wedding1.jpeg')
# Define the function to round the corners of an image
def round_corners(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + image.size, radius, fill=255)
    rounded_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)
    return rounded_image

# Apply the round corners function with a specified radius
rounded_imagewedding = round_corners(imagewedding, radius=50) # Adjust radius as needed

# Display the image in col2 with a specified width of 300
with col2:
    st.image(rounded_imagewedding, width=300)


st.markdown('<br><br>', unsafe_allow_html=True)


st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        </style>
        <div style="font-size: 24px; font-family:'Alex Brush', cursive;">
        We promise an evening of great company, delicious food, and a lively celebration.
        Please RSVP by filling out the form below to confirm your attendance. Also check out the other pages in the sidebar!
        </div>""", unsafe_allow_html=True)


st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        </style>
        <h1 style="font-family:'Alex Brush', cursive;">RSVP</h1>
        """, unsafe_allow_html=True)



conn = st.connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(worksheet="Responses", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

YES_NO = [
    "YES",
    "NO",
]



st.markdown("""
            <style>
            /* Apply font size to general elements */
            html, body, div, span, app, .block-container * {
                font-size: 26px !important;
            }
            /* Specific adjustments might be needed for input and textarea elements */
            input, textarea, select, button {
                font-size: 24px !important;
            }
            </style>
            """, unsafe_allow_html=True)

# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    
    Name = st.text_input(label="Name*")
    Attending = st.radio("Are You Planning On Coming?*",[":green[Yes]", ":red[No]"],index=None,horizontal=True)
    # Attending = st.selectbox("Are You Planning On Coming?*", options=YES_NO, index=None)
    NumberOfParty = st.slider("How Many People Are In Your Party?*", 1, 5, 1)
    MealRestriction = st.text_area(label="Do You Have Any Meal Restrictions?    If Yes, Please Describe Them Here.",height=50)
    additional_info = st.text_area(label="Additional Info", height=50)

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Form")

    # If the submit button is pressed
    if submit_button:
        # Check if all mandatory fields are filled
        if not Attending or not Name:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        else:
            # Create a new row of data
            new_data = {
                "Name": Name,
                "Attending": Attending,
                "Number": NumberOfParty,
                "Meal": MealRestriction,
                "Notes": additional_info,
                "Time": datetime.datetime.now()  # Assign the timestamp only here
            }

            # Add the new data to the existing DataFrame
            updated_df = existing_data.append(new_data, ignore_index=True)

            # Update Google Sheets with the new data
            conn.update(worksheet="Responses", data=updated_df)

            if Attending == ":red[No]":
                st.warning(f"Sorry you can't make it, {Name}!")
            elif Attending == ":green[Yes]":
                st.success(f"Looking forward to seeing you there, {Name}!")


st.markdown("""
            <div style="font-size: 24px; font-family:'Alex Brush', cursive;">
            Parking in downtown Montreal can be difficult. 
            There is a parking lot (Superior Parking located at 1414 Drummond street), adjacent to Mount Stephen's, but spots are limited and cannot be guaranteed.
            Please plan accordingly and consider taking an Uber/Taxi for a better experience.
            </div>""", unsafe_allow_html=True)