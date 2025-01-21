import streamlit as st

def calculate_storage_capacity(total_area, non_storage_area, usable_height, pallet_volume, utilization_factor):
    # Calculate net storage area
    net_storage_area = total_area - non_storage_area
    
    # Calculate storage volume
    storage_volume = net_storage_area * usable_height

    # Adjust for utilization factor
    effective_capacity = storage_volume * utilization_factor

    # Convert to pallet positions
    pallet_positions = effective_capacity / pallet_volume

    return net_storage_area, storage_volume, effective_capacity, pallet_positions

# Streamlit App
st.title("Warehouse Storage Capacity Estimator")

# Input parameters
st.sidebar.header("Input Parameters")
total_area = st.sidebar.number_input("Total Warehouse Area (m²)", min_value=0.0, value=10000.0, step=100.0)
non_storage_area = st.sidebar.number_input("Non-Storage Area (m²)", min_value=0.0, value=2000.0, step=100.0)
usable_height = st.sidebar.number_input("Usable Height (m)", min_value=0.0, value=10.0, step=0.1)
pallet_volume = st.sidebar.number_input("Average Pallet Volume (m³)", min_value=0.1, value=1.8, step=0.1)
utilization_factor = st.sidebar.slider("Space Utilization Factor (%)", min_value=0, max_value=100, value=85) / 100

# Calculate results
net_storage_area, storage_volume, effective_capacity, pallet_positions = calculate_storage_capacity(
    total_area, non_storage_area, usable_height, pallet_volume, utilization_factor
)

# Display results
st.header("Results")
st.write(f"**Net Storage Area:** {net_storage_area:.2f} m²")
st.write(f"**Storage Volume:** {storage_volume:.2f} m³")
st.write(f"**Effective Capacity:** {effective_capacity:.2f} m³")
st.write(f"**Estimated Pallet Positions:** {pallet_positions:.0f}")

st.markdown("---")
st.markdown("### How It Works")
st.write(
    "This app calculates the estimated storage capacity of a warehouse based on input parameters such as total warehouse area, non-storage areas, usable height, and pallet dimensions. "
    "It also adjusts for space utilization efficiency to provide a realistic estimate of usable storage capacity."
)

st.markdown("---")
st.markdown("### Remark")
st.write(
    "**Pallet size consideration:** The calculation assumes an average pallet volume, which varies based on regional and industry standards. "
    "Common sizes include **1200 x 1000 mm**, **1219 x 1016 mm**, and **1200 x 800 mm**. Ensure the input pallet volume matches your specific requirements for accurate results."
)

# Add table of pallet sizes
st.markdown("---")
st.markdown("### Common Standard Pallet Sizes")
st.write(
    "| Region/Standard         | Dimensions (mm)         | Dimensions (in)       | Notes                                |\n"
    "|-------------------------|-------------------------|-----------------------|--------------------------------------|\n"
    "| **ISO Standard Pallets**|                         |                       | Globally recognized for trade       |\n"
    "|                         | 1200 x 1000            | 47.2 x 39.4           | Common in Europe, Asia, internationally |\n"
    "|                         | 1200 x 800             | 47.2 x 31.5           | Euro pallet, widely used in Europe  |\n"
    "|                         | 1140 x 1140            | 44.9 x 44.9           | Used in Australia and other regions |\n"
    "|                         | 1100 x 1100            | 43.3 x 43.3           | Common in Asia, particularly Japan  |\n"
    "|                         | 1067 x 1067            | 42 x 42               | North America, international shipping |\n"
    "| **North American**      | 1219 x 1016            | 48 x 40               | Dominant in retail, grocery industries |\n"
    "| **European**            | 1200 x 800             | 47.2 x 31.5           | Euro pallet (EPAL 1)                |\n"
    "|                         | 1200 x 1000            | 47.2 x 39.4           | Common in general industry          |\n"
    "| **Australian**          | 1165 x 1165            | 45.9 x 45.9           | Used in warehouses, rail transport  |\n"
    "| **Asian**               | 1100 x 1100            | 43.3 x 43.3           | Widely used in Japan, Korea, China  |\n"
    "| **Other Notable Sizes** | 1200 x 1200            | 47.2 x 47.2           | Bulk materials                      |\n"
    "|                         | 800 x 600              | 31.5 x 23.6           | Half-pallet, smaller shipments      |"
)
