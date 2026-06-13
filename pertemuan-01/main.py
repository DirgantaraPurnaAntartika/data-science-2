"""Pertemuan 01 - Pengenalan Data Science.

Contoh mini pipeline: membuat data, memahami variabel, dan mengambil insight awal.
"""

import pandas as pd


def main():
    data = {
        "nama": ["Andi", "Budi", "Citra", "Dina", "Eka"],
        "jam_belajar": [2, 4, 3, 5, 1],
        "nilai": [70, 85, 78, 92, 60],
    }
    df = pd.DataFrame(data)

    print("Data awal:")
    print(df)

    print("\nRingkasan statistik:")
    print(df[["jam_belajar", "nilai"]].describe())

    korelasi = df["jam_belajar"].corr(df["nilai"])
    print(f"\nKorelasi jam belajar dan nilai: {korelasi:.2f}")

    rata_rata = df["nilai"].mean()
    print(f"Rata-rata nilai: {rata_rata:.2f}")


if __name__ == "__main__":
    main()
