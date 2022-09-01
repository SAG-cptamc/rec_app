# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:25:12 2022

@author: gskvskumar
"""

import streamlit as st
from PIL import Image
import psycopg2
image= Image.open(r"C:/Users/gskvskumar/Desktop/desktop 24-5-2022/qasource.jpg") 

pic= st.sidebar.image(image, use_column_width=True)
st.sidebar.caption("For over 20 years, we have provided dedicated offshore quality engineering teams and expertise that work hand-in-hand with our clients to deliver thoroughly tested code for internal and commercial applications.")
st.sidebar.title("Smart Interview System")
st.sidebar.header("Processes")
select = st.sidebar.selectbox(
    "Navigation",
    ("Updating Database", "Image Data Testing", "Video Data Testing","Records")
)
if select == "Updating Database":
    st.title("Updating Database")
    # Initialize connection.
    # Uses st.experimental_singleton to only run once.
    @st.experimental_singleton
    def init_connection():
        return psycopg2.connect(**st.secrets["postgres"])

    conn = init_connection()
    ename = st.text_input("Enter Aspirant's name")
    eladdress = st.text_input("Enter Directory of Image with extension i.e .jpg etc")
    submit_button = form_submit_button(label='Submit')

if select == "Image Data Testing":
    st.title("Image Data Testing")


if select == "Video Data Testing":
    st.title("Video Data Testing")


if select == "Records":
    st.title("Records")
































#     col1 = st.form(key='my_form')
#     col1.header("A data science project for employee data")
#     col1.text_input('Name')
#     col1.text_input('Email address')
#     col1.number_input('Pick a number',10)
#     col1.text_area('Messege')
#     submit_button = col1.form_submit_button(label='Submit')
    
    
# if submit_button:
#     st.info(' Thank you! Form submission Succesful')
# with col2:
#     col2 = st.form(key='my_form1')
#     col2.number_input('Salary')
#     col2.text_input('Designation')
#     col2.text_input('Department')
#     submit_button1 =col2. form_submit_button(label='Submit')
# if submit_button1:
#         st.success(' Thank you! Form submission Succesful')