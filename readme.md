1. Business Question
    * Kapan penjualan tertinggi terjadi?
    * Bagaimana tren penjualan dari waktu ke waktu?
    * Apakah terdapat penurunan atau peningkatan signifikan?
    * Produk atau strategi apa yang perlu dioptimalkan?
    

2. Data Wrangling
    * Data dibaca dari file CSV Amazon Sale Report
    * Kolom Date diubah menjadi format datetime
    * Data dengan nilai Amount kosong dihapus
    * Data dengan jumlah pembelian (Qty) ≤ 0 dihapus
    * Dilakukan pengecekan missing values untuk memastikan kualitas data


3. Insights (Analisis)
 A. Tren Penjualan Bulanan
    Berdasarkan grafik:
    Penjualan tertinggi terjadi pada bulan April 2022
    Pada bulan Maret 2022, penjualan masih sangat rendah (kemungkinan data belum penuh atau awal periode)
    Setelah puncak di April:
    Terjadi penurunan di bulan Mei
    Penurunan berlanjut di bulan Juni

    Kesimpulan:
    Ada lonjakan besar di April (kemungkinan karena promo/event)
    Setelah itu tren menunjukkan penurunan bertahap

 B. Produk Underperformer
    (Berdasarkan scatter plot yang dijalankan)
    Terdapat produk dengan:
        * Harga (Amount) tinggi
        * Namun jumlah terjual (Qty) rendah

    Kesimpulan:
    Beberapa produk kemungkinan overpriced
    Harga menjadi penghambat penjualan

 C. Analisis Kategori Produk
    (Berdasarkan bar chart)
    Ada kategori yang memberikan kontribusi penjualan paling besar
    Ada juga kategori dengan penjualan rendah

    Kesimpulan:
    Tidak semua kategori efisien
    Perlu fokus ke kategori dengan performa terbaik

 D. Analisis Lokasi (Kota)
    (Berdasarkan output top city)
    Beberapa kota memiliki jumlah order jauh lebih tinggi dibanding lainnya

    Kesimpulan:
    Permintaan tidak merata
    Ada kota yang menjadi market utama

 E. Status Order
    Mayoritas order kemungkinan berstatus delivered/shipped
    Ada sebagian yang cancelled atau returned

    Kesimpulan:
    Perlu perhatian pada order yang gagal agar tidak merugikan bisnis


4. Recommendation (Saran Bisnis)
    * Strategi Penjualan
    Maksimalkan strategi yang digunakan di bulan April (karena performa terbaik)
    Buat promo serupa di bulan berikutnya untuk menjaga tren

    * Optimasi Produk
    Evaluasi produk dengan harga tinggi tapi penjualan rendah
    Berikan:
        * diskon
        * bundling
        * atau repositioning harga
        
    * Fokus Kategori
    Tingkatkan stok dan promosi pada kategori dengan penjualan tinggi
    Kurangi investasi pada kategori yang kurang efisien

    * Target Lokasi
    Fokus marketing di kota dengan order tinggi
    Perluas promosi ke kota dengan potensi rendah

    * Perbaikan Operasional
    Kurangi jumlah order cancel/return
    Evaluasi:
        * pengiriman
        * kualitas produk
        * pelayanan

    * Kesimpulan Akhir
    Penjualan mencapai puncak di April 2022
    Setelah itu terjadi penurunan bertahap
    Terdapat ketidakseimbangan antara harga dan jumlah penjualan
    Beberapa kategori dan wilayah memiliki performa lebih baik dibanding lainnya