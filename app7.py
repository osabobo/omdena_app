
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
DATA_URL = ('nga_lga_zonal_statistics_2016.csv')

st.title('Display table of the dataset of Night time spot in Nigeria')
data = pd.read_csv(DATA_URL)
def map_g():
    map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=6, control_scale=True)
    for index, c in data.iterrows():
        folium.Marker([c['Latitude'], c['Longitude']], popup=c["STATE"]).add_to(map)
    folium_static(map)
map_g()
df = pd.DataFrame({'lat': data['Latitude'], 'lon': data['Longitude']})
st.write(data)
df1=df.values.tolist()
options = [i for i in df1]
selected_stock=st.selectbox("Select the Latitude and Longitude  so that you can identify the location and use the plus and minus sign on the map to zoom",options)
def map_h(line):
    # center on Liberty Bell
    m = folium.Map(line, zoom_start=6)
    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
          line, popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
map_h(selected_stock)
