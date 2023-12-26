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

st.title("Lisa and Greg's Wedding Portal")


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
st_lottie(lottie_animation, key="lottie-holiday", height=500)


st.subheader("You Are Invited To Our Wedding!")

st.markdown("""
    <div style="font-size: 20px;">
    It's At 4pm On June 29th, At The Mount Stephen.<br><br>
    </div>
""", unsafe_allow_html=True)

# Form Prompt
st.write("Please fill out the form below to help us plan the event.")

conn = st.connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(worksheet="Responses", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

YES_NO = [
    "YES",
    "NO",
]


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