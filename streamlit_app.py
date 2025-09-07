import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Your Commute Cost Calculator", page_icon="🌳", layout="centered")

# --- HEADER ---
st.markdown("<h1 style='text-align:center; font-size:48px;'>🌳 Your Commute Cost Calculator </h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; font-size:20px;'>How many trees does your commute cost each year?</p>", unsafe_allow_html=True)

# --- INPUTS ---
distance = st.number_input("Enter your daily one-way commute distance (km):", min_value=0.0, max_value=1000.0, value=30.0, step=1.0)
mode = st.selectbox("Select your transport mode:", ["Car 🚗", "Bus 🚌", "Bike 🚴‍♀️"])

# --- CONSTANTS ---
co2_per_km = {"Car 🚗": 0.21, "Bus 🚌": 0.05, "Bike 🚴‍♀️": 0}
working_days = 250
co2_per_tree = 25

# --- CALCULATION ---
if distance > 0:
    total_km = distance * 2 * working_days
    co2 = total_km * co2_per_km[mode]
    trees = round(co2 / co2_per_tree, 1)

    # --- DISPLAY ---
    st.metric("Trees per year 🌲", f"{trees} trees")
    progress_value = min(trees, 150) / 150
    st.progress(progress_value)

    # --- FEEDBACK ---
    if trees <= 50:
        st.success("🌟 Excellent! You're keeping it green.")
    elif trees <= 100:
        st.warning("😐 Moderate. Could be better — try bus or bike more often.")
    else:
        st.error("🚨 High impact! Consider greener commuting options.")

else:
    st.info("Enter your distance to calculate your tree cost 🌱")
