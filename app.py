import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(
    page_title="Dashboard Prediksi Dropout - Era Syafina",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS untuk style
st.markdown("""
<style>
    .stSidebar .css-1d391kg {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 10px 0;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1e40af;
    }
    .result-box {
        padding: 30px;
        border-radius: 12px;
        margin-top: 20px;
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
        text-align: center;
    }
    .high-risk {
        background-color: #dc2626;
        box-shadow: 0 0 20px #f87171;
    }
    .low-risk {
        background-color: #16a34a;
        box-shadow: 0 0 20px #4ade80;
    }
    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Load model dan scaler dengan cache
@st.cache_resource
def load_model_files():
    model_path = "model_dropout_xgboost.pkl"
    scaler_path = "scaler.pkl"
    encoders_path = "label_encoders.pkl"
    if not all(os.path.exists(p) for p in [model_path, scaler_path, encoders_path]):
        return None, None, None
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    encoders = joblib.load(encoders_path)
    return model, scaler, encoders

model, scaler, label_encoders = load_model_files()

# Header utama
st.title("🎓 Dashboard Prediksi Dropout Mahasiswa")
st.markdown("Disusun oleh **Era Syafina**")

if model is None or scaler is None or label_encoders is None:
    st.error("⚠️ File model, scaler, atau label encoder tidak ditemukan. Pastikan file 'model_dropout_xgboost.pkl', 'scaler.pkl', dan 'label_encoders.pkl' ada di folder aplikasi.")
    st.stop()

# Sidebar Input Data
st.sidebar.header("📝 Input Data Mahasiswa")

def select_option(label, options_dict):
    choice = st.sidebar.selectbox(label, options=list(options_dict.keys()))
    return options_dict[choice]

marital_status = select_option("Status Pernikahan", {
    "1 - Single": 1,
    "2 - Married": 2,
    "3 - Widower": 3,
    "4 - Divorced": 4,
    "5 - Facto union": 5,
    "6 - Legally separated": 6,
})

application_mode = select_option("Mode Pendaftaran", {
    "1 - 1st phase - general contingent": 1,
    "2 - Ordinance No. 612/93": 2,
    "5 - 1st phase - special contingent (Azores Island)": 5,
    "7 - Holders of other higher courses": 7,
    "10 - Ordinance No. 854-B/99": 10,
    "15 - International student (bachelor)": 15,
    "16 - 1st phase - special contingent (Madeira Island)": 16,
    "17 - 2nd phase - general contingent": 17,
    "18 - 3rd phase - general contingent": 18,
    "26 - Ordinance No. 533-A/99, item b2)": 26,
    "27 - Ordinance No. 533-A/99, item b3": 27,
    "39 - Over 23 years old": 39,
    "42 - Transfer": 42,
    "43 - Change of course": 43,
    "44 - Technological specialization diploma holders": 44,
    "51 - Change of institution/course": 51,
    "53 - Short cycle diploma holders": 53,
    "57 - Change of institution/course (International)": 57,
})

application_order = st.sidebar.number_input("Urutan Pendaftaran", min_value=0, max_value=9, value=0)

course = select_option("Program Studi", {
    "33 - Biofuel Production Technologies": 33,
    "171 - Animation and Multimedia Design": 171,
    "8014 - Social Service (evening attendance)": 8014,
    "9003 - Agronomy": 9003,
    "9070 - Communication Design": 9070,
    "9085 - Veterinary Nursing": 9085,
    "9119 - Informatics Engineering": 9119,
    "9130 - Equinculture": 9130,
    "9147 - Management": 9147,
    "9238 - Social Service": 9238,
    "9254 - Tourism": 9254,
    "9500 - Nursing": 9500,
    "9556 - Oral Hygiene": 9556,
    "9670 - Advertising and Marketing Management": 9670,
    "9773 - Journalism and Communication": 9773,
    "9853 - Basic Education": 9853,
    "9991 - Management (evening attendance)": 9991,
})

daytime_evening_attendance = select_option("Waktu Kehadiran", {
    "1 - Daytime": 1,
    "0 - Evening": 0
})

previous_qualification = select_option("Kualifikasi Sebelumnya", {
    "1 - Secondary education": 1,
    "2 - Higher education - bachelor's degree": 2,
    "3 - Higher education - degree": 3,
    "4 - Higher education - master's": 4,
    "5 - Higher education - doctorate": 5,
    "6 - Frequency of higher education": 6,
    "9 - 12th year of schooling - not completed": 9,
    "10 - 11th year of schooling - not completed": 10,
    "12 - Other - 11th year of schooling": 12,
    "14 - 10th year of schooling": 14,
    "15 - 10th year of schooling - not completed": 15,
    "19 - Basic education 3rd cycle": 19,
    "38 - Basic education 2nd cycle": 38,
    "39 - Technological specialization course": 39,
    "40 - Higher education - degree (1st cycle)": 40,
    "42 - Professional higher technical course": 42,
    "43 - Higher education - master (2nd cycle)": 43,
})

previous_qualification_grade = st.sidebar.number_input(
    "Nilai Kualifikasi Sebelumnya", 
    min_value=0.0, 
    max_value=200.0, 
    value=100.0,
    step=0.1,
)

nationality = select_option("Kewarganegaraan", {
    "1 - Portuguese": 1,
    "2 - German": 2,
    "6 - Spanish": 6,
    "11 - Italian": 11,
    "13 - Dutch": 13,
    "14 - English": 14,
    "17 - Lithuanian": 17,
    "21 - Angolan": 21,
    "22 - Cape Verdean": 22,
    "24 - Guinean": 24,
    "25 - Mozambican": 25,
    "26 - Santomean": 26,
    "32 - Turkish": 32,
    "41 - Brazilian": 41,
    "62 - Romanian": 62,
    "100 - Moldova (Republic of)": 100,
    "101 - Mexican": 101,
    "103 - Ukrainian": 103,
    "105 - Russian": 105,
    "108 - Cuban": 108,
    "109 - Colombian": 109,
})

mothers_qualification = select_option("Kualifikasi Ibu", {
    "1 - Secondary Education": 1,
    "2 - Higher Education - Bachelor's Degree": 2,
    "3 - Higher Education - Degree": 3,
    "4 - Higher Education - Master's": 4,
    "5 - Higher Education - Doctorate": 5,
    "6 - Frequency of Higher Education": 6,
    "9 - 12th Year of Schooling - Not Completed": 9,
    "10 - 11th Year of Schooling - Not Completed": 10,
    "12 - Other - 11th Year of Schooling": 12,
    "14 - 10th Year of Schooling": 14,
    "15 - 10th Year of Schooling - Not Completed": 15,
})

# Membuat DataFrame input untuk model
input_data = pd.DataFrame({
    'Marital_status': [marital_status],
    'Application_mode': [application_mode],
    'Application_order': [application_order],
    'Course': [course],
    'Daytime_evening_attendance': [daytime_evening_attendance],
    'Previous_qualification': [previous_qualification],
    'Previous_qualification_grade': [previous_qualification_grade],
    'Nationality': [nationality],
    'Mothers_qualification': [mothers_qualification]
})

# Encode categorical features
for col in label_encoders:
    if col in input_data.columns:
        enc = label_encoders[col]
        input_data[col] = enc.transform(input_data[col])

# Scale fitur numerik
input_scaled = scaler.transform(input_data)

# Tombol prediksi
if st.sidebar.button("🔍 Prediksi Dropout"):
    prediction_proba = model.predict_proba(input_scaled)[0][1]  # Prob dropout
    prediction_label = "Berisiko Dropout" if prediction_proba >= 0.5 else "Tidak Berisiko Dropout"
    
    # Tampilkan hasil dengan style
    box_class = "high-risk" if prediction_proba >= 0.5 else "low-risk"
    st.markdown(f'<div class="result-box {box_class}">Probabilitas Dropout: {prediction_proba:.2%} <br> <br> <span style="font-size:1.5rem">{prediction_label}</span></div>', unsafe_allow_html=True)

    # Grafik probabilitas
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=prediction_proba*100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Probabilitas Dropout (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#dc2626" if prediction_proba >= 0.5 else "#16a34a"},
            'steps': [
                {'range': [0, 50], 'color': "#a7f3d0"},
                {'range': [50, 100], 'color': "#fecaca"},
                {'range': [70, 100], 'color': "salmon"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 50}}))
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Masukkan data mahasiswa lengkap di sidebar lalu klik tombol Prediksi untuk melihat hasil.")

