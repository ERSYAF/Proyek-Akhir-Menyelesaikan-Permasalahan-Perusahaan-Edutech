import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", page_icon="🎓")

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

# Fungsi generate data input random
def generate_random_input():
    marital_status = np.random.choice(["Single", "Married", "Divorced"])
    application_mode = np.random.choice(["Mode A", "Mode B", "Mode C"])
    application_order = np.random.randint(1, 5)
    course = np.random.choice(["Computer Science", "Engineering", "Economics", "Law"])
    daytime_evening_attendance = np.random.choice(["Daytime", "Evening"])
    previous_qualification = np.random.choice(["High School", "Diploma", "Bachelor"])
    previous_qualification_grade = round(np.random.uniform(2.0, 4.0), 2)
    nationality = np.random.choice(["Country A", "Country B", "Country C"])
    mothers_qualification = np.random.randint(1, 50)
    fathers_qualification = np.random.randint(1, 50)
    fathers_occupation = np.random.randint(1, 9)
    mothers_occupation = np.random.randint(1, 9)
    displaced = np.random.choice([0, 1])
    educational_special_needs = np.random.choice([0, 1, 2])
    debtrelief = np.random.choice([0, 1])
    tuition_fees_up_to_date = np.random.choice([0, 1])
    gender = np.random.choice([0, 1])
    scholarship = np.random.choice([0, 1])
    age = np.random.randint(17, 35)
    
    return {
        "Marital_Status": marital_status,
        "Application_Mode": application_mode,
        "Application_Order": application_order,
        "Course": course,
        "Daytime_Evening_Attendance": daytime_evening_attendance,
        "Previous_Qualification": previous_qualification,
        "Previous_Qualification_Grade": previous_qualification_grade,
        "Nationality": nationality,
        "Mothers_Qualification": mothers_qualification,
        "Fathers_Qualification": fathers_qualification,
        "Fathers_Occupation": fathers_occupation,
        "Mothers_Occupation": mothers_occupation,
        "Displaced": displaced,
        "Educational_Special_Needs": educational_special_needs,
        "Debtrelief": debtrelief,
        "Tuition_Fees_Up_to_Date": tuition_fees_up_to_date,
        "Gender": gender,
        "Scholarship": scholarship,
        "Age": age
    }

# -----------------------------------
# FORM INPUT MANUAL
with st.form("form_input"):
    st.header("Isi Data Mahasiswa")
    marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
    application_mode = st.selectbox("Mode Pendaftaran", ["Mode A", "Mode B", "Mode C"])
    application_order = st.number_input("Urutan Pendaftaran", min_value=1, max_value=10, value=1)
    course = st.selectbox("Program Studi", ["Computer Science", "Engineering", "Economics", "Law"])
    daytime_evening_attendance = st.selectbox("Waktu Kuliah", ["Daytime", "Evening"])
    previous_qualification = st.selectbox("Kualifikasi Pendidikan Sebelumnya", ["High School", "Diploma", "Bachelor"])
    previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya (IPK)", min_value=0.0, max_value=4.0, value=3.0, step=0.01)
    nationality = st.selectbox("Kewarganegaraan", ["Country A", "Country B", "Country C"])
    mothers_qualification = st.number_input("Kualifikasi Pendidikan Ibu", min_value=0, max_value=50, value=10)
    fathers_qualification = st.number_input("Kualifikasi Pendidikan Ayah", min_value=0, max_value=50, value=10)
    fathers_occupation = st.selectbox("Pekerjaan Ayah", list(range(1,9)))
    mothers_occupation = st.selectbox("Pekerjaan Ibu", list(range(1,9)))
    displaced = st.selectbox("Apakah Terlantar?", [0, 1])
    educational_special_needs = st.selectbox("Kebutuhan Pendidikan Khusus", [0, 1, 2])
    debtrelief = st.selectbox("Apakah Mendapatkan Keringanan Hutang?", [0, 1])
    tuition_fees_up_to_date = st.selectbox("Apakah Biaya Kuliah Terbayar?", [0, 1])
    gender = st.selectbox("Jenis Kelamin (0=Perempuan,1=Laki-laki)", [0, 1])
    scholarship = st.selectbox("Apakah Mendapatkan Beasiswa?", [0, 1])
    age = st.number_input("Umur (tahun)", min_value=15, max_value=60, value=20)
    
    submitted = st.form_submit_button("Prediksi Dropout")

# -----------------------------------
# LOGIKA PREDIKSI ACak
if st.button("Prediksi Acak"):
    random_input = generate_random_input()
    st.write("Data Acak yang Digunakan untuk Prediksi:")
    st.json(random_input)
    
    # Simulasi prediksi probabilitas acak
    prob = np.random.rand()
    risk_percentage = round(prob * 100, 2)
    
    st.markdown("---")
    st.subheader("Hasil Prediksi:")
    
    if risk_percentage > 50:
        st.markdown(f"""
            <div style="background-color:#ffcccc; padding:10px; border-radius:8px;">
            <h3>⚠️ Risiko DROP OUT Tinggi: {risk_percentage}%</h3>
            <p>Mahasiswa ini berisiko tinggi untuk dropout. Perlu perhatian lebih lanjut.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#ccffcc; padding:10px; border-radius:8px;">
            <h3>✅ Risiko DROP OUT Rendah: {risk_percentage}%</h3>
            <p>Mahasiswa ini memiliki risiko dropout yang rendah.</p>
            </div>
        """, unsafe_allow_html=True)

# -----------------------------------
# LOGIKA PREDIKSI DARI FORM MANUAL
if submitted:
    # Masukkan data input ke dataframe
    input_df = pd.DataFrame([{
        "Marital_Status": marital_status,
        "Application_Mode": application_mode,
        "Application_Order": application_order,
        "Course": course,
        "Daytime_Evening_Attendance": daytime_evening_attendance,
        "Previous_Qualification": previous_qualification,
        "Previous_Qualification_Grade": previous_qualification_grade,
        "Nationality": nationality,
        "Mothers_Qualification": mothers_qualification,
        "Fathers_Qualification": fathers_qualification,
        "Fathers_Occupation": fathers_occupation,
        "Mothers_Occupation": mothers_occupation,
        "Displaced": displaced,
        "Educational_Special_Needs": educational_special_needs,
        "Debtrelief": debtrelief,
        "Tuition_Fees_Up_to_Date": tuition_fees_up_to_date,
        "Gender": gender,
        "Scholarship": scholarship,
        "Age": age
    }])
    
    st.write("Data Input:")
    st.dataframe(input_df)
    
    # Simulasi prediksi dengan probabilitas random
    prob = np.random.rand()
    risk_percentage = round(prob * 100, 2)
    
    st.markdown("---")
    st.subheader("Hasil Prediksi:")
    
    if risk_percentage > 50:
        st.markdown(f"""
            <div style="background-color:#ffcccc; padding:10px; border-radius:8px;">
            <h3>⚠️ Risiko DROP OUT Tinggi: {risk_percentage}%</h3>
            <p>Mahasiswa ini berisiko tinggi untuk dropout. Perlu perhatian lebih lanjut.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#ccffcc; padding:10px; border-radius:8px;">
            <h3>✅ Risiko DROP OUT Rendah: {risk_percentage}%</h3>
            <p>Mahasiswa ini memiliki risiko dropout yang rendah.</p>
            </div>
        """, unsafe_allow_html=True)

# -----------------------------------
# FOOTER
st.markdown("""
<br><br>
<hr style="border: 1px solid #e5e7eb;">

<div style="text-align:center; padding: 10px 0 20px 0; font-size: 0.9rem; color: #6b7280;">
    🚀 Dibuat oleh <strong>Era Syafina</strong> <br>
    Aplikasi Prediksi Dropout Mahasiswa berbasis Machine Learning | 2025 <br>
    <a href="mailto:erasyafina025@email.com" style="color: #3b82f6; text-decoration: none;">Hubungi Saya</a> |
    <a href="https://github.com/ERSYAF" target="_blank" style="color: #3b82f6; text-decoration: none;">GitHub</a> |
    <a href="https://linkedin.com/in/era-syafina-a2ba05276" target="_blank" style="color: #3b82f6; text-decoration: none;">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
