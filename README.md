# commute-calculator
App made for bus infographic poster, calculates how environment friendly your daily commute is.
import streamlit as st

st.title("Commute Tree Cost Calculator 🌳")

st.write("Find out how many trees it takes to cover your yearly commute CO₂!")

# User inputs
distance = st.number_input("Enter your daily one-way commute distance (km):", min_value=0.0, step=0.1)
mode = st.selectbox("Select your mode of transport:", ["Car", "Bus", "Bike"])

# Constants
kg_co2_per_km = {"Car": 0.21, "Bus": 0.05, "Bike": 0.0}  # kg CO₂ per km
working_days = 250
kg_co2_per_tree = 25  # annual CO₂ absorption per tree

# Calculate tree cost
if distance > 0:
    total_km = distance * 2 * working_days
    total_co2 = total_km * kg_co2_per_km[mode]
    trees_needed = total_co2 / kg_co2_per_tree
    st.success(f"Your commute uses about **{trees_needed:.1f} trees** worth of CO₂ each year!")
else:
    st.info("Enter your commute distance to see the result.")
