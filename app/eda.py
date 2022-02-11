# importing packages
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

def eda():
	submenu = ["Descriptive", "Plots"]
	choice = st.sidebar.selectbox("Submenu", submenu)

	df = pd.read_csv("https://raw.githubusercontent.com/samarthgangurde01/seoul-bike-sharing-demand-prediction/main/Data.csv", sep=',', encoding='latin')
	dt = pd.read_csv("https://raw.githubusercontent.com/samarthgangurde01/seoul-bike-sharing-demand-prediction/main/File.csv", sep=',', encoding='latin')

	if choice == "Descriptive":
		st.subheader("This is our data")
		st.dataframe(df)

		st.subheader("Here are the statistical values for all the numerical columns")
		st.dataframe(df.describe())

		st.subheader("Here you will find the data types info for all the columns")
		img = Image.open("C:\B\info1641661138.jpeg")
		st.image(img)

	elif choice == "Plots":

		with st.expander("Based on Column Target"):
			choose = st.selectbox("Choose the plot you want to view", ["count of rented bikes over months",
																	   "Count of Rented bikes for weekend",
																	   "count of rented bikes for hours and weekends",
																	   "count of rented bikes over Hours",
																		"count of rented bikes for function day",
																	  	"count of rented bikes over seasons",
																	   	"count of rented bikes for holidays"])

			if choose == "count of rented bikes over months":
				a,ax = plt.subplots(figsize=(8, 8))
				sns.barplot(data=dt,x='Month',y='Rented_Bike_Count',ax=ax,capsize=.2)
				st.pyplot(a)

			elif choose == "Count of Rented bikes for weekend":
				b, ax = plt.subplots(figsize=(6,6))
				sns.barplot(data=dt, x='weekend', y='Rented_Bike_Count', ax=ax, capsize=.2)
				ax.set(title='Count of Rented bikes VS weekend ')
				st.plotly_chart(b)

			elif choose == "count of rented bikes for hours and weekends":
				c, ax = plt.subplots(figsize=(10, 8))
				sns.barplot(data=dt, x='Hour', y='Rented_Bike_Count', hue='weekend', ax=ax)
				st.plotly_chart(c)

			elif choose == "count of rented bikes for function day":
				d, ax = plt.subplots(figsize=(6, 6))
				sns.barplot(data=dt, x='Functioning_Day', y='Rented_Bike_Count', ax=ax, capsize=.2)
				st.plotly_chart(d)

			elif choose == "count of rented bikes over seasons":
				e, ax = plt.subplots(figsize=(6, 8))
				sns.barplot(data=dt, x='Seasons', y='Rented_Bike_Count', ax=ax, capsize=.2)
				st.plotly_chart(e)
			elif choose == "count of rented bikes for holidays":
				f, ax = plt.subplots(figsize=(6, 6))
				sns.barplot(data=dt, x='Holiday', y='Rented_Bike_Count', ax=ax, capsize=.2)
				ax.set(title='Count of Rented bikes acording to Holiday ')
				st.plotly_chart(f)

		with st.expander("HatMaps"):
			choose = st.selectbox("Choose the plot you want to view", ["Heat Map"])

			if choose == "Heat Map":
				cor = dt.corr()
				p = px.imshow(cor)
				st.plotly_chart(p)



