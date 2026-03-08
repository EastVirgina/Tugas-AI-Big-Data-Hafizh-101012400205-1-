import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tree_census.csv', sep=';')
print(f"Data berhasil dimuat. Total baris: {len(df)}")

print("\n--- Struktur Dataset ---")
print(df.info())

print("\n--- Jumlah Missing Values per Kolom ---")
print(df.isnull().sum().sort_values(ascending=False).head(10))

plt.figure(figsize=(10,5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')

plt.title("Peta Missing Values dalam Dataset")
plt.show()

print("\n--- Statistik Deskriptif Diameter ---")
print(df[['tree_dbh', 'stump_diam']].describe())

plt.figure(figsize=(8,5))
sns.countplot(x='health', data=df, palette='viridis', order=['Good', 'Fair', 'Poor'])
plt.title("Distribusi Kesehatan Pohon di New York")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['tree_dbh'], bins=50, kde=True, color='forestgreen')

plt.title("Distribusi Diameter Pohon (DBH)")
plt.xlim(0, 60)
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='health', y='tree_dbh', data=df, palette='Set2')

plt.title("Hubungan Diameter Pohon dengan Status Kesehatan")
plt.ylim(0, 70) 
plt.show()