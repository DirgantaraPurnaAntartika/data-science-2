"""Pertemuan 02 - Struktur Data Python, NumPy, dan Pandas."""

import numpy as np
import pandas as pd


IDENTITAS = {
    "Nama": "Dirgantara Purna Antartika",
    "NIM": "240401010001",
    "Kelas": "IF405",
    "Program Studi": "S1 Informatika",
}


def tampilkan_identitas():
    print("Identitas Mahasiswa")
    for label, nilai in IDENTITAS.items():
        print(f"{label}: {nilai}")
    print()


def main():
    tampilkan_identitas()

    nilai_list = [70, 85, 78, 92, 60]
    nilai_array = np.array(nilai_list)

    print("List Python:", nilai_list)
    print("Array NumPy:", nilai_array)
    print("Nilai + 5 dengan NumPy:", nilai_array + 5)

    df = pd.DataFrame(
        {
            "mahasiswa": ["Andi", "Budi", "Citra", "Dina", "Eka"],
            "kelas": ["IF401", "IF403", "IF401", "IF405", "IF403"],
            "nilai": nilai_array,
        }
    )

    print("\nDataFrame Pandas:")
    print(df)

    print("\nRata-rata nilai per kelas:")
    print(df.groupby("kelas")["nilai"].mean())


if __name__ == "__main__":
    main()
