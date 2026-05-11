import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="AI Batch Analyser", layout="wide")

st.title("🚀 AI Batch Pattern Analyser")
st.write("Tempelkan ribuan data nomor di bawah ini untuk analisis instan.")

# --- AREA COPY-PASTE ---
st.header("1. Input Data (Copy-Paste)")
raw_data = st.text_area("Tempel nomor di sini (pisahkan dengan spasi, koma, atau baris baru):", 
                        height=200, 
                        placeholder="Contoh: 1234, 5678, 9012...")

# Proses Data
all_numbers = []
if raw_data:
    # Membersihkan data: memisahkan berdasarkan spasi, koma, atau enter
    all_numbers = raw_data.replace(',', ' ').replace('\n', ' ').split()
    st.success(f"✅ {len(all_numbers)} data berhasil dibaca!")

# --- ANALISIS & PREDIKSI ---
if len(all_numbers) > 0:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header("2. Statistik Digit")
        all_digits = "".join(all_numbers)
        counts = Counter(all_digits)
        
        # Tabel Frekuensi
        freq_df = pd.DataFrame.from_dict(counts, orient='index', columns=['Muncul']).sort_index()
        st.bar_chart(freq_df)
        
        # Angka Terkuat
        hot_digits = [item[0] for item in counts.most_common(4)]
        st.info(f"Digit Terkuat (Hot): {', '.join(hot_digits)}")

    with col2:
        st.header("3. Generator Prediksi")
        num_to_gen = st.slider("Jumlah prediksi yang ingin dihasilkan:", 10, 200, 100)
        
        if st.button(f"Generate {num_to_gen} Prediksi Sekarang"):
            prediksi_list = []
            
            for _ in range(num_to_gen):
                # Metode: Mengambil 4 digit berdasarkan bobot frekuensi (Hot Numbers lebih sering muncul)
                # Jika ingin murni acak dari history, gunakan random.sample
                pola = "".join(random.choices(all_digits, k=4))
                prediksi_list.append(pola)
            
            # Tampilan dalam bentuk grid agar rapi
            st.write(f"### Hasil {num_to_gen} Prediksi:")
            st.code("  |  ".join(prediksi_list)) 
            
            # Fitur Download
            txt_result = "\n".join(prediksi_list)
            st.download_button("Download Hasil (TXT)", txt_result, file_name="prediksi.txt")
else:
    st.info("Menunggu data ditempelkan untuk memulai analisis.")

st.divider()
st.caption("Tips: Jika data bertambah setiap hari, cukup copy semua dari file Excel/catatanmu dan tempel ulang di sini.")
