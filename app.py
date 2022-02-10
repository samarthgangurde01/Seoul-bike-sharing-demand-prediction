import streamlit as st
from main import main
from eda import eda
import urllib.request
from PIL import Image
def main_page():
    menu = ["Home", "Data Analysis Section", "Prediction Section", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":

        st.write("## Seoul Bike Sharing Demand Prediction")

        urllib.request.urlretrieve(
            'http://betterbikeshare.org/wp-content/uploads/2015/06/BikeShareLaunch.227.jpg',
            "gfg.png")

        img = Image.open("gfg.png")
        st.image(img)

        st.write(
            """
### - DataScource
The data that we use in this particular app is provided by almabetter contain the features of Seoul Bike Sharing Demand System.
- https://drive.google.com/drive/folders/1PhGs30XnVzPtdGC6Zsl1NO5Jk4D-6qvu
### - App Content
 - This app has four sections

 1) Home Page - The page you are currently in

 2) Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts
  * Descriptive - The page in which you will find more info about data
  * Plots - The page in which you will find plots of the data


 3) Prediction- The page in which you will be asked to give the information on all the required aspects
   and we will predict the desired the output
   
 4) About - This Page is about me
       """)

    elif choice == "Data Analysis Section":
        eda()
    elif choice == "Prediction Section":
        main()
    else:
        st.subheader("About")
        st.write("""
          #### Name :- Samarth Gokulsing Gangurde
          #### Email:-samarthgangurde01@gmail.com
          #### Data Scientist Enthusiast 
          #### Github link-https://github.com/samarthgangurde01""")



main_page()