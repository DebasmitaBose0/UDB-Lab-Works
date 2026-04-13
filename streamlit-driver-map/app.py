import pandas as pd
import streamlit as st
import pydeck as pdk

st.set_page_config(page_title="Driver Location Map", layout="wide")

st.title("Driver Location Map")
st.markdown("Visualize driver positions and status on an interactive map.")

# Example driver location data
drivers = pd.DataFrame(
    [
        {
            "driver_id": "D1001",
            "name": "Ava",
            "status": "Available",
            "lat": 37.7749,
            "lon": -122.4194,
        },
        {
            "driver_id": "D1002",
            "name": "Noah",
            "status": "Delivering",
            "lat": 37.7845,
            "lon": -122.4076,
        },
        {
            "driver_id": "D1003",
            "name": "Mia",
            "status": "Offline",
            "lat": 37.7647,
            "lon": -122.4312,
        },
        {
            "driver_id": "D1004",
            "name": "Ethan",
            "status": "Available",
            "lat": 37.7893,
            "lon": -122.4140,
        },
        {
            "driver_id": "D1005",
            "name": "Liam",
            "status": "Delivering",
            "lat": 37.7719,
            "lon": -122.4471,
        },
    ]
)

st.subheader("Driver status")
st.dataframe(drivers)

st.subheader("Map view")
map_df = drivers.rename(columns={"lat": "latitude", "lon": "longitude"})
st.map(map_df)

st.subheader("Richer map visualization")

status_colors = {
    "Available": [0, 200, 0],
    "Delivering": [0, 120, 255],
    "Offline": [220, 20, 60],
}

drivers["color"] = drivers["status"].map(status_colors)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=drivers,
    get_position="[lon, lat]",
    get_fill_color="color",
    get_radius=150,
    pickable=True,
    auto_highlight=True,
)

view_state = pdk.ViewState(latitude=37.776, longitude=-122.42, zoom=12, pitch=0)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "Driver: {name}\nStatus: {status}"},
)

st.pydeck_chart(deck)

st.markdown(
    "---\n"
    "Use the map controls to zoom, pan, and inspect driver locations."
)

st.caption("Run this app with `streamlit run app.py`. This container listens on port 8501.")
