import streamlit as st
import pandas as pd
import time

# Title of the app
st.title("Nikita's Profile Page")
# Collect basic information
name = "Nikita Qosholo"
field = "Oceanography"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.image('Nikita_profile_photo.jpeg')

st.header("Researcher Overview")
description = """
Master of Science student in Physical Oceanography with a strong focus on characterizing surface ocean variability using 
observational data. Passionate about advancing understanding of ocean dynamics through rigorous analysis and research. 
"""

def stream_data():
    for word in description.split(" "):
        yield word + " "
        time.sleep(0.02)

# Display basic profile information
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


# Add a section for publications
st.header("Publications")
st.text("Pending")
# Add a contact section

st.header("Contact Information")
email = "qosholonikita@gmail.com"
st.write(f"You can reach {name} at {email}.")
