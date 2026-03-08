Berdasarkan sleuruh analisis eksplorasi data yang telah dilakukan pada dataset pohon di New York, berikut adalah beberapa temuan utama yang dapat disimpulkan:

Struktur Dataset: Dataset memiliki 10 kolom dengan berbagai tipe data, termasuk numerik dan kategorikal. Terdapat beberapa kolom yang memiliki banyak nilai kosong (missing values).
Missing Values: Kolom-kolom seperti 'stump_diam', 'stump_diam', dan 'stump_diam' memiliki jumlah missing values yang signifikan. Visualisasi heatmap menunjukkan pola missing values yang tersebar di beberapa kolom.
Statistik Deskriptif: Diameter pohon (DBH) memiliki rata-rata sekitar 10.5 inci dengan rentang yang cukup luas, menunjukkan adanya variasi ukuran pohon yang signifikan.
Distribusi Data: Kesehatan pohon didominasi oleh kategori 'Good', diikuti oleh 'Fair' dan 'Poor'. Distribusi diameter pohon menunjukkan bahwa sebagian besar pohon memiliki DBH di bawah 20 inci, dengan beberapa outlier yang memiliki DBH lebih besar.
Analisis Hubungan Antar Variabel: Boxplot menunjukkan bahwa pohon dengan kesehatan 'Poor' cenderung memiliki DBH yang lebih kecil dibandingkan dengan pohon yang sehat ('Good'), meskipun terdapat beberapa outlier di kategori 'Poor'.
Kesimpulan: EDA ini memberikan wawasan awal tentang kondisi pohon di New York, termasuk distribusi kesehatan dan ukuran pohon. Data ini dapat digunakan untuk analisis lebih lanjut, seperti prediksi kesehatan pohon berdasarkan fitur-fitur yang tersedia.
--- 1. Import Library ---
import pandas as pd import matplotlib.pyplot as plt import seaborn as sns
