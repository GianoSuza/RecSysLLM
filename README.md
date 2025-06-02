# Book Recommendation System

## Kelompok 4

Anggota:

1. **Muhammad Naufal Arifin**: 1301220356
2. **Nadiella Fitantriani Putri**: 1301223195
3. **Rheno Febrian Cholistyo**: 1301220188
4. **Sakie Giano Suza**: 1301223205

## Deskripsi

Ini adalah sistem rekomendasi buku berbasis **Ollama** dan **Streamlit**. Sistem ini menggunakan model **nomic-embed-text:latest** dari Ollama untuk menghasilkan embeddings dari deskripsi buku, kemudian menggunakan **cosine similarity** untuk memberikan rekomendasi buku berdasarkan kemiripan deskripsi yang dimasukkan oleh pengguna.

## Persyaratan

Sebelum menjalankan kode ini, pastikan Anda telah menginstal semua persyaratan berikut:

1. **Ollama**: Anda harus menginstal Ollama untuk menggunakan model **nomic-embed-text:latest**. Pastikan untuk mengunduh dan mengonfigurasi Ollama sesuai dengan dokumentasi mereka.
2. **Streamlit**: Untuk menjalankan aplikasi web, Anda perlu menginstal **Streamlit**.
3. **Pandas**: Library untuk memanipulasi dataset dalam format CSV.
4. **Scikit-learn**: Digunakan untuk menghitung kemiripan menggunakan cosine similarity.

### Instalasi Persyaratan

1. **Ollama**: Anda dapat mengunduh Ollama dari [website resmi Ollama](https://ollama.com/). Setelah menginstal Ollama, Anda harus mengonfigurasi dan mengunduh model **nomic-embed-text:latest** dengan perintah berikut:

   ```bash
   ollama pull nomic-embed-text:latest
   ```

   Model **nomic-embed-text:latest** dapat ditemukan di [halaman Ollama](https://ollama.com/library/nomic-embed-text:latest).

2. **Instalasi Library yang Dibutuhkan**:  
   Gunakan perintah berikut untuk menginstal semua dependensi yang diperlukan:

   ```bash
   pip install ollama streamlit pandas scikit-learn
   ```

## Langkah Menjalankan

1. **Menyiapkan Folder dan Dataset**:

   - Pastikan file **`recommendation.py`** dan **`BooksDatasetClean.csv`** dalam **folder yang sama**.
   - Dataset `BooksDatasetClean.csv` berisi kolom-kolom berikut:

     - `Title`: Judul buku
     - `Authors`: Penulis buku
     - `Description`: Deskripsi singkat buku
     - `Category`: Kategori atau genre buku
     - `Price Starting With ($)`: Harga buku
     - `Publish Date (Month)`: Bulan publikasi buku
     - `Publish Date (Year)`: Tahun publikasi buku

2. **Menjalankan Aplikasi Streamlit**:  
   Setelah Anda menginstal semua persyaratan, buka terminal atau command prompt, arahkan ke folder tempat file **`recommendation.py`** dan **`BooksDatasetClean.csv`** disimpan, kemudian jalankan aplikasi dengan perintah berikut:

   ```bash
   streamlit run recommendation.py
   ```

   Aplikasi akan membuka antarmuka pengguna di browser, di mana Anda dapat memasukkan deskripsi buku dan mendapatkan rekomendasi berdasarkan kemiripan deskripsi tersebut dengan buku-buku yang ada di dataset.

3. **Fitur Sistem Rekomendasi**:

   - Masukkan deskripsi buku di kolom input.
   - Klik tombol "Get Recommendations".
   - Sistem akan menampilkan 5 buku teratas yang paling mirip dengan deskripsi yang dimasukkan.

   > **Catatan:** Pada saat memulai sistem dan mencari rekomendasi akan memakan beberapa waktu karena banyaknya data.

## Penjelasan Kode

1. **Dataset**: Kode ini memuat dataset yang berisi informasi buku dan membersihkan data dari entri yang tidak memiliki deskripsi (kolom `Description`).
2. **Ollama API**: Sistem menggunakan model `nomic-embed-text:latest` untuk menghasilkan embeddings dari deskripsi buku. Model ini diakses melalui API Ollama.
3. **Rekomendasi**: Menggunakan **cosine similarity** untuk menghitung kesamaan antara deskripsi buku yang dimasukkan pengguna dan buku-buku dalam dataset.
4. **Streamlit**: Antarmuka pengguna dibangun menggunakan **Streamlit**, memungkinkan pengguna untuk berinteraksi dengan sistem rekomendasi secara langsung.

## Troubleshooting

Jika Anda mengalami masalah dengan menjalankan aplikasi, pastikan:

- **Ollama** telah diinstal dan dikonfigurasi dengan benar, serta model **nomic-embed-text:latest** telah diunduh dengan benar.
- **Streamlit** dapat berjalan dengan lancar, pastikan tidak ada konflik dependensi.
- Dataset Anda sesuai dengan format yang diharapkan (CSV dengan kolom yang benar).
  "# RecSysLLM"
