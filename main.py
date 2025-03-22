import streamlit as st
from traffic_utils import get_coordinates, get_traffic_flow_data
from map_utils import display_traffic_map
from config import TOMTOM_API_KEY

st.title("🚥  Traffic Flow App")

# User enters a place name
location = st.text_input("Enter a location (e.g., New York, Los Angeles)", "San Francisco")

if st.button("Get Traffic Data"):
    coords = get_coordinates(location, TOMTOM_API_KEY)
    
    if coords:
        lat, lon = coords
        data = get_traffic_flow_data(lat, lon, TOMTOM_API_KEY)

        if data:
            st.write("### Traffic Flow Data")
            st.write(f"📍 **Current Speed:** {data['flowSegmentData']['currentSpeed']} km/h")
            st.write(f"🚗 **Free Flow Speed:** {data['flowSegmentData']['freeFlowSpeed']} km/h")
            st.write(f"🔍 **Confidence Level:** {data['flowSegmentData']['confidence']}")

            # Traffic Condition Alerts
            speed_ratio = data['flowSegmentData']['currentSpeed'] / data['flowSegmentData']['freeFlowSpeed']
            if speed_ratio > 0.8:
                st.success("✅ Smooth Traffic")
            elif speed_ratio > 0.5:
                st.warning("⚠️ Moderate Traffic")
            else:
                st.error("❌ Heavy Traffic")

            # Display traffic flow map
            display_traffic_map(lat, lon, TOMTOM_API_KEY)
        else:
            st.error("Failed to fetch traffic data. Check location or API key.")
    else:
        st.error("Invalid location. Try again.")
