import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Commute Tree Cost", page_icon="🌳", layout="centered")

# --- HEADER ---
st.markdown("<h1 style='text-align:center; font-size:48px;'>🌳 Tree Commute Calculator</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; font-size:20px;'>See your annual CO₂ impact in trees</p>", unsafe_allow_html=True)

# --- INPUTS ---
distance = st.slider("Daily one-way distance (km):", 0, 100, 20)
mode = st.selectbox("Transport mode:", ["Car 🚗", "Bus 🚌", "Bike 🚴‍♀️"])

# --- CONSTANTS ---
co2_per_km = {"Car 🚗": 0.21, "Bus 🚌": 0.05, "Bike 🚴‍♀️": 0}
working_days = 250
co2_per_tree = 25

# --- CALC ---
if distance > 0:
    total_km = distance * 2 * working_days
    co2 = total_km * co2_per_km[mode]
    trees = round(co2 / co2_per_tree, 1)

    # --- DISPLAY ---
    st.metric("Trees per year 🌲", f"{trees} trees")
    st.progress(min(int(trees), 50) / 50)  # Visual bar

    if trees < 2:
        st.success("Excellent! 🌟 Keep going green!")
    elif trees < 10:
        st.warning("Not bad — try a few more bus/bike trips 🚴‍♂️")
    else:
        st.error("High impact! 🚨 Consider switching to bus or bike.")

else:
    st.info("Move the slider to calculate your tree impact 🌱")
