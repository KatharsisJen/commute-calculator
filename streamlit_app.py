import streamlit as st

st.title("Commute Tree Cost Calculator 🌳")
st.write("See how many trees your commute costs the planet each year!")

# User inputs
distance = st.number_input("Enter your daily one-way commute distance (km):", min_value=0.0, step=0.5)
mode = st.selectbox("Select your mode of transport:", ["Car", "Bus", "Bike"])

# Constants
kg_co2_per_km = {"Car": 0.21, "Bus": 0.05, "Bike": 0.0}
working_days = 250
kg_co2_per_tree = 25

# Calculate tree cost
if distance > 0:
    total_km = distance * 2 * working_days
    total_co2 = total_km * kg_co2_per_km[mode]
    trees_needed = total_co2 / kg_co2_per_tree

    st.metric(label="Trees Needed per Year", value=f"{trees_needed:.1f}")

    # Show tree icons (limit to 50)
    tree_icons = "🌳" * min(int(trees_needed), 50)
    st.write(tree_icons if tree_icons else "No trees needed! 🌱")

    # Extra info
    st.write(f"That's equal to **{total_co2:.0f} kg of CO₂** per year.")

    if mode == "Car" and trees_needed > 10:
        st.warning("Consider switching to a bus or bike to cut your tree cost!")
else:
    st.info("Enter your commute distance to see your result.")
