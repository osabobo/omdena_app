
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import json
st.set_page_config(layout="wide")
json1= f'nigeria_geojson.geojson'
DATA_URL= f'Nighttime_and_population_data.csv'
st.title('Display table of the dataset of Night time spot in Nigeria')
data = pd.read_csv(DATA_URL)
st.write(data)
choice=["AREA","PERIMETER","Population"]
select_maps = st.sidebar.selectbox(
    "How do you want to see the data?",
    ("OpenStreetMap", "Stamen Terrain","Stamen Toner")
)
selected_stock=st.selectbox("Select the choice",choice)
def map_g():
    map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()],tiles=select_maps, zoom_start=6, control_scale=True,)
    folium.Choropleth(geo_data=json1,name="choropleth",data=data,columns=['state',selected_stock],key_on="feature.properties.state", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name=selected_stock).add_to(map)
    folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',Name='state',popup=folium.features.GeoJsonPopup(fields=['state'])).add_to(map)
    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["state"]).add_to(map)
    folium_static(map,width=1000, height=700)
map_g()
