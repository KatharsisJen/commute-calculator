import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Commute Tree Cost 🌳", page_icon="🌍", layout="centered")

st.title("🌳 Commute Tree Cost Calculator")
st.subheader("How many trees does your commute cost each year?")

# --- USER INPUTS ---
distance = st.number_input(
    "Enter your daily one-way commute distance (km):",
    min_value=0.0, step=0.5, format="%.1f"
)
mode = st.radio(
    "Select your mode of transport:",
    ["Car", "Bus", "Bike"],
    help="Your main daily commute mode"
)

# --- CONSTANTS ---
kg_co2_per_km = {"Car": 0.21, "Bus": 0.05, "Bike": 0.0}  # kg CO₂ per km
working_days = 250
kg_co2_per_tree = 25  # kg CO₂ absorbed by a tree per year

# --- CALCULATION ---
if distance > 0:
    total_km = distance * 2 * working_days
    total_co2 = total_km * kg_co2_per_km[mode]
    trees_needed = total_co2 / kg_co2_per_tree

    # --- RESULT DISPLAY ---
    st.metric("🌱 Trees Needed to Offset", f"{trees_needed:.1f} trees")

    # Tree bar visualization (max 50)
    tree_count = min(int(trees_needed), 50)
    st.write("Tree impact visualisation (max 50 trees):")
    st.write("🌳" * tree_count if tree_count > 0 else "🌱 No trees needed!")

    st.write(f"**CO₂ produced:** {total_co2:.0f} kg per year")

    # --- FEEDBACK & SUGGESTIONS ---
    if trees_needed < 2:
        st.success("Amazing! 🌟 Your commute is very eco-friendly. Keep it up!")
    elif 2 <= trees_needed <= 10:
        st.info("Good job! 🌿 Consider biking or bussing even more for extra savings.")
    else:
        st.error("High impact 🚨 Consider switching to bus or bike to save many trees!")
        st.write(f"If you took the bus instead, you'd only need **{(total_co2 * 0.25 / kg_co2_per_tree):.1f} trees**.")

else:
    st.info("Enter your commute details to see your tree impact.")
