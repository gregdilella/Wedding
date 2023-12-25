import streamlit as st
from streamlit_extras.let_it_rain import rain

st.title("About Us")

def run_snow_animation():
    rain(emoji="❤️", font_size=20, falling_speed=5, animation_length="infinite")


run_snow_animation()