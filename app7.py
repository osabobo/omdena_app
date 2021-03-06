import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

st.set_page_config(layout="wide")
json1= f'nigeria_lga.json'
DATA_URL= f'low_intensity.csv'
DATA_URL1= f'moderately_low_intensity.csv'
DATA_URL2= f'medium_intensity.csv'
DATA_URL3= f'moderate_high_intensity.csv'
DATA_URL4= f'high_intensity.csv'
st.sidebar.title('Omdena Lagos, Nigeria')
st.sidebar.write('Omdena Lagos, Nigeria chapter is a part of Omdena that focuses on running open-source AI projects to solve challenges facing our local communities.')
from PIL import Image
image = Image.open('omdena_Nigeria.jpg')
st.sidebar.image(image)
#colors = ["orange", "yellow", "green", "blue"]
#choice=
select_maps = st.sidebar.selectbox(
    "How do you want to see the map ?",
    ("OpenStreetMap", "Stamen Terrain","Stamen Toner")

)
add_selectbox = st.sidebar.selectbox(
    "How would you like to view the intensity on map?",
    ("Low", "moderately low","medium intensity","moderate high intensity","high intensity"))
if add_selectbox == 'Low':
    data = pd.read_csv(DATA_URL)
    st.title('Omdena AI for Energy')
    def map_g():
        map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)

        folium.Choropleth(geo_data=json1,name="choropleth",data=data,columns=['LGA','population density'],key_on="feature.properties.LGA", fill_color='YlOrRd',
                           fill_opacity=0.9,
                           line_opacity=0.2,
                           legend_name='population density').add_to(map)
        #folium.LayerControl().add_to(map)
        #folium.Marker(
    #location=[data['Latitude'].mean(), data['Longitude'].mean()],
    #popup="Mt. Hood Meadows",
    #icon=folium.Icon(icon="cloud"),).add_to(map)



    # Add hover functionality.
        # square marker
        folium.features.GeoJson(
    'nigeria_lga.json',
    name="States",
    tooltip=folium.features.GeoJsonTooltip(fields=["LGA"]),
    popup=folium.features.GeoJsonPopup(fields=["LGA"]),
    #style_function=lambda x: {
        #"fillColor": colors[x['properties']['service_level']],
        #"radius": (x['properties']['lines_served'])*30,
    #},
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(map)
        #for index, c in data.iterrows():
            #folium.Marker([c['Latitude'], c['Longitude']],tooltip='square',icon=icon_square).add_to(map)

        folium_static(map,width=900, height=800)
    map_g()
if add_selectbox == 'moderately low':
    data1 = pd.read_csv(DATA_URL1)
    st.title('Omdena AI for Energy')
    def map_g1():
        map = folium.Map(location=[data1['Latitude'].mean(), data1['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data1,columns=['LGA','population density'],key_on="feature.properties.LGA", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='population density').add_to(map)
        #folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.
        folium.features.GeoJson(
    'nigeria_lga.json',
    name="States",
    tooltip=folium.features.GeoJsonTooltip(fields=["LGA"]),
    popup=folium.features.GeoJsonPopup(fields=["LGA"]),
    #style_function=lambda x: {
        #"fillColor": colors[x['properties']['service_level']],
        #"radius": (x['properties']['lines_served'])*30,
    #},
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(map)
    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=900, height=800)
    map_g1()
if add_selectbox == 'medium intensity':
    data2 = pd.read_csv(DATA_URL2)
    st.title('Omdena AI for Energy')
    def map_g2():
        map = folium.Map(location=[data2['Latitude'].mean(), data2['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        fortooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data2,columns=['LGA','population density'],key_on="feature.properties.LGA", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='population density').add_to(map)
        #folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.
        folium.features.GeoJson(
    'nigeria_lga.json',
    name="States",
    tooltip=folium.features.GeoJsonTooltip(fields=["LGA"]),
    popup=folium.features.GeoJsonPopup(fields=["LGA"]),
    #style_function=lambda x: {
        #"fillColor": colors[x['properties']['service_level']],
        #"radius": (x['properties']['lines_served'])*30,
    #},
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(map)
    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=900, height=800)
    map_g2()
if add_selectbox == 'moderate high intensity':
    data3 = pd.read_csv(DATA_URL3)
    st.title('Omdena AI for Energy')
    def map_g3():
        map = folium.Map(location=[data3['Latitude'].mean(), data3['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data3,columns=['LGA','population density'],key_on="feature.properties.LGA", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='population density').add_to(map)
        #folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.
        folium.features.GeoJson(
     'nigeria_lga.json',
     name="States",
     tooltip=folium.features.GeoJsonTooltip(fields=["LGA"]),
     popup=folium.features.GeoJsonPopup(fields=["LGA"]),
     #style_function=lambda x: {
         #"fillColor": colors[x['properties']['service_level']],
         #"radius": (x['properties']['lines_served'])*30,
     #},
     highlight_function=lambda x: {"fillOpacity": 0.8},
     zoom_on_click=True,
 ).add_to(map)
    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=900, height=800)
    map_g3()
if add_selectbox == 'high intensity':
    data4 = pd.read_csv(DATA_URL4)
    st.title('Omdena AI for Energy')
    def map_g4():
        map = folium.Map(location=[data4['Latitude'].mean(), data4['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data4,columns=['LGA','population density'],key_on="feature.properties.LGA", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='population density').add_to(map)
        #folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.
        folium.features.GeoJson(
    'nigeria_lga.json',
    name="States",
    tooltip=folium.features.GeoJsonTooltip(fields=["LGA"]),
    popup=folium.features.GeoJsonPopup(fields=["LGA"]),
    #style_function=lambda x: {
        #"fillColor": colors[x['properties']['service_level']],
        #"radius": (x['properties']['lines_served'])*30,
    #},
    highlight_function=lambda x: {"fillOpacity": 0.8},
    zoom_on_click=True,
).add_to(map)
    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=900, height=800)
    map_g4()
link = '[Nighttime Code ](https://github.com/OmdenaAI/omdena-nigeria-energy/blob/main/src/final%20deliverables/task/Nighttime_light/Earth%20Engine%20Master.ipynb)'
st.sidebar.markdown(link, unsafe_allow_html=True)
link1='[Presentation](https://github.com/OmdenaAI/omdena-nigeria-energy/tree/main/src/final%20deliverables/Presentation)'
st.sidebar.markdown(link1, unsafe_allow_html=True)
link2='[Data Modeling code](https://github.com/OmdenaAI/omdena-nigeria-energy/blob/main/src/final%20deliverables/task/Data_Modeling/Omdena%20cluster%20model.ipynb)'
st.sidebar.markdown(link2, unsafe_allow_html=True)
link3='[Dataset](https://github.com/OmdenaAI/omdena-nigeria-energy/tree/main/src/final%20deliverables/Dataset_final)'
st.sidebar.markdown(link3, unsafe_allow_html=True)
link4='[Data visualisation](https://github.com/OmdenaAI/omdena-nigeria-energy/tree/main/src/final%20deliverables/task/Data_visualization)'
st.sidebar.markdown(link4, unsafe_allow_html=True)
link5='[Contributors](https://github.com/OmdenaAI/omdena-nigeria-energy/blob/main/src/final%20deliverables/Lagos_Energy_Contributors.ipynb)'
st.sidebar.markdown(link5, unsafe_allow_html=True)
