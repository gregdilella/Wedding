import streamlit as st
from streamlit_extras.let_it_rain import rain

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

st.title("The Proposal")

def run_snow_animation():
    rain(emoji="🍁", font_size=50, falling_speed=4, animation_length=1)
run_snow_animation()


# st.image("assets/prop1.png", caption='The day I asked Lisa to Marry Me', use_column_width=True)

from PIL import Image, ImageDraw

def add_rounded_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w,h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

# Load your image
image_path = "assets/prop1.png"
image = Image.open(image_path)


# Add rounded corners (adjust radius as needed)
radius = 50  # radius of the rounded corners
rounded_image = add_rounded_corners(image.convert("RGBA"), radius)

# Display the image
st.image(rounded_image, caption='The day I Asked Lisa To Marry Me', use_column_width=True)



st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown("""
            &nbsp;&nbsp;&nbsp;&nbsp;On a crisp, sunny fall afternoon, we dog walked through the nearby park, as we approached our favourite spot, I felt my heart pounding with a mix of excitement and nervous anticipation. With a deep breath, I turned to her, the love of my life, and with words woven from the deepest fibers of my heart, I proposed. Unbeknownst to her, our friends, like skillful ninjas, were discreetly nestled behind trees and bushes, cameras at the ready, capturing the moment her surprise turned to tears.""")
st.markdown('<br><br>', unsafe_allow_html=True)

image_path = "assets/knee.png"
image = Image.open(image_path)


# Add rounded corners (adjust radius as needed)
radius = 50  # radius of the rounded corners
rounded_image = add_rounded_corners(image.convert("RGBA"), radius)

# Display the image
st.image(rounded_image, caption='Actual Photo', use_column_width=True)

st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown("""    &nbsp;&nbsp;&nbsp;&nbsp;Lisa shares my passion for dogs, finding joy in their enthusiasm and loyalty. Her love for reading opens windows to new worlds and ideas, inspiring endless conversations and learning. Family is her anchor, and she weaves its importance into the fabric of our lives. Travel with her is an adventure, not just in exploring new places but in discovering new depths in each other. Her ambition and drive make her an incredible partner; she's not just striving to reach her goals but also lifting me towards mine. In her, I have found not just a lover and my best friend, but a true partner in every sense of the word.

            """)
