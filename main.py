import numpy as np
import pandas as pd
import streamlit as st


dataset = pd.read_csv('cleaned_data.csv', sep=',', encoding='latin')


X = dataset.drop(columns=['Rented_Bike_Count'], axis=1)
y = np.sqrt(dataset['Rented_Bike_Count'])



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0)

from sklearn.preprocessing import MaxAbsScaler
scaler =MaxAbsScaler()
# fit the scaler to the train set, it will learn the parameters
scaler.fit(X_train)

# transform train and test sets
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#import the packages
from sklearn.ensemble import RandomForestRegressor
# Create an instance of the RandomForestRegressor
rf_model = RandomForestRegressor()
#Fitting the model and printing y_pred
rf_model.fit(X_train,y_train)

Model=rf_model



def welcome():
    return "Welcome All"

def seoulbikedemand_prediction(Temperature, Humidity, Wind_speed, Visibility, Solar_Radiation, Rainfall, Snowfall,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23,Hour_24,Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No,Month_2,Month_3,Month_4,Month_5,Month_6,Month_7,Month_8,Month_9,Month_10,Month_11,Month_12,Functioning_Day_Yes,weekend_1):
    predictionn = Model.predict([[Temperature,Humidity,Wind_speed,Visibility,Solar_Radiation,Rainfall,Snowfall,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23,Hour_24,Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No,Month_2,Month_3,Month_4,Month_5,Month_6,Month_7,Month_8,Month_9,Month_10,Month_11,Month_12,Functioning_Day_Yes,weekend_1]])
    print(predictionn)
    return predictionn


def main():
    st.title("seoul bike prediction ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    Temperature = st.text_input('Temperature in celsius')
    Humidity = st.text_input('Humidity Level')
    Wind_speed = st.text_input('Wind_speed in m/s')
    Visibility = st.text_input('Visibility')
    Solar_Radiation = st.text_input('Solar_Radiation')
    Rainfall = st.text_input('Rainfall')
    Snowfall = st.text_input('Snowfall')

    # for hours
    hours_list = ['Hour_1', 'Hour_2', 'Hour_3', 'Hour_4', 'Hour_5', 'Hour_6', 'Hour_7', 'Hour_8', 'Hour_9', 'Hour_10',
                  'Hour_11', 'Hour_12', 'Hour_13', 'Hour_14', 'Hour_15', 'Hour_16', 'Hour_17', 'Hour_18', 'Hour_19',
                  'Hour_20', 'Hour_21', 'Hour_22', 'Hour_23','Hour_24']

    Hour = st.selectbox('which season', hours_list)
    if Hour == 'Hour_1':
        Hour_1 = 1
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_2':
        Hour_1 = 0
        Hour_2 = 1
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_3':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 1
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_4':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 1
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_5':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 1
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_6':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 1
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_7':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 1
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_8':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 1
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_9':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 1
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_10':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 1
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_11':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 1
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_12':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 1
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_13':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 1
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_14':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 1
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_15':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 1
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_16':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 1
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_17':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 1
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_18':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 1
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_19':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 1
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0

    elif Hour == 'Hour_20':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 1
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0


    elif Hour == 'Hour_21':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 1
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 0


    elif Hour == 'Hour_22':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 1
        Hour_23 = 0
        Hour_24 = 0


    elif Hour == 'Hour_23':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 1
        Hour_24 = 0


    elif Hour == 'Hour_24':
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0
        Hour_24 = 1



    # for season
    season_list = ['Seasons_Spring', 'Seasons_Autumn', 'Seasons_Summer', 'Seasons_Winter']
    season = st.selectbox('which season', season_list)

    if season == 'Seasons_Autumn':
        Seasons_Spring = 0
        Seasons_Summer = 0
        Seasons_Winter = 0

    elif season == 'Seasons_Spring':
        Seasons_Spring = 1
        Seasons_Summer = 0
        Seasons_Winter = 0

    elif season == 'Seasons_Summer':
        Seasons_Spring = 0
        Seasons_Summer = 1
        Seasons_Winter = 0

    elif season == 'Seasons_Winter':
        Seasons_Spring = 0
        Seasons_Summer = 0
        Seasons_Winter = 1

         ##for holliday
    holidays_list = ['YES', 'NO']
    holliday = st.selectbox('is it holliday', holidays_list)
    if holliday == 'NO':
            Holiday_No = 1
    else:
            Holiday_No = 0

            # for month
    month_list = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6', 'Month_7', 'Month_8', 'Month_9',
                  'Month_10', 'Month_11', 'Month_12']
    month = st.selectbox('which month', month_list)

    if month == 'Month_1':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_2':
        Month_2 = 1
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_3':
        Month_2 = 0
        Month_3 = 1
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_4':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 1
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_4':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 1
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_5':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 1
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_6':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 1
        Month_7 = 0
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_7':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 1
        Month_8 = 0
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_8':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 1
        Month_9 = 0
        Month_10 = 0
        Month_12 = 0


    elif month == 'Month_9':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 0
        Month_9 = 1
        Month_10 = 0
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_10':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 1
        Month_9 = 0
        Month_10 = 1
        Month_11 = 0
        Month_12 = 0

    elif month == 'Month_11':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 1
        Month_9 = 0
        Month_10 = 0
        Month_11 = 1
        Month_12 = 0

    elif month == 'Month_12':
        Month_2 = 0
        Month_3 = 0
        Month_4 = 0
        Month_5 = 0
        Month_6 = 0
        Month_7 = 0
        Month_8 = 1
        Month_9 = 0
        Month_10 = 0
        Month_11 = 0
        Month_12 = 1

        # for function days
    Functionday_list = ['Yes', 'No']
    Function = st.selectbox('is it  Functionday?', Functionday_list)
    if Function == '  Yes':
        Functioning_Day_Yes = 1
    else:
        Functioning_Day_Yes = 0

        # for weekends

    weekend_list = ['No','Yes']
    weekend = st.selectbox('is it weekend?', weekend_list)
    if weekend == 'Yes':
        weekend_1 = 1
    else:
      weekend_1 = 0

    result = ""
    if st.button("Predict"):
     result = seoulbikedemand_prediction(Temperature, Humidity, Wind_speed, Visibility, Solar_Radiation, Rainfall, Snowfall,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23,Hour_24,Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No,Month_2,Month_3,Month_4,Month_5,Month_6,Month_7,Month_8,Month_9,Month_10,Month_11,Month_12,Functioning_Day_Yes,weekend_1)
     result = result**2
     st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
