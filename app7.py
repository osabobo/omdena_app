
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
DATA_URL = ('nga_lga_zonal_statistics_2016.csv')

st.title('Display table of the dataset of Night time spot in Nigeria')
data = pd.read_csv(DATA_URL)
df = pd.DataFrame({'lat': data['Latitude'], 'lon': data['Longitude']})
st.write(data)
df1=df.values.tolist()
options = [i for i in df1]
selected_stock=st.selectbox("Select the Latitude and Longitude  so that you can identify the location and use the plus and minus sign on the map to zoom",options)
def map_h(line):
    # center on Liberty Bell
    m = folium.Map(line, zoom_start=9)
    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
          line, popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
map_h(selected_stock)
