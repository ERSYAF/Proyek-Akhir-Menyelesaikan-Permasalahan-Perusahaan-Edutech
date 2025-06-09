# Proyek-Akhir-Menyelesaikan-Permasalahan-Perusahaan-Edutech
## Business Understanding

Sebagai institusi pendidikan tinggi, Jaya Jaya Institut telah membuktikan dirinya dalam menghasilkan lulusan-lulusan yang kompeten dan berprestasi. Namun, di balik pencapaian tersebut, institusi ini menghadapi tantangan yang cukup krusial: meningkatnya jumlah mahasiswa yang gagal menyelesaikan pendidikan atau keluar sebelum lulus.

Untuk mengantisipasi hal ini, JJI (Jaya Jaya Institut) berinisiatif melakukan deteksi dini terhadap mahasiswa yang berisiko mengalami dropout, agar dapat diberikan intervensi dan pendampingan yang tepat sasaran. Dalam proyek ini, Anda berperan sebagai data scientist yang bertanggung jawab untuk mengeksplorasi data mahasiswa dan merancang pendekatan analitik yang mampu mengurangi angka putus studi secara signifikan.

### Permasalahan Bisnis

1. Jumlah mahasiswa yang gagal menyelesaikan studi masih tergolong tinggi.
2. Belum tersedia mekanisme prediktif untuk mendeteksi potensi dropout sejak dini.
3. Kurangnya optimalisasi pemanfaatan data analitik dalam proses pendampingan akademik.
4. Risiko menurunnya reputasi institusi akibat tingginya tingkat putus studi.
5. Dibutuhkan pendekatan strategis berbasis data yang efektif untuk menanggulangi masalah dropout.

### Cakupan Proyek

Proyek ini akan mencakup langkah-langkah berikut:

1. **Analisis Data**: Mengumpulkan dan mengevaluasi data mahasiswa serta analisis terhadap data siswa untuk memahami pola dan faktor yang berkaitan dengan dropout.
2. **Pra-pemrosesan Data**: Menyiapkan dan membersihkan data agar layak untuk dianalisis lebih dalam.
3. **Pengembangan Model Machine Learning**: Membangun model machine learning untuk deteksi dropout.
4. **Evaluasi Model**: Mengukur akurasi dan performa model.
5. **Pembuatan Dashboard**: Menyajikan hasil analisis secara visual dengan mengembangkan dashboard interaktif untuk membantu pengambilan keputusan.
6. **Rekomendasi Solusi**: Menyampaikan rekomendasi strategis berdasarkan hasil analisis data untuk menurunkan angka dropout.

### Persiapan

#### Sumber Data

Dataset yang digunakan dalam proyek ini tersedia di repositori berikut: [Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance). Dataset tersebut mencakup informasi tentang performa siswa, termasuk data akademik, demografi, serta faktor lainnya yang relevan untuk keperluan analisis. Beberapa kolom yang terdapat dalam dataset antara lain:

| **Nama Kolom**                               | **Deskripsi**                                          |
| -------------------------------------------- | ------------------------------------------------------ |
| Marital_status                               | Status perkawinan siswa.                               |
| Application_mode                             | Jenis pendaftaran saat mendaftar.                      |
| Application_order                            | Urutan pengajuan pendaftaran.                          |
| Course                                       | Program studi yang diambil oleh siswa.                 |
| Daytime_evening_attendance                   | Jenis kehadiran (siang/malam).                         |
| Previous_qualification                       | Pendidikan terakhir yang dimiliki.                     |
| Previous_qualification_grade                 | Nilai dari pendidikan terakhir.                        |
| Nacionality                                  | Kewarganegaraan siswa.                                 |
| Mothers_qualification                        | Tingkat pendidikan ibu.                                |
| Fathers_qualification                        | Tingkat pendidikan ayah.                               |
| Mothers_occupation                           | Pekerjaan ibu.                                         |
| Fathers_occupation                           | Pekerjaan ayah.                                        |
| Admission_grade                              | Nilai saat masuk ke institusi.                         |
| Displaced                                    | Status apakah siswa berpindah tempat tinggal.          |
| Educational_special_needs                    | Status kebutuhan pendidikan khusus.                    |
| Debtor                                       | Status apakah siswa memiliki utang.                    |
| Tuition_fees_up_to_date                      | Status pelunasan biaya kuliah.                         |
| Gender                                       | Jenis kelamin siswa.                                   |
| Scholarship_holder                           | Status penerima beasiswa.                              |
| Age_at_enrollment                            | Usia saat pendaftaran.                                 |
| International                                | Apakah siswa berasal dari luar negeri.                 |
| Curricular_units_1st_sem_credited            | Jumlah SKS semester pertama yang diakui.               |
| Curricular_units_1st_sem_enrolled            | Jumlah SKS semester pertama yang diambil.              |
| Curricular_units_1st_sem_evaluations         | Jumlah evaluasi yang dilakukan di semester pertama.    |
| Curricular_units_1st_sem_approved            | Jumlah mata kuliah semester pertama yang lulus.        |
| Curricular_units_1st_sem_grade               | Rata-rata nilai pada semester pertama.                 |
| Curricular_units_1st_sem_without_evaluations | Jumlah mata kuliah tanpa evaluasi di semester pertama. |
| Curricular_units_2nd_sem_credited            | SKS semester kedua yang diakui.                        |
| Curricular_units_2nd_sem_enrolled            | SKS semester kedua yang diambil.                       |
| Curricular_units_2nd_sem_evaluations         | Evaluasi pada semester kedua.                          |
| Curricular_units_2nd_sem_approved            | Mata kuliah semester kedua yang lulus.                 |
| Curricular_units_2nd_sem_grade               | Rata-rata nilai semester kedua.                        |
| Curricular_units_2nd_sem_without_evaluations | Jumlah mata kuliah semester kedua tanpa evaluasi.      |
| Unemployment_rate                            | Tingkat pengangguran.                                  |
| Inflation_rate                               | Tingkat inflasi.                                       |
| GDP                                          | Produk Domestik Bruto.                                 |
| Status                                       | Status akhir siswa (dropout, lulus, dll.).             |

Kolom-kolom di atas memberikan informasi penting yang dapat digunakan dalam analisis dan pembuatan model prediktif.

#### Setup Environment

1. **Pasang Dependensi**
   Lakukan pemasangan seluruh paket yang dibutuhkan menggunakan file `requirements.txt` dengan perintah:

   ```bash
   pip install -r requirements.txt
   ```

2. **Download Dataset**
   Ambil dataset melalui link yang tersedia dan tempatkan file tersebut di folder proyek Anda.

3. **Mulai Jupyter Notebook**
   Jalankan Jupyter Notebook untuk melakukan eksplorasi data dan membangun model machine learning.

## Business Dashboard

### Deskripsi Dashboard

Dashboard dirancang menggunakan Metabase untuk menyajikan informasi siswa secara interaktif kepada para stakeholder. Visualisasi yang tersedia mencakup statistik dropout, distribusi nilai, serta variabel-variabel yang memengaruhi kinerja akademik siswa. Dengan dashboard ini, pengguna dapat mengidentifikasi pola dan tren penting yang berguna dalam proses pengambilan keputusan berbasis data.

### Panduan Akses Dashboard

Untuk mengakses dashboard yang dibuat di Metabase, ikuti langkah-langkah berikut:

1. Buka peramban web dan arahkan ke: [Metabase Dashboard](http://localhost:3000).
2. Masukkan informasi login berikut:

   - **Email**: `root@gmail.com`
   - **Kata Sandi**: `root123`

3. Setelah berhasil login, Anda akan diarahkan ke halaman utama. Pilih tampilan dashboard yang ingin dianalisis untuk melihat beragam visualisasi data.

---

## Menjalankan Prototipe Sistem Machine Learning

Ikuti petunjuk berikut untuk mengoperasikan sistem machine learning yang telah dikembangkan:

1. **Instalasi Dependensi**
   Pastikan semua pustaka yang dibutuhkan telah terpasang dengan menjalankan:

   ```bash
   pip install -r requirements.txt
   ```

2. **Menjalankan Aplikasi Streamlit**
   Aplikasi menggunakan Streamlit sebagai tampilan antarmuka. Jalankan aplikasi dengan:

   ```bash
   streamlit run app.py
   ```

3. **Akses Aplikasi dari Browser**
   Sistem akan berjalan secara lokal dan bisa dibuka di:
   [http://localhost:3000/](http://localhost:3000/)
   Selain itu, versi online yang telah di-deploy dapat diakses di:
   [https://proyek-akhir-menyelesaikan-permasalahan-perusahaan-edutech-sv7.streamlit.app/](https://proyek-akhir-menyelesaikan-permasalahan-perusahaan-edutech-sv7.streamlit.app/)

4. **Mengoperasikan Aplikasi**

   - Isi data mahasiswa pada formulir, seperti status pernikahan, program studi, nilai kualifikasi sebelumnya, dan data lain yang diperlukan.
   - Klik tombol "Prediksi Dropout" untuk mendapatkan hasil prediksi risiko dropout berdasarkan data yang diisi.
   - Dan juga bisa klik tombol "Prediksi Acak" untuk melihat prediksi menggunakan data acak sebagai simulasi.

5. **Memahami Output Prediksi**

   - Jika hasil prediksi menunjukkan Risiko DROP OUT Tinggi, aplikasi akan menampilkan persentase risiko beserta indikator visual berwarna merah sebagai peringatan.
   - Jika hasil prediksi menunjukkan Risiko DROP OUT Rendah, aplikasi akan menampilkan persentase risiko beserta indikator visual berwarna hijau yang menandakan risiko rendah.

Prototipe ini dirancang untuk mendukung institusi pendidikan dalam mengidentifikasi siswa yang rentan terhadap dropout, serta memfasilitasi tindakan intervensi yang tepat waktu.

## Conclusion

Analisis yang dilakukan melalui dashboard “Performance Students” di Jaya Jaya Institut mengungkap bahwa tingginya angka dropout dipengaruhi oleh sejumlah faktor utama. Faktor-faktor tersebut meliputi keterlambatan pembayaran biaya kuliah,kurangnya dukungan berupa beasiswa, serta tingginya angka dropout pada program studi tertentu seperti Teknologi Produksi Biofuel dan Teknik Informatika. Selain itu, mahasiswa yang mendaftar pada usia muda, berjenis kelamin laki-laki, dan berstatus debitur juga lebih berisiko mengalami dropout.

Dengan adanya dashboard interaktif dan model prediksi berbasis machine learning, institusi dapat dengan cepat mengidentifikasi mahasiswa yang berisiko dan memberikan pendampingan yang tepat. Hal ini diharapkan dapat menurunkan tingkat dropout serta meningkatkan reputasi institusi dalam jangka panjang.

### Rekomendasi Action Items

Berikut beberapa langkah strategis yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan retensi mahasiswa:

- Mengembangkan sistem deteksi dini menggunakan machine learning yang mampu mengidentifikasi mahasiswa dengan risiko tinggi dropout berdasarkan data akademik, kondisi keuangan, dan faktor demografi.
- Memperluas dukungan finansial melalui peningkatan akses beasiswa serta program keringanan biaya, terutama bagi mahasiswa dari latar belakang ekonomi kurang mampu atau yang belum menyelesaikan pembayaran.
- Meningkatkan mutu proses belajar dan bimbingan akademik pada semester pertama, termasuk pelaksanaan program mentoring dan tutoring untuk membantu mahasiswa baru beradaptasi dan mencapai prestasi.
- Melakukan tinjauan dan perbaikan kurikulum serta metode pengajaran di program studi dengan tingkat dropout yang tinggi, serta menyediakan alternatif seperti kelas malam untuk memberikan fleksibilitas belajar.
- Menyelenggarakan layanan konseling dan program pengembangan karakter guna mendukung kebutuhan psikologis dan sosial mahasiswa, khususnya bagi mahasiswa baru yang rentan terhadap tekanan akademik dan persoalan pribadi.
