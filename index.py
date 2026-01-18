import os
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# PATH & LOAD DATA
# ===============================
DATA_PATH = "data"             
FILE_NAME = "XAU_15m_data.csv"
FILE_PATH = os.path.join(DATA_PATH, FILE_NAME)

df = pd.read_csv(FILE_PATH, sep=';', skiprows=1, header=None)
df.columns = ["datetime", "open", "high", "low", "close", "volume"]

print("✅ Data berhasil dimuat!")
print(f"Total baris: {len(df)}")
print("Kolom:", df.columns.tolist())
print("\nContoh data:")
print(df.head())

# ===============================
# DATETIME & FILTER 2025
# ===============================
df["datetime"] = pd.to_datetime(df["datetime"], format="%Y.%m.%d %H:%M")
gold_2025 = df[df["datetime"].dt.year == 2025]

print(f"\n✅ Total data Gold tahun 2025: {len(gold_2025)} baris")
print("\n📊 Statistik Gold 2025:")
print(gold_2025.describe())

# ===============================
# PREP DATA TAMBAHAN
# ===============================
gold_2025["month"] = gold_2025["datetime"].dt.month
monthly_avg = gold_2025.groupby("month")["close"].mean()

gold_2025["MA20"] = gold_2025["close"].rolling(20).mean()
gold_2025["MA50"] = gold_2025["close"].rolling(50).mean()

# ===============================
# 1️⃣ GOLD PRICE (CLOSE)
# ===============================
plt.figure(figsize=(10,5))
plt.plot(gold_2025["datetime"], gold_2025["close"])
plt.title("Gold Price (Close) - 2025")
plt.xlabel("Tanggal")
plt.ylabel("Harga")
plt.grid(True)

# ===============================
# 2️⃣ AVERAGE PRICE PER MONTH
# ===============================
plt.figure(figsize=(10,5))
plt.bar(monthly_avg.index, monthly_avg.values)
plt.title("Average Gold Price per Month (2025)")
plt.xlabel("Bulan")
plt.ylabel("Harga Rata-rata")
plt.grid(True)

# ===============================
# 3️⃣ TRADING VOLUME
# ===============================
plt.figure(figsize=(10,5))
plt.plot(gold_2025["datetime"], gold_2025["volume"])
plt.title("Gold Trading Volume (2025)")
plt.xlabel("Tanggal")
plt.ylabel("Volume")
plt.grid(True)

# ===============================
# 4️⃣ DISTRIBUSI HARGA
# ===============================
plt.figure(figsize=(10,5))
plt.hist(gold_2025["close"], bins=50)
plt.title("Distribusi Harga Gold (2025)")
plt.xlabel("Harga")
plt.ylabel("Frekuensi")

# ===============================
# 5️⃣ BOXPLOT HARGA
# ===============================
plt.figure(figsize=(6,5))
plt.boxplot(gold_2025["close"])
plt.title("Boxplot Harga Gold (2025)")
plt.ylabel("Harga")

# ===============================
# 6️⃣ MOVING AVERAGE
# ===============================
plt.figure(figsize=(10,5))
plt.plot(gold_2025["datetime"], gold_2025["close"], label="Close")
plt.plot(gold_2025["datetime"], gold_2025["MA20"], label="MA20")
plt.plot(gold_2025["datetime"], gold_2025["MA50"], label="MA50")
plt.title("Gold Price with Moving Average (2025)")
plt.xlabel("Tanggal")
plt.ylabel("Harga")
plt.legend()
plt.grid(True)

# ===============================
# TAMPILKAN SEMUA CHART SEKALIGUS
# ===============================
plt.show()

# ===============================
# SAVE DATA
# ===============================
OUTPUT_PATH = os.path.join(DATA_PATH, "gold_2025.csv")
gold_2025.to_csv(OUTPUT_PATH, index=False)
print(f"\n✅ Data Gold 2025 berhasil disimpan ke: {OUTPUT_PATH}")
