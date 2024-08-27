import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

df = pd.read_csv('data/uwa.csv')


st.title("愛媛県避難所開設状況マップ")

# st.table(data=df)

f_map = folium.Map(
    location = [33.203803, 132.555574],
    zoom_start = 11)

color_dict = {'open':'blue', 'close':'red', np.nan:'lightgray'}

for index, row in df.iterrows():
    folium.Marker(
        [row['lat'], row['lon']],
        popup=row['name'],
        icon=folium.Icon(color=color_dict[row['status']])
    ).add_to(f_map)


st_folium(f_map, use_container_width=True, height=720, returned_objects=[])
