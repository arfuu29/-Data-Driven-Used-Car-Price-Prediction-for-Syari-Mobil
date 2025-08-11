import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Syari Mobil | Prediksi Harga",
    page_icon="🚗",
    layout="wide"
)

# --- Fungsi untuk Memuat Model ---
# Menggunakan cache agar model tidak perlu dimuat ulang setiap kali ada interaksi
@st.cache_resource
def load_model(path):
    with open(path, 'rb') as file:
        model_pipeline = pickle.load(file)
    return model_pipeline

# --- Memuat Model ---
# Ganti 'best_model.pkl' dengan nama file pickle Anda
try:
    model = load_model('best_model.pkl')
except FileNotFoundError:
    st.error("File model 'best_model.pkl' tidak ditemukan. Pastikan file tersebut berada di folder yang sama dengan app.py")
    st.stop()


# --- Daftar Opsi untuk Input dari Notebook Anda ---
# (Pastikan opsi ini sesuai dengan yang digunakan saat melatih model)
make_options = ['Toyota', 'Hyundai', 'Ford', 'Chevrolet', 'Nissan', 'GMC', 'Kia', 'Mercedes', 'Lexus', 'Mazda', 'Honda', 'BMW', 'Mitsubishi', 'Dodge', 'Land Rover', 'Other']
type_options = ['Land Cruiser', 'Camry', 'Hilux', 'Accent', 'Yukon', 'Sonata', 'Tahoe', 'Taurus', 'Elantra', 'Expedition', 'Corolla', 'Furniture', 'Suburban', 'Patrol', 'Prado', 'Accord', 'S', 'ES', 'Range Rover', 'Sunny', 'Other']
region_options = ['Riyadh', 'Dammam', 'Jeddah', 'Qassim', 'Al-Medina', 'Al-Ahsa', 'Aseer', 'Makkah', 'Taef', 'Tabouk', 'Other']
gear_type_options = ['Automatic', 'Manual']
origin_options = ['Saudi', 'Gulf Arabic', 'Other', 'Unknown']
options_options = ['Full', 'Standard', 'Semi Full']


# --- Antarmuka Pengguna (UI) ---

# Judul dan Deskripsi
st.title("🚗 Syari Mobil - Alat Estimasi Harga")
st.markdown("Gunakan alat ini untuk mendapatkan estimasi harga pasar yang wajar untuk mobil bekas di Arab Saudi. Cukup masukkan detail mobil di panel sebelah kiri.")

# Sidebar untuk Input
st.sidebar.header("Masukkan Detail Mobil")

# Input dari Pengguna
make = st.sidebar.selectbox("Merek (Make)", make_options)
type_lumped = st.sidebar.selectbox("Tipe (Type)", type_options)
region_lumped = st.sidebar.selectbox("Wilayah (Region)", region_options)
gear_type = st.sidebar.selectbox("Tipe Transmisi (Gear Type)", gear_type_options)
origin = st.sidebar.selectbox("Asal (Origin)", origin_options)
options = st.sidebar.selectbox("Opsi Fitur (Options)", options_options)

year = st.sidebar.slider("Tahun Pembuatan (Year)", 1980, datetime.now().year, 2015)
mileage = st.sidebar.number_input("Jarak Tempuh (Mileage)", min_value=0, max_value=1000000, value=150000, step=1000)
engine_size = st.sidebar.slider("Ukuran Mesin (Engine Size)", 1.0, 8.0, 2.5, 0.1)

# Tombol Prediksi
predict_button = st.sidebar.button("Prediksi Harga", use_container_width=True, type="primary")


# --- Area Output ---
st.subheader("Hasil Estimasi Harga")

if predict_button:
    # 1. Membuat DataFrame dari input
    car_age = datetime.now().year - year
    
    input_data = {
        'Gear_Type': [gear_type],
        'Origin': [origin],
        'Options': [options],
        'Engine_Size': [engine_size],
        'Mileage': [mileage],
        'Type_Lumped': [type_lumped],
        'Make_Lumped': [make],
        'Region_Lumped': [region_lumped],
        'is_classic': [1 if car_age > 25 else 0],
        'car_class': ['Luxury' if make in ['Rolls-Royce', 'Bentley', 'Ferrari', 'Lamborghini', 'McLaren', 'Aston Martin', 'Maserati', 'Porsche'] 
                      else 'Premium' if make in ['Mercedes-Benz', 'BMW', 'Audi', 'Lexus', 'Jaguar', 'Land Rover', 'Cadillac', 'Genesis', 'Lincoln', 'Infiniti'] 
                      else 'Standard'],
        'Mileage_per_Age': [mileage / (car_age + 1)],
        'Price_Deviation_by_Make': [0], # Placeholder, ini akan dihitung ulang jika perlu atau diabaikan oleh model
        'Car_Age_Sq': [car_age**2]
    }
    
    # Pastikan urutan kolom sesuai dengan saat training
    feature_order = [
        'Gear_Type', 'Origin', 'Options', 'Engine_Size', 'Mileage', 
        'Type_Lumped', 'Make_Lumped', 'Region_Lumped', 'is_classic', 
        'car_class', 'Mileage_per_Age', 'Price_Deviation_by_Make', 'Car_Age_Sq'
    ]
    input_df = pd.DataFrame(input_data)[feature_order]

    # 2. Melakukan Prediksi
    with st.spinner("Menghitung estimasi..."):
        prediction_log = model.predict(input_df)
        prediction_real = np.expm1(prediction_log)[0]

    # 3. Menampilkan Hasil
    st.success("Prediksi berhasil dibuat!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Estimasi Harga Wajar",
            value=f"{prediction_real:,.0f} SAR"
        )
    
    with col2:
        # Menampilkan rentang harga berdasarkan MAPE 7.52%
        mape = 0.0752
        lower_bound = prediction_real * (1 - mape)
        upper_bound = prediction_real * (1 + mape)
        st.metric(
            label="Rentang Harga Pasar (±7.5%)",
            value=f"{lower_bound:,.0f} - {upper_bound:,.0f} SAR",
            help="Rentang ini didasarkan pada rata-rata kesalahan model sebesar 7.52% pada data uji."
        )

    st.markdown("---")
    st.markdown("**Disclaimer:** Estimasi ini adalah hasil dari model machine learning dan harus digunakan sebagai referensi. Harga final dapat bervariasi tergantung kondisi fisik mobil dan negosiasi.")

else:
    st.info("Silakan masukkan detail mobil di panel sebelah kiri dan klik 'Prediksi Harga'.")

