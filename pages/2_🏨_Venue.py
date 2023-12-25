import streamlit as st

st.title("Le Mount Stephen")

address = "1440 Drummond Street, Montreal, Quebec H3G 1V9 Canada"

# Display the address in a box
st.info(address)


import streamlit as st
import pydeck as pdk

# Address to display
address = "1440 Drummond Street, Montreal, Quebec H3G 1V9 Canada"

embed_url = "https://30days.streamlit.app/?embed=true"

# Create two columns
col1, col2 = st.columns([0.9, 0.1])


# In the second column, create the copy button
with col2:
    st.markdown("""
        <button onclick="navigator.clipboard.writeText(`{}`)" style="float: right;">
            Copy
        </button>
    """.format(embed_url), unsafe_allow_html=True)



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
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=map_view))

st.markdown("""
The Mount Stephen Club in Montreal, initially established as a private gentlemen's club in 1926, is housed in a mansion built in 1880 for George Stephen, 1st Baron Mount Stephen. This building is a prominent example of Victorian-era architecture, reflecting the city's historical and cultural heritage. Over the years, it transitioned from a private residence to an exclusive club for Montreal's elite. It has been repurposed into a luxury boutique hotel, blending its historical essence with modern functionality.

George Stephen was a significant figure in Canadian history, primarily known for his role in the development of the Canadian Pacific Railway and as President of the Bank of Montreal. His contributions to Canada's economic and infrastructural development have left a lasting legacy, with the Mount Stephen mansion standing as a tangible reminder of his impact on Canadian society.""")