import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="AI Multi-D Predictor", layout="wide")

st.title("🎯 AI Multi-D Pattern Analyser")
st.write("Input 4D, Output 4D, 3D, & 2D dengan format kustom.")

# --- INPUT AREA ---
raw_data = st.text_area("Tempel Data 4D di sini:", height=150, placeholder="Contoh: 1234 5678 9012...")

all_numbers = []
if raw_data:
    # Membersihkan input agar hanya mengambil angka 4 digit
    processed = raw_data.replace(',', ' ').replace('\n', ' ').split()
    all_numbers = [num for num in processed if len(num) == 4 and num.isdigit()]
    st.success(f"✅ {len(all_numbers)} data 4D valid terbaca.")

if all_numbers:
    all_digits = "".join(all_numbers)
    
    # Fungsi Helper untuk Generate Format Bintang
    def generate_formatted(digits_source, length, count):
        results = []
        for _ in range(count):
            num = "".join(random.choices(digits_source, k=length))
            results.append(f"*{num}*")
        return "".join(results)

    # --- TAMPILAN OUTPUT ---
    tab1, tab2, tab3 = st.tabs(["🔮 Prediksi 4D", "🔮 Prediksi 3D", "🔮 Prediksi 2D"])

    with tab1:
        st.header("Prediksi 4D (100 Line)")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("🔥 Top Prediksi")
            st.code(generate_formatted(all_digits, 4, 34), wrap_lines=True)
        with col2:
            st.subheader("⚡ Prediksi Kedua")
            st.code(generate_formatted(all_digits, 4, 33), wrap_lines=True)
        with col3:
            st.subheader("🛡️ Cadangan")
            st.code(generate_formatted(all_digits, 4, 33), wrap_lines=True)

    with tab2:
        st.header("Prediksi 3D (100 Line)")
        tcol1, tcol2, tcol3 = st.columns(3)
        with tcol1:
            st.subheader("🔥 Top Prediksi")
            st.code(generate_formatted(all_digits, 3, 34), wrap_lines=True)
        with tcol2:
            st.subheader("⚡ Prediksi Kedua")
            st.code(generate_formatted(all_digits, 3, 33), wrap_lines=True)
        with tcol3:
            st.subheader("🛡️ Cadangan")
            st.code(generate_formatted(all_digits, 3, 33), wrap_lines=True)

    with tab3:
        st.header("Prediksi 2D (10 Line)")
        st.info("10 Prediksi Terpilih Berdasarkan Bobot Frekuensi")
        st.code(generate_formatted(all_digits, 2, 10), wrap_lines=True)

else:
    st.info("Silakan tempel data 4D untuk memproses prediksi.")

st.divider()
st.caption("Logika: Angka dihasilkan berdasarkan bobot kemunculan digit (probability weight) dari data history.")
