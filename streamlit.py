import streamlit as st
import random
st.title("NKSTUDIOS")
st.header("Imagine to Inspire; Implement to Immortalise")
st.subheader("Home of music by NKBEATZ, movies and web-series by NKFILMS, stories and novels by NKPUBLISHERS")
st.markdown("Thanks for choosing us. Fill in your details below.")
name = st.text_input("Enter your name:")
st.radio("Pick your gender",['Male','Female','Transgender','Prefer not to say'])
st.slider("Pick your age", 18, 100)
st.selectbox("From where did you get to know about us?",['Social Media','Current Employees','Newspaper','Television','Prefer not to say'])
st.selectbox("You are applying for:",['Internship','Contract-based Work','Permanent Job'])
idd = random.randrange(1000000,2000000)
if st.button("Submit"):
    st.write("Hello,", name, "!", "Thanks for applying. Welcome to NKSTUDIOS. Your ID is: ",idd)
