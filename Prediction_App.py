import pandas as pd
import streamlit as st
import joblib as jl
import matplotlib.pyplot as plt

# UI
st.set_page_config(page_title="Water Pollution Predictor", layout="centered")
st.markdown("""
<style>
.stApp {
    background-image: url('https://web-assets.bcg.com/8e/cf/276ec569492cb6f13a8b56061b35/what-is-water-really-worth-report-rectangle.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}
.transbox {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    text-align: center;
}
.title-text {
    color: navy;
    font-size: 28px;
    font-weight: bold;
}
.desc-text {
    color: navy;
    font-size: 16px;
}
.section-header {
    color: white;
    font-size: 20px;
    font-weight: bold;
    margin-top: 2rem;
    background-color: rgba(100, 149, 237, 0.8);
    padding: 0.5rem;
    border-radius: 5px;
}
.expander-title-box {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 0.6rem 1rem;
    border-radius: 6px;
    font-weight: bold;
    color: black;
    margin-top: 1.2rem;
}
.expander-box {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 1rem;
    border-radius: 8px;
    color: black;
    overflow-x: auto;
}
/* White arrow and text for expander */
details summary {
    color: white;
}
details summary::-webkit-details-marker {
    filter: invert(1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('''
<div class="transbox">
    <div class="title-text">Water Pollution Predictor</div>
    <div class="desc-text">This app predicts pollution levels for various parameters based on <b>Station ID</b> and <b>Year</b></div>
</div>
''', unsafe_allow_html=True)

# MODEL LOADING
try:
    model = jl.load('stacking_prediction_model.pkl')
    model_cols = jl.load('columns.pkl')
except Exception as e:
    st.error(f"Error loading model or column data: {e}")
    st.stop()

with st.sidebar:
    st.header("Input Parameters")
    year_input = st.number_input('Select Year', min_value=1995, max_value=2050, value=2026)
    station_id = st.number_input('Enter Station ID', min_value=1, max_value=22, value=1)

#PREDICTION
if st.button('Predict'):
    input_df = pd.DataFrame({'year': [year_input], 'id': [str(station_id)]})
    input_encoded = pd.get_dummies(input_df, columns=['id'], prefix='id')
    for col in model_cols:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_cols]

    try:
        predicted_pollutants = model.predict(input_encoded)[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
    thresholds = {
        'NH4': (0.0, 0.3, 0.5),
        'BSK5': (0.0, 2.0, 3.0),
        'Suspended': (0.0, 15, 25),
        'O2': (8, 5, 0),
        'NO3': (0.0, 5, 10),
        'NO2': (0.0, 0.05, 0.1),
        'SO4': (0.0, 150, 250),
        'PO4': (0.0, 0.05, 0.1),
        'CL': (0.0, 150, 250)
    }

    def classify(pollutant, value):
        low, mid, high = thresholds[pollutant]
        if pollutant == 'O2':
            if value >= low:
                return 'Good'
            elif value >= mid:
                return 'Acceptable'
            else:
                return 'High'
        else:
            if value <= low:
                return 'Good'
            elif value <= mid:
                return 'Acceptable'
            else:
                return 'High'

    status = [classify(p, val) for p, val in zip(pollutants, predicted_pollutants)]

    ranges = [f"{t[0]}–{t[1]} (Good), {t[1]}–{t[2]} (Acceptable), >{t[2]} (High)" if p != 'O2'
              else f">{t[0]} (Good), {t[1]}–{t[0]} (Acceptable), <{t[1]} (High)"
              for p, t in thresholds.items()]

    st.markdown(f'<div class="section-header">Predicted Pollution Levels for Station {station_id} in {year_input}</div>', unsafe_allow_html=True)
    results_df = pd.DataFrame({
        'Pollutant': pollutants,
        'Predicted Value': predicted_pollutants,
        'Status': status,
        'Healthy Range': ranges
    })

    st.dataframe(results_df.style.applymap(
        lambda val: 'background-color: lightgreen' if val == 'Good'
        else 'background-color: khaki' if val == 'Acceptable'
        else 'background-color: pink',
        subset=['Status']
    ), use_container_width=True)

# VISUALIZATION
    st.markdown('<div class="section-header">Visual Summary</div>', unsafe_allow_html=True)
    colors = {'Good': 'green', 'Acceptable': 'orange', 'High': 'red'}
    bar_colors = [colors[s] for s in status]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(pollutants, predicted_pollutants, color=bar_colors)
    ax.set_ylabel("Pollution Level")
    ax.set_ylim(0, max(predicted_pollutants) * 1.2)
    ax.set_title("Predicted Levels by Pollutant")
    st.pyplot(fig)

# HEALTH & ENVIRONMENTAL EFFECTS
    effects_df = pd.DataFrame({
    'Pollutant': ['NH₄ (Ammonium)', 'BSK5 (BOD5)', 'Suspended Solids', 'O₂ (Dissolved Oxygen)', 'NO₃ (Nitrate)',
                  'NO₂ (Nitrite)', 'SO₄ (Sulfate)', 'PO₄ (Phosphate)', 'Cl⁻ (Chloride)'],
    'Safe Limit': ['≤ 0.5 mg/L', '≤ 3 mg/L', '≤ 25 mg/L', '≥ 5 mg/L', '≤ 10 mg/L',
                   '≤ 0.1 mg/L', '≤ 250 mg/L', '≤ 0.1 mg/L', '≤ 250 mg/L'],
    'Abnormal Value Effects': [
        'High values indicate organic pollution or sewage',
        'High = More organic matter needing oxygen',
        'High turbidity reduces light penetration',
        'Low DO stresses or kills aquatic life',
        'High nitrate levels from fertilizers/sewage',
        'Indicates recent pollution or microbial activity',
        'High in industrial runoff or mineral water',
        'Leads to nutrient enrichment (eutrophication)',
        'High from sewage, road salts, or industry'
    ],
    'Health/Environmental Consequences': [
        'Toxic to aquatic life; indicates wastewater contamination',
        'Depletes oxygen → aquatic death; sign of pollution',
        'Harms aquatic plants and animals; sediment buildup',
        'Causes fish kills; indicates poor water quality',
        'Can cause blue baby syndrome (methemoglobinemia)',
        'Toxic; affects blood oxygen transport',
        'Causes diarrhea; corrosive to infrastructure',
        'Algal blooms → oxygen depletion → fish death',
        'Affects taste, agriculture; corrosive to pipes'
    ]
})

    st.markdown('<div class="section-header">Health & Environmental Effects of Pollutants</div>', unsafe_allow_html=True)
    st.dataframe(effects_df, use_container_width=True)