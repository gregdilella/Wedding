import streamlit as st
import os
st.title("Photos")

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


import os
from PIL import Image, ImageDraw
import streamlit as st

def add_rounded_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

# Directory containing the images
directory = "assets/gallery"
files = sorted(os.listdir(directory))

# Filter out six image files (assuming they are .png or .jpg)
image_files = [file for file in files if file.endswith(('.png', '.jpg'))][:6]

# Display the images with rounded corners
radius = 20  # Radius for the rounded corners
for image_file in image_files:
    image_path = os.path.join(directory, image_file)
    image = Image.open(image_path).convert("RGBA")
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)
