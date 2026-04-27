# ==============================
# ANALISIS PERFORMA PENJUALAN (AMAZON DATA)
# ==============================

# 1. IMPORT LIBRARY
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 2. LOAD DATA
# ==============================
df = pd.read_csv('Amazon Sale Report.csv', low_memory=False)

print("=== DATA AWAL ===")
print(df.head())

# ==============================
# 3. INSPEKSI DATA
# ==============================
print("\n=== INFO DATA ===")
print(df.info())

print("\n=== KOLOM ===")
print(df.columns)

print("\n=== CEK NULL ===")
print(df.isnull().sum())

# ==============================
# 4. DATA CLEANING
# ==============================

# ubah kolom tanggal
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# hapus data yang tidak punya Amount
df = df[df['Amount'].notnull()]

# hapus data jumlah <= 0
df = df[df['Qty'] > 0]

# ==============================
# 5. ANALISIS TREND PENJUALAN
# ==============================
df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Amount'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.show()

# ==============================
# 6. PRODUK UNDERPERFORMER
# ==============================
plt.figure(figsize=(6,4))
plt.scatter(df['Amount'], df['Qty'])
plt.xlabel('Harga (Amount)')
plt.ylabel('Jumlah Terjual (Qty)')
plt.title('Produk Underperformer')
plt.show()

# ==============================
# 7. ANALISIS KATEGORI PRODUK
# ==============================
category_sales = df.groupby('Category')['Amount'].sum().sort_values()

plt.figure(figsize=(8,5))
category_sales.plot(kind='barh')
plt.title('Total Penjualan per Kategori')
plt.xlabel('Total Penjualan')
plt.ylabel('Kategori')
plt.show()

# ==============================
# 8. TOP KOTA DENGAN ORDER TERBANYAK
# ==============================
top_city = df['ship-city'].value_counts().head(5)

print("\n=== TOP 5 KOTA DENGAN ORDER TERBANYAK ===")
print(top_city)

# ==============================
# 9. STATUS ORDER
# ==============================
status_count = df['Status'].value_counts()

print("\n=== STATUS ORDER ===")
print(status_count)

# ==============================
# SELESAI
# ==============================
print("\nAnalisis selesai")