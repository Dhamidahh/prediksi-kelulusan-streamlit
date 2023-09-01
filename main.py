#Masukkan Library
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah', 'Kuliah_Kerja_Mahasiswa',
              'Seminar_Pendidikan_Agama', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']
# Muat model
model = joblib.load('random_forest_model.pkl')

# Muat data training
X_train = joblib.load('X_train.pkl')
y_train = joblib.load('y_train.pkl')

# Judul aplikasi
st.title('Prediksi Kelulusan Tepat Waktu')

# Judul header dan masukkin nama
st.header("Aplikasi Prediksi Kelulusan Mahasiswa TI UNTIRTA")

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama_Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
img = img.resize((300, 300))
st.image(img, use_column_width=False)


# Fungsi untuk melakukan prediksi
def predict_lulus_tepat_waktu(input_nilai_mata_kuliah):
    prediction = model.predict([input_nilai_mata_kuliah])
    return prediction[0]


# Input nilai mata kuliah
Bahasa_Inggris = st.number_input("Masukkan Nilai Bahasa Inggris", 0.0, max(data["Bahasa_Inggris"]), 4.0, 0.0)
Fisika_Dasar_1 = st.number_input("Masukkan Nilai Fisika Dasar 1", 0.0, max(data["Fisika_Dasar_1"]), 4.0, 0.0)
Kalkulus_1 = st.number_input("Masukkan Nilai Kalkulus 1", 0.0, max(data["Kalkulus_1"]), 4.0, 0.0)
Kimia_Dasar = st.number_input("Masukkan Nilai Kimia Dasar", 0.0, max(data["Kimia_Dasar"]), 4.0, 0.0)
Pengantar_Teknik_Industri = st.number_input("Masukkan Nilai Pengantar Teknik Industri 1", 0.0,
                                            max(data["Pengantar_ Teknik_Industri"]), 4.0, 0.0)
Sistem_Lingkungan_Industri = st.number_input("Masukkan Nilai Sistem Lingkungan Industri", 0.0,
                                             max(data["Sistem_Lingkungan_Industri"]), 4.0, 0.0)
Fisika_Dasar_2 = st.number_input("Masukkan Nilai Fisika Dasar 2", 0.0, max(data["Fisika_Dasar_2"]), 4.0, 0.0)
Kalkulus_2 = st.number_input("Masukkan Nilai Kalkulus 2", 0.0, max(data["Kalkulus_2"]), 4.0, 0.0)
Menggambar_Teknik = st.number_input("Masukkan Nilai Menggambar Teknik", 0.0, max(data["Menggambar_Teknik"]), 4.0, 0.0)
Pengantar_Ekonomika = st.number_input("Masukkan Nilai Pengantar Ekonomika", 0.0, max(data["Pengantar_Ekonomika "]), 4.0, 0.0)
Praktikum_Fisika_Dasar = st.number_input("Masukkan Nilai Praktikum Disika Dasar", 0.0,
                                         max(data["Praktikum_Fisika_Dasar"]), 4.0, 0.0)
Praktikum_Menggambar_Teknik = st.number_input("Masukkan Nilai Praktikum Menggambar Teknik", 0.0,
                                              max(data["Praktikum_Menggambar_Teknik"]), 4.0, 0.0)
Aljabar_Linear = st.number_input("Masukkan Nilai Aljabar Linear", 0.0, max(data["Aljabar_Linear"]), 4.0)
Ergonomi_dan_Perancangan_Sistem_Kerja_1 = st.number_input("Masukkan Nilai Ergonomi dan Perancangan Sistem Kerja", 0.0,
                                                          max(data["Ergonomi_dan_Perancangan_Sistem_Kerja_1"]), 4.0, 0.0)
Mekanika_Teknik = st.number_input("Masukkan Nilai Mekanika Teknik", 0.0, max(data["Mekanik_Teknik"]), 4.0, 0.0)
Material_Teknik = st.number_input("Masukkan Nilai Material Teknik", 0.0, max(data["Material_Teknik"]), 4.0, 0.0)
Pemrograman_Komputer = st.number_input("Masukkan Nilai Pemrograman Komputer", 0.0, max(data["Pemrograman_Komputer"]),
                                       4.0, 0.0)
Penelitian_Operasional_1 = st.number_input("Masukkan Nilai Penelitian Operasional", 0.0,
                                           max(data["Penelitian_Operasional"]), 4.0, 0.0)
Praktikum_Material = st.number_input("Masukkan Nilai Prakikum Material", 0.0, max(data["Praktikum_Material"]), 4.0, 0.0)
Praktikum_Pemrograman_Komputer = st.number_input("Masukkan Nilai Praktikum Pemrograman Komputer", 0.0,
                                                 max(data["Praktikum_Pemrograman_Komputer"]), 4.0, 0.0)
Proses_Manufaktur = st.number_input("Masukkan Nilai Proses Manufaktur", 0.0, max(data["Proses_Manufaktur"]), 4.0, 0.0)
Statistika_Industri = st.number_input("Masukkan Nilai Statistika Industri", 0.0, max(data["Statistika_Industri"]), 4.0)
Analisis_Biaya = st.number_input("Masukkan Nilai Analisis Biaya", 0.0, max(data["Analisis_Biaya"]), 4.0, 0.0)
Ergonomi_dan_Perancangan_Sistem_Kerja_2 = st.number_input("Masukkan Nilai Ergonomi dan Perancangan Sistem Kerja 2", 0.0,
                                                          max(data["Ergonomi_dan_Perancangan_Sistem_Kerja_2"]), 4.0, 0.0)
Matematika_Optimasi = st.number_input("Masukkan Nilai Penelitian Operasional 2", 0.0, max(data["Matematika_Optimasi"]),
                                      4.0, 0.0)
Perancangan_dan_Pengembangan_Produk = st.number_input("Masukkan Nilai Perancangan dan Pengembangan Produk", 0.0,
                                                      max(data["Perancangan_dan_Pengembangan _Produk "]), 4.0)
Penelitian_Operasional_2 = st.number_input("Masukkan Nilai Penelitian Operasional 2", 0.0,
                                           max(data["Penelitian_Operasional_2"]), 4.0, 0.0, key="penelitian_operasional_2")
Praktikum_Perancangan_Teknik_Industri_1 = st.number_input("Masukkan Nilai Praktikum Perancangan Teknik Industri 1", 0.0,
                                                          max(data["Praktikum_Perancangan_Teknik_Industri_1"]), 4.0, 0.0)
Psikologi_Industri = st.number_input("Masukkan Nilai Psikologi Industri", 0.0, max(data["Psikologi_Industri"]), 4.0, 0.0)
Statistika_Industri_2 = st.number_input("Masukkan Nilai Statistika Industri 2", 0.0, max(data["Statistika_Industri_2"]),
                                        4.0, 0.0)
Ekonomi_Teknik = st.number_input("Masukkan Nilai Ekonomi Teknik", 0.0, max(data["Ekonomi_Teknik"]), 4.0, 0.0)
Mekatronika_dan_Opimasi_Sistem_Produksi = st.number_input("Masukkan Nilai Mekatronika dan Optimasi Sistem Produksi",
                                                          0.0, max(data["Mekatronika_dan_Opimasi_Sistem_Produksi"]),
                                                          4.0, 0.0)
Pemodelan_Sistem = st.number_input("Masukkan Nilai Pemodelan Sistem", 0.0, max(data["Pemodelan_Sistem"]), 4.0, 0.0)
Pengendalian_dan_Penjaminan_Mutu = st.number_input("Masukkan Nilai Pengendalian dan Penjaminan Mutu", 0.0,
                                                   max(data["Pengendalian_dan_Penjaminan_Mutu"]), 4.0, 0.0)
Perancangan_Tata_Letak_Fasilitas = st.number_input("Masukkan Nilai Perancangan Tat Letak Fasilitas", 0.0,
                                                   max(data["Perancangan_Tata_Letak_Fasilitas"]), 4.0, 0.0)
Perencanaan_dan_Pengendalian_Produksi = st.number_input("Masukkan Nilai Perancangan dan Pengendalian Produksi", 0.0,
                                                        max(data["Perencanaan_dan_Pengendalian_Produksi"]), 4.0, 0.0)
Praktikum_Perancangan_Teknik_Industri_2 = st.number_input("Masukkan Nilai Praktikum Perancangan Teknik Industri 2", 0.0,
                                                          max(data["Praktikum_Perancangan_Teknik_Industri_2"]), 4.0, 0.0)
Analisis_dan_Peancangan_Perusahaan = st.number_input("Masukkan Nilai Analisis dan Perancangan Perusahaan", 0.0,
                                                     max(data["Analisis_dan_Peancangan_Perusahaan"]), 4.0, 0.0)
Analisis_dan_Perancangan_Sistem_Informasi = st.number_input("Masukkan Nilai Analisis dan Perancangan Sistem Informasi",
                                                            0.0, max(data["Analisis_dan_Perancangan_Sistem_Informasi"]),
                                                            4.0, 0.0)
Kerja_Praktek = st.number_input("Masukkan Nilai Kerja Praktek", 0.0, max(data["Kerja_Praktek"]), 4.0, 0.0)
Kesehatan_dan_Keselamatan_Kerja = st.number_input("Masukkan Nilai Kesehatan dan Keselamatan Kerja", 0.0,
                                                  max(data["Kesehatan_dan_Keselamatan_Kerja"]), 4.0, 0.0)
Organisasi_dan_Manajemen_Perusahaan_Industri = st.number_input(
    "Masukkan Nilai Oragnisasi dan Manajemen Perusahaan Industri", 0.0,
    max(data["Organisasi_dan_Manajemen_Perusahaan_Industri"]), 4.0, 0.0)
Praktikum_Perancangan_Teknik_Industri_3 = st.number_input("Masukkan Nilai Praktikum dan Perancangan Teknik Industri 3",
                                                          0.0, max(data["Praktikum_Perancangan_Teknik_Industri_2"]),
                                                          4.0, 0.0)
Simulasi_Komputer = st.number_input("Masukkan Nilai Simulasi Komputer", 0.0, max(data["Simulasi_Komputer"]), 4.0, 0.0)
Sistem_Produksi = st.number_input("Masukkan Nilai Sistem Produksi", 0.0, max(data["Sistem_Produksi"]), 4.0, 0.0)
Kewirausahaan = st.number_input("Masukkan Nilai Kewirausahaan", 0.0, max(data["Kewirausahaan"]), 4.0, 0.0)
Manajemen_Pemasaran = st.number_input("Masukkan Nilai Manajemen Perusahaan", 0.0, max(data["Manajemen_Pemasaran"]), 4.0, 0.0)
Metodologi_Penelitian = st.number_input("Masukkan Nilai Metodologi Peneltian", 0.0, max(data["Metodologi_Penelitian"]),
                                        4.0, 0.0)
Sistem_Rantai_Pasok = st.number_input("Masukkan Nilai Sistem Rantai Pasok", 0.0, max(data["Sistem_Rantai_Pasok"]), 4.0, 0.0)
Tugas_Akhir_1 = st.number_input("Masukkan Nilai Tugas Akhir 1", 0.0, max(data["Tugas_Akhir_1"]), 4.0, 0.0)
Tugas_Akhir_2 = st.number_input("Masukkan Nilai Tugas Akhir 2", 0.0, max(data["Tugas_Akhir_2"]), 4.0, 0.0)

if st.button('Prediksi'):
    input_nilai_mata_kuliah = [Bahasa_Inggris, Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar,
                               Pengantar_Teknik_Industri, Sistem_Lingkungan_Industri, Fisika_Dasar_2,
                               Kalkulus_2, Menggambar_Teknik, Pengantar_Ekonomika,
                               Praktikum_Fisika_Dasar, Praktikum_Menggambar_Teknik, Aljabar_Linear,
                               Ergonomi_dan_Perancangan_Sistem_Kerja_1, Material_Teknik, Mekanika_Teknik,
                               Pemrograman_Komputer, Penelitian_Operasional_1, Praktikum_Material,
                               Praktikum_Pemrograman_Komputer, Proses_Manufaktur, Statistika_Industri,
                               Analisis_Biaya, Ergonomi_dan_Perancangan_Sistem_Kerja_2, Matematika_Optimasi,
                               Penelitian_Operasional_2, Perancangan_dan_Pengembangan_Produk,
                               Praktikum_Perancangan_Teknik_Industri_1, Psikologi_Industri, Statistika_Industri_2,
                               Ekonomi_Teknik, Mekatronika_dan_Opimasi_Sistem_Produksi, Pemodelan_Sistem,
                               Pengendalian_dan_Penjaminan_Mutu, Perancangan_Tata_Letak_Fasilitas,
                               Perencanaan_dan_Pengendalian_Produksi, Praktikum_Perancangan_Teknik_Industri_2,
                               Analisis_dan_Peancangan_Perusahaan, Analisis_dan_Perancangan_Sistem_Informasi,
                               Kerja_Praktek, Kesehatan_dan_Keselamatan_Kerja,
                               Organisasi_dan_Manajemen_Perusahaan_Industri, Praktikum_Perancangan_Teknik_Industri_3,
                               Simulasi_Komputer, Sistem_Produksi, Kewirausahaan, Manajemen_Pemasaran,
                               Metodologi_Penelitian, Sistem_Rantai_Pasok, Tugas_Akhir_1,
                               Tugas_Akhir_2]  # Tambahkan nilai mata kuliah lain
    prediction = predict_lulus_tepat_waktu(input_nilai_mata_kuliah)

    if 'name' in st.session_state:
        st.write(f"Halo {st.session_state.name}!")

    if 'age' in st.session_state:
        st.write(f"NIM {st.session_state.age}.")

    if prediction == 1:
        st.write('Hasil Prediksi: Lulus Tepat Waktu')
    else:
        st.write('Hasil Prediksi: Tidak Lulus Tepat Waktu')

    st.write("Apabila Anda ingin bertanya, silahkan hubungi dhinihamidah11@gmail.com")
