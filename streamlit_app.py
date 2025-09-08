import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Your Commute Cost Calculator",
    page_icon="🌳",
    layout="centered"
)

# --- HEADER ---
st.header("Your Commute Cost Calculator")
st.subheader("Find out how many trees your commute costs each year!")

# --- INPUTS ---
distance = st.number_input(
    "Enter your daily one-way commute distance (km):",
    min_value=0.0,
    max_value=1000.0,
    value=30.0,
    step=1.0
)

mode = st.selectbox(
    "Select your transport mode:",
    ["Car", "Bus", "Bike"]
)

# --- CONSTANTS ---
CO2_PER_KM = {
    "Car": 0.21,  # kg CO2 per km
    "Bus": 0.05,
    "Bike": 0
}
WORKING_DAYS = 250
CO2_PER_TREE = 25  # kg CO2 absorbed per tree per year

# --- CALCULATION ---
if distance > 0:
    total_km = distance * 2 * WORKING_DAYS
    co2_kg = total_km * CO2_PER_KM[mode]
    trees = round(co2_kg / CO2_PER_TREE, 1)

    # --- DISPLAY ---
    st.metric("Trees per year", f"{trees} trees")
    st.progress(min(trees, 150) / 150)

    # --- FEEDBACK ---
    if trees <= 50:
        st.success("Excellent! Your commute is very eco-friendly.")
    elif trees <= 100:
        st.warning("Moderate impact. Try using bus or bike more often.")
    else:
        st.error("High impact! Consider switching to greener options.")
else:
    st.info("Enter your distance above to calculate your tree cost.")
