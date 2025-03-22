import folium
import streamlit.components.v1 as components

def display_traffic_map(lat, lon, api_key):
    """Generate an interactive map with TomTom Traffic Flow Tiles."""
    # Initialize map centered on user location
    traffic_map = folium.Map(location=[lat, lon], zoom_start=14)

    # Add TomTom Traffic Flow Tile Layer
    folium.TileLayer(
        tiles=f"https://{api_key}@api.tomtom.com/map/1/tile/flow/relative0/{{z}}/{{x}}/{{y}}.png?tileSize=256&key={api_key}",
        attr="TomTom Traffic",
        name="Traffic Flow",
        overlay=True,
        control=True
    ).add_to(traffic_map)

    # Add marker for the location
    folium.Marker([lat, lon], tooltip="Traffic Location", icon=folium.Icon(color="red")).add_to(traffic_map)

    # Add Layer control
    folium.LayerControl().add_to(traffic_map)

    # Render map in Streamlit
    components.html(traffic_map._repr_html_(), height=500)
