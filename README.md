
#Project Title : Seoul Bike Sharing Demand Prediction

## Description
Handelling missing values and duplicates was our first step, and secondly we moved to Exploratry data analysis where we performed Exploratory Data Analysis(EDA) on all the features of our datset. We first analysed our dependent variable, 'Rented Bike Count' & independet variables like month, weekend and hours etc.further we moved toword variables correlation and their relationship with the others We also removed some features.could create dummie variables of categorical variables.in last we implemented 6 machine learning algorithms Linear Regression,Lasso,ridge,Decission Tree, Random Forest and XGBoost.none of them showed overfitting.Random Forest Model has given accuracy upto 90% which is preety good for prediction and choosing it for deployment
we created our webapp by streamlit library and deployed it on Heroku

## Table of Content
* Dataset Information
* Tools and Libraries Used
* Files
* Results
* Screenshots
* Deployment
* Business Summary
* 
## Dataset Information
Currently Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.
The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour and date information.

Dataset Link:-https://github.com/samarthgangurde01/seoul-bike-sharing-demand-prediction/blob/main/SeoulBikeData.csv

## Tools and Libraries Used
* Pandas
* numpy
* Matplotlib
* Seaborn
* plotly
* sklearn
* pickle

## Files
* This repository contains two files /
* capston_seoul_bike_prediction.ipynb: Google colab contains all the python code, documentation and visualization
* SeoulBikeData.csv: Our dataset 
* /clean data/Data.csv: Our processed dataset file
* /clean data/clean.csv:clean dataset file
* /app/app.py:contains whole structure of app
* /app/eda.py:contains EDA setup for app
* /app/main.py:contains best algorithm for app
* /image/info1641661138.jpeg:image
* /image/philly-bike-share.jpeg:image
* requirements.txt:contains required libraries 

## Results
Random Forest Model has given accuracy upto 90%.Lets see its other values

RANDOM FOREST

MSE : 15.382922163400737

RMSE : 3.922106852624076

MAE : 2.5328978390679664

R2 : 0.9004823319676353

## Screenshots

![image](https://user-images.githubusercontent.com/93859458/152525488-f743f44c-6947-4c05-b11c-5614dfca8807.png)
![image](https://user-images.githubusercontent.com/93859458/152525537-d5d5f4fd-f315-4436-95fa-f291f138c1ec.png)
![image](https://user-images.githubusercontent.com/93859458/152525193-6bf7f581-24de-494a-bd94-9159f1cf7c8d.png)
![image](https://user-images.githubusercontent.com/93859458/152525374-ff641401-7fa5-4161-aedc-14d57784fe39.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/samarthgangurde01/seoul-bike-sharing-demand-prediction
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

## Demo vedio,when we run model on local servor
link-https://youtu.be/zcb8x2iGAw4

we suggest you to watch in full screen


## Deployment
we deployed our model on streamlit.io
![image](https://user-images.githubusercontent.com/93859458/153545789-856eae5b-c9d4-44c4-a1f4-5440083dbb59.png)

### streamlit.io
Streamlit.io is an open-source platform for machine learning and data science teams to create data applications with python
The platform uses python scripting, APIs, widgets, instant deployment, team collaboration tools, and application management solutions to help data scientists and machine learning engineers create python-based applications. Applications created using Streamlit range from applications capable of real time object detection, geographic data browsers, deep dream network debuggers, to face-GAN explorers. Frameworks compatible with Streamlit include: Scikit Learn, Keras, Plotly, OpenCV,, NumPy, Seaborn, Python, Matplotlib, and Pandas.

Link for app:- https://share.streamlit.io/samarthgangurde01/seoul-bike-sharing-demand-prediction/main/app/app.py

### Screenshorts of deployed model
![image](https://user-images.githubusercontent.com/93859458/153553308-3059baae-1ee5-4ac7-8d01-668329cf45ff.png)
![image](https://user-images.githubusercontent.com/93859458/153553584-ae52fdef-f504-47eb-8bbb-1ea4cf8d0431.png)
![image](https://user-images.githubusercontent.com/93859458/153553639-e99741f7-48c9-4ca6-bfb4-47abfed1fcd4.png)
![image](https://user-images.githubusercontent.com/93859458/153553712-144b0090-238c-4a96-8aac-9e9928b3b2ed.png)


### Trial datasets
                                                   
Temperature          : -5.2                                                

Humidity             :  37                                              

Wind_speed           :  2.2                                               

Visibility           :  2000                                              

Solar_Radiation      :  0.0                                               

Rainfall             :  0.0                                              

Snowfall             :  0.0                                            

Hour                 :  24

Seasons              :  winter

Holiday              :  YES                                             

Month                :  1st                                                 

Functioning_Day      :  YES                                               

weekend              :  NO                                               



## Business Goal:
You are required to builed model of demand for shared bikes with the available independent variables. It will be used by the management to understand how exactly the demands vary with different features. They can accordingly manipulate the business strategy to meet the demand levels and meet the customer's expectations. Further, the model will be a good way for management to understand the demand dynamics of a new market.


## Feedback
If you have any feedback, please reach out to us at samarthgangurde01@gmail.com

