import streamlit as st
import pandas as pd
import joblib
import datetime
from streamlit_lottie import st_lottie
import requests

# --------------------------
# LOAD TRAINED PIPELINE
# --------------------------
model = joblib.load("traffic_analysis.pkl")

def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(e)
        return None



traffic_animation = load_lottie(
    "https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json"
)

st.title("🚦 Traffic Congestion Prediction System")

if traffic_animation:
    st_lottie(traffic_animation, height=380)


st.write("Enter traffic conditions:")

# --------------------------
# USER INPUTS
# --------------------------



hour_part = st.selectbox("Hour", list(range(1, 13)))
minute_part = st.selectbox("Minute", list(range(0, 60)))
ampm = st.selectbox("AM/PM", ["AM", "PM"])

# Convert to 24-hour format
if ampm == "PM" and hour_part != 12:
    hour = hour_part + 12
elif ampm == "AM" and hour_part == 12:
    hour = 0
else:
    hour = hour_part

months = {
    "January": 1, "February": 2, "March": 3,
    "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

selected_month = st.selectbox("Month", list(months.keys()))
month = months[selected_month]

temp = st.number_input("Temperature (°C)", value=20.0)

clouds = st.slider("Cloud Cover (%)", 0, 100, 40)

rain = st.selectbox("Rain in last hour?",["YES","NO"])
#rain_val = 1 if rain else 0 
snow = st.selectbox("Snow in last hour?", ["No", "Yes"])

weather_main = st.selectbox(
    "Weather Condition",
    [
        "Clouds",
        "Clear",
        "Rain",
        "Snow",
        "Mist",
        "Haze",
        "Fog",
        "Drizzle",
        "Thunderstorm",
        "Smoke",
        "Squall"
    ]
)

is_weekend = st.selectbox("Is Weekend?", ["No", "Yes"])

# --------------------------
# CONVERT INPUTS
# --------------------------

rain_val = 1 if rain == "Yes" else 0
snow_val = 1 if snow == "Yes" else 0
is_weekend_val = 1 if is_weekend == "Yes" else 0

# --------------------------
# CREATE INPUT DATAFRAME
# --------------------------

input_data = pd.DataFrame([{
    'temp': temp,
    'clouds_all': clouds,
    'rain_1hr': rain_val,
    'snow_1hr': snow_val,
    'weather_main': weather_main,
    'hour': hour,
    'month': month,
    'is_weekend': is_weekend_val
}])

# --------------------------
# PREDICTION
# --------------------------

if st.button("Predict Traffic"):

    with st.spinner("Analyzing traffic conditions..."):
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]

    st.metric("Traffic Risk", f"{proba*100:.2f}%")
    st.progress(int(proba * 100))

    if prediction == 1:
        st.error("🚦 Heavy Traffic — Consider alternate route!")
    else:
        st.success("✅ Your Road Looks Clear!")