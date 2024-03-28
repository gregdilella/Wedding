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
        
        h1, h2, p, div, span, a {
            font-family: 'Alex Brush', cursive;
        }
        </style>
        """, unsafe_allow_html=True)


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
with col2:
    
    st.markdown(f"""
        <video width="auto" height="300" controls>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """, unsafe_allow_html=True)


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

options = [
    "","Ian and Leila Henriques", "Meagan and Michalis Iriotakis",
    "Kerri Henriques and Aymen Djellal", "Neela, Darren and Valerie Pymento",
    "Sharon Pymento", "Erica Street", "Emma Street", "Neil Henriques",
    "Tina Iriotakis and Gianni Ciliberto", "Karl Henriques",
    "Max Gaudette and Judith Darmon", "Albert and Regine Hadida",
    "Arthur Pereira", "Alwyn and Marjorie Rapose", "Melinda and Celso Furtado",
    "Marian and Carl Fernandes", "Vivianne Lapointe and Damien Auger", "Ali Siddiquee",
    "Mary Quiroz", "Nadia Monczak and Benjamin Deschamps",
    "Gabrielle Bibas and Tomer Zazkis", "Michelle Chitayat and Kenneth Kunin",
    "Patrick Moynihan and Guillaume Labelle", "Natela Baron Goldman and Eric Perruclet",
    "John Di Lella and Sandy Gasparini", "Valerie Di Lella and Drew Nicholson",
    "Bill, Natasha, Chelsey and Victoria Campbell", "Gino Di Lella", "Mike Di Lella",
    "Joe and Rita Di Lella", "Lauren Di Lella", "James Di Lella and Elyse Champagne",
    "Laura Piro and Lino Iaizzo", "Lina Iaciofano and Tony Discenza",
    "Pasqualino and Maria Iaciofano", "Mary Fantacone and Tony Filiatrault",
    "Flora Fantacone and Jimmy Gianopoulos", "Mary Romano and Joe Iaricci",
    "Nick and Connie Primiano", "Steve Knezevic and Linda Dolnik",
    "John and Patsy Patone", "Maurice and Amy Conti", "Zsolt Szigetvari and Maggie Lettuca",
    "Tyler Ehler and Angeline Darses", "Michael Baslyk", "Martin Antonov Spasov",
    "William and Ashley McLaughlin", "Christina Pantuso and Tim Schiavi",
    "Carolyn De Luca and James Lavinskas", "Lisa Pico and Richard Ribaya",
    "Christine Mangione and Daniel Laplante", "Wendy Duran and Ben Ross",
    "Raquel Ferdinand and Dylan Pearson", "Alicia Schiavi and David Del Re",
    "Savina Caporali", "Victoria D'Alessandro", "Stefanie Fontana",
    "AJ Dopud", "Yohan Henriques and Mara De Simone", "Peter and Zoe Iriotakis",
    "Nadia, Mohammed and Ines Djellal", "Roger, Donna, Matthew and Brian Henriques",
    "Jude Netto", "Nicola and Jonathan White", "Sonya and Sebastian Pereira",
    "Eva Paylan", "Mariam and Ji Song", "Mervyn and Cynthia Pereira",
    "Caryl and Gerard Pinto", "Tim and Mary Kougias", "Khac Minh Nguyen",
    "Sayeh Davoudi and Alex Marcakis", "Karis Cheung", "Atefa Jaffari",
    "Sarah Monsonego and Josh Benchetrit", "Madonna Tamoeva and Paul Budhiraja",
    "Rosie Faucher and Hugo Potvin", "Slobodan Milosevic", "Michel Marleau",
    "Serghei Bucatel", "Linda Campbell", "Pamela and Ed Piro", "Manuela Lombardi",
    "Claudio and Angela Di Lella", "Benito and Elvira Garzia", "Tony and Marise Romano",
    "Nick and Carmen Pallotta", "Stella and Agostino Mariani", "Matthew Miller",
    "Shaun and Jillian McLaughlin", "Steve Haraschak", "Samantha Taran and Matthew Chausse",
    "Etienne Goulet Lang", "Nik-ki and Mike Street", "Vinita, Raminder, Rahul and Ramon Singh",
    "Jal and Nergish Panthaki", "Giovanni and Federica Di Lella", "Keif Orsini"
]




# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    
    Name = st.selectbox(label="Name*", options=options)
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


 