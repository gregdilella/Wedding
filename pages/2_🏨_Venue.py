import streamlit as st


import base64
import pydeck as pdk

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

image_path = "assets/mtstephen.png"
image = Image.open(image_path)

# Add rounded corners (adjust radius as needed)
radius = 50  # radius of the rounded corners
rounded_image = add_rounded_corners(image.convert("RGBA"), radius)

embed_url = "https://30days.streamlit.app/?embed=true"

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

st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        
        p, div, span, a {
            font-family: 'Alex Brush', cursive;
            font-size: 24px;
        }
        </style>
        <h1>Le Mount Stephen</h1>
        <p>We are so excited to get married at the Mount Stephen. The venue is situated in the heart of Montreal, the city we call home. Here is some fun information on the history of the building and the man who it’s named after.</p>
        """, unsafe_allow_html=True)


# Display the image
st.image(rounded_image, caption='The Mount Stephen', use_column_width=True)
image_path = "assets/mtstephen.png"
image = Image.open(image_path)

# Add rounded corners (adjust radius as needed)
radius = 50  # radius of the rounded corners
rounded_image = add_rounded_corners(image.convert("RGBA"), radius)

address = "1440 Drummond Street, Montreal, Quebec H3G 1V9 Canada"





embed_url = "https://30days.streamlit.app/?embed=true"



# Coordinates for the address (latitude and longitude)
latitude = 45.4999
longitude = -73.5773

# Create a map using Pydeck
map_view = pdk.ViewState(latitude=latitude, longitude=longitude, zoom=15)
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"position": [longitude, latitude], "size": 100}],
    get_position="position",
    get_color=[255, 0, 0, 200],
    get_radius="size",
)


st.markdown('<br><br>', unsafe_allow_html=True)

def colored_bold_handwriting_text(text):
    return f"<span style=\"font-weight:bold; font-family:'Alex Brush', cursive; font-size: 22px;\">{text}</span>"

venue_text2 = colored_bold_handwriting_text("""
            The Mount Stephen Club in Montreal, initially established as a private gentlemen's club in 1926, is housed in a mansion built in 1880 for George Stephen. This building is a prominent example of Victorian-era architecture, reflecting the city's historical and cultural heritage. Over the years, it transitioned from a private residence to an exclusive club for Montreal's elite. It has been repurposed into a luxury boutique hotel, blending its historical essence with modern functionality.
            """)
st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        </style>
        """ + venue_text2, unsafe_allow_html=True)

st.markdown('<br><br>', unsafe_allow_html=True)

venue_text3 = colored_bold_handwriting_text("""
            George Stephen was a significant figure in Canadian history, primarily known for his role in the development of the Canadian Pacific Railway and as President of the Bank of Montreal. His contributions to Canada's economic and infrastructural development have left a lasting legacy, with the Mount Stephen mansion standing as a tangible reminder of his impact on Canadian society.
            """)
st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        </style>
        """ + venue_text3, unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)


# st.image("assets/mtstephen.png", caption='Le Mount Stephen', use_column_width=True)

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
st.code(address)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=map_view))

st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        
        p, div, span, a {
            font-family: 'Alex Brush', cursive;
            font-size: 24px;
        }
        </style>
        <h1>Accomodation</h1>
        
        """, unsafe_allow_html=True)

file_path = 'MountStephensRates.pdf'

# Read the PDF file in binary mode
with open(file_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Create a download button and offer the PDF as a download
st.download_button(
    label="Download Mount Stephens Rates",
    data=pdf_bytes,
    file_name="MountStephensRates.pdf",
    mime="application/pdf"
)


# Display the list of hotels
st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');

            .alex-brush-font {
                font-family: 'Alex Brush', cursive;
                font-size: 24px;
            }
            </style>
            """, unsafe_allow_html=True)

# Use HTML to apply the custom class for styling
st.markdown("""
            <h2 class="alex-brush-font">Here are a few other nearby options:</h2>
            <ul class="alex-brush-font">
                <li>The Four Seasons Hotel</li>
                <li>Vogue Hotel Montreal</li>
                <li>Le Centre Sheraton Montreal</li>
                <li>The Ritz-Carlton</li>
                <li>Hotel OMNI Montreal</li>
                <li>Le St-Martin Montreal</li>
            </ul>
            """, unsafe_allow_html=True)
