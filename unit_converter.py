import streamlit as st
from pint import UnitRegistry

# Initialize Pint's Unit Registry
ureg = UnitRegistry()

# Streamlit App Title
st.title("🔄 Unit Converter App")

# Manually Defining Categories & Units
unit_categories = {
    "length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "mass": ["gram", "kilogram", "pound", "ounce"],
    "temperature": ["celsius", "fahrenheit", "kelvin"],
    "time": ["second", "minute", "hour", "day"],
    "volume": ["liter", "milliliter", "gallon", "cup"]
}

# Select Category
category = st.selectbox("Select a category:", list(unit_categories.keys()))

# Select Source and Target Units
from_unit = st.selectbox("Convert from:", unit_categories[category])
to_unit = st.selectbox("Convert to:", unit_categories[category])

# Input Value
value = st.number_input("Enter value:", format="%.6f")

# Conversion Button
if st.button("Convert"):
    try:
        if category == "temperature":
            # Temperature conversion needs proper handling
            value = ureg.Quantity(value, ureg.degC) if from_unit == "celsius" else ureg.Quantity(value, ureg.degF)
            result = value.to(ureg.degF if to_unit == "fahrenheit" else ureg.degC).magnitude
        else:
            # Normal conversion for other units
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion Error: {e}")

# Run Streamlit App with: `streamlit run unit_converter.py`
