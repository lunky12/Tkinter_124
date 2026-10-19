
import tkinter as tk
from tkinter import ttk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("650x550")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Style
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TEntry", padding=6)
style.configure("TButton", font=("Arial", 11, "bold"), padding=8)

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#17365d"
)
judul.pack(pady=20)

# Frame untuk input nilai
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=5)

# Daftar mata pelajaran
mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sosiologi",
    "Geografi",
    "Informatika"
]

# Menyimpan input nilai
input_nilai = []

# Membuat 10 label dan input nilai dalam 2 kolom
for i, mapel in enumerate(mata_pelajaran):
    baris = i % 5
    kolom = (i // 5) * 2

    label = tk.Label(
        frame_input,
        text=mapel,
        font=("Arial", 10),
        bg="#f0f4f8",
        anchor="w",
        width=17
    )
    label.grid(row=baris, column=kolom, padx=8, pady=9, sticky="w")

    entry = ttk.Entry(frame_input, width=12)
    entry.grid(row=baris, column=kolom + 1, padx=8, pady=9)

    input_nilai.append(entry)

# Fungsi hasil prediksi
def hasil_prediksi():
    label_hasil.config(
        text="Hasil Prediksi: Teknologi Informasi",
        fg="#16803c"
    )

# Tombol prediksi
tombol_prediksi = ttk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol_prediksi.pack(pady=25)

# Frame hasil prediksi
frame_hasil = tk.Frame(
    root,
    bg="white",
    highlightbackground="#cbd5e1",
    highlightthickness=1
)
frame_hasil.pack(fill="x", padx=45, pady=5)

label_hasil = tk.Label(
    frame_hasil,
    text="Hasil prediksi akan muncul di sini",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#475569",
    pady=18
)
label_hasil.pack()

# Menjalankan aplikasi
root.mainloop()
