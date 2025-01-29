import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

st.image('Nikita_profile_photo.jpeg')

# Collect basic information
name = "Nikita Qosholo"
field = "Oceanography"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


# Add a section for publications
st.header("Publications")
st.text("Pending")
# Add a contact section

st.header("Contact Information")
email = "qosholonikita@gmail.com"
st.write(f"You can reach {name} at {email}.")
