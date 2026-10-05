import streamlit as st
import pandas as pd
import joblib

import os

# Obtenir le chemin absolu du dossier où se trouve app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.joblib")

# Charger le modèle
model = joblib.load(model_path)

# Configuration
st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️"
)

st.title("✈️ Flight Price Prediction")
st.write("Predisez le prix d'un billet d'avion.")

# Formulaire
airline = st.selectbox(
    "Compagnie aerienne",
    ["SpiceJet", "AirAsia", "Vistara", "GO_FIRST", "Indigo", "Air_India"]
)

source_city = st.selectbox(
    "Ville de depart",
    ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
)

departure_time = st.selectbox(
    "Heure de depart",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)

stops = st.selectbox(
    "Nombre d'escales",
    ["zero", "one", "two_or_more"]
)

arrival_time = st.selectbox(
    "Heure d'arrivee",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)

destination_city = st.selectbox(
    "Destination",
    ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
)

flight_class = st.selectbox(
    "Classe",
    ["Economy", "Business"]
)

duration = st.number_input(
    "Duree du vol (heures)",
    min_value=0.1,
    max_value=50.0,
    value=2.0
)

days_left = st.number_input(
    "Nombre de jours avant le vol",
    min_value=1,
    max_value=49,
    value=10
)

# Prediction
if st.button("💰 Predire le prix"):

    test = pd.DataFrame([{
        "airline": airline,
        "source_city": source_city,
        "departure_time": departure_time,
        "stops": stops,
        "arrival_time": arrival_time,
        "destination_city": destination_city,
        "class": flight_class,
        "duration": duration,
        "days_left": days_left
    }])

    prediction = model.predict(test)

    st.success(
        f"Prix estime : {prediction[0]:,.2f}"
    )