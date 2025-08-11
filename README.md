

Prediksi Harga Mobil Bekas untuk Optimalisasi Bisnis Dealer
===========================================================

Proyek ini bertujuan untuk mengembangkan model _machine learning_ yang dapat memprediksi harga mobil bekas di pasar Arab Saudi secara akurat. Model ini dirancang untuk menjadi alat bantu strategis bagi dealer mobil **"Syari Mobil"** dalam mengoptimalkan proses akuisisi dan penjualan.

Latar Belakang
--------------

Syari Mobil adalah dealer mobil bekas yang model bisnisnya bergantung pada kemampuan untuk **membeli mobil dengan harga rendah** dan **menjualnya kembali dengan harga pasar yang kompetitif**. Saat ini, proses penilaian harga dilakukan sepenuhnya secara manual oleh agen, yang menimbulkan beberapa tantangan:

*   **Tidak Efisien:** Riset manual untuk setiap mobil memakan waktu yang signifikan.
    
*   **Tidak Konsisten:** Penilaian yang subjektif menyebabkan variasi harga yang tidak standar.
    
*   **Berisiko:** Kesalahan dalam penilaian dapat mengurangi margin keuntungan atau memperlambat perputaran inventaris.
    

Pernyataan Masalah
------------------

Untuk meningkatkan efisiensi dan profitabilitas, Syari Mobil memerlukan sebuah alat yang dapat memberikan **estimasi harga yang cepat, akurat, dan objektif** kepada agen di lapangan, menggantikan pendekatan yang berbasis intuisi dengan keputusan yang berbasis data.

Tujuan Proyek
-------------

Tujuan utama dari proyek ini adalah untuk membangun sebuah model prediksi harga yang dapat:

1.  **Memberikan Estimasi Harga Beli yang Optimal:** Membantu agen dalam proses negosiasi pembelian.
    
2.  **Menentukan Harga Jual yang Kompetitif:** Merekomendasikan harga jual yang wajar untuk mempercepat penjualan.
    
3.  **Meningkatkan Efisiensi Operasional:** Mengurangi waktu yang dihabiskan untuk riset manual.
    

Hasil Model
-----------

Setelah melalui proses _preprocessing_, _feature engineering_, dan _hyperparameter tuning_, model **XGBoost** terpilih sebagai model dengan performa terbaik.

### Metrik Evaluasi

Model ini dievaluasi menggunakan dua metrik utama:

*   **Mean Absolute Error (MAE): 3.200,92 SAR**
    
    *   Secara rata-rata, prediksi harga yang diberikan oleh model meleset sekitar 3.201 SAR dari harga sebenarnya.
        
*   **Mean Absolute Percentage Error (MAPE): 7,52%**
    
    *   Metrik ini menunjukkan bahwa rata-rata kesalahan prediksi hanya **7,52%** dari harga mobil, yang menandakan tingkat akurasi yang sangat tinggi dan andal untuk penggunaan bisnis.
        

### Analisis Performa Model

#### Plot Harga Aktual vs. Harga Prediksi

Plot ini menunjukkan korelasi yang sangat kuat antara harga yang diprediksi oleh model dengan harga pasar yang sebenarnya. Titik-titik data yang berkerumun rapat di sekitar garis diagonal adalah bukti visual yang meyakinkan bahwa model ini **konsisten dan dapat dipercaya**.

#### Faktor Penentu Harga (_Feature Importance_)

Analisis _feature importance_ menunjukkan bahwa model tidak hanya melihat spesifikasi dasar, tetapi juga telah belajar memahami dinamika pasar. Faktor terpenting yang memengaruhi prediksi adalah:

1.  **Penyimpangan Harga dari Rata-rata Merek (Price\_Deviation\_by\_Make):** Menunjukkan apakah sebuah mobil tergolong "mahal" atau "murah" untuk mereknya.
    
2.  **Kelas Mobil (car\_class):** Pengelompokan mobil ke dalam kelas "Standar", "Premium", atau "Mewah".
    
3.  **Detail Spesifik:** Seperti tipe mobil tertentu (misalnya, Prado) dan lokasi penjualan.
    

Kesimpulan dan Dampak Bisnis
----------------------------

Proyek ini berhasil mengembangkan model prediksi yang tidak hanya akurat secara statistik, tetapi juga relevan secara bisnis. Dengan tingkat kesalahan rata-rata hanya **7,52%**, model ini siap untuk diimplementasikan dan memberikan dampak signifikan bagi Syari Mobil.

### Dampak Bisnis yang Diharapkan:

*   **Optimalisasi Harga Akuisisi:** Memastikan pembelian mobil dilakukan dengan harga yang menguntungkan untuk memaksimalkan margin.
    
*   **Percepatan Penjualan:** Menentukan harga jual yang kompetitif untuk mempercepat perputaran inventaris.
    
*   **Peningkatan Efisiensi:** Mengurangi waktu riset manual dan menstandarkan proses penilaian di seluruh perusahaan.
    

Implementasi model ini akan menjadi langkah transformatif, mendorong Syari Mobil menuju pengambilan keputusan yang lebih cerdas dan berbasis data.
