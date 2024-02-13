# TIDAK SELESAI

import tkinter as tk
from tkinter import filedialog, messagebox
from inputUser import inputFile, inputTerminal
from process import search, solusi
from output import outputTerminal, outputFile
import numpy as np
import time

def run_program():
    global buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq
    global hasilSearch, poin, index, execution_time_ms
    
    # Ambil opsi input
    opsiInput = input_var.get()
    
    if opsiInput == 'File':
        filename = filedialog.askopenfilename(title="Pilih File")
        buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq = inputFile(filename)
    else:
        buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq = inputTerminal()

    # Catat waktu mulai eksekusi
    start_time = time.time()

    # Mencari panjang sequence terpanjang dan terpendek
    maxLen = len(sequences[0])
    minLen = len(sequences[0])
    for i in range(banyak_seq):
        if len(sequences[i]) > maxLen:
            maxLen = len(sequences[i])
        if len(sequences[i]) < minLen:
            minLen = len(sequences[i])

    # Mencari semua buffer yang mungkin
    buffer = []
    visitedMat = np.zeros((row_matrix, col_matrix), dtype=bool)
    for i in range(row_matrix):
        for j in range(col_matrix):
            visitedMat[i][j] = False

    if buffer_size < minLen:
        messagebox.showinfo("Informasi", "Tidak ada buffer yang mungkin")
        hasilSearch = [([], [(0, 0)])]
    else:
        hasilSearch = []
        for i in range (minLen, buffer_size+1):
            result = search(matrix, row_matrix, col_matrix, buffer_size, i, buffer, 0, 0, visitedMat, True)
            if result != [([], [(0, 0)])]:              
                hasilSearch.extend(result)
            else:
                hasilSearch.extend(result)
                messagebox.showinfo("Informasi", "Tidak ada buffer yang mungkin")

    # Mencari solusi yang paling optimal
    poin, index = solusi(hasilSearch, sequences, reward_seq)

    # Hitung waktu eksekusi dalam milidetik
    execution_time_ms = (time.time() - start_time) * 1000

    # Tampilkan hasil pada GUI
    outputTerminal(hasilSearch, poin, index)
    label_time.config(text=f"Waktu eksekusi program: {execution_time_ms:.2f} ms")

    # Munculkan dialog untuk menyimpan hasil jika user menginginkan
    if messagebox.askyesno("Simpan Solusi", "Apakah ingin menyimpan solusi?"):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Simpan Solusi")
        outputFile(hasilSearch, poin, index, execution_time_ms, filename)
        messagebox.showinfo("Informasi", "Solusi berhasil disimpan.")
    else:
        messagebox.showinfo("Informasi", "Solusi tidak disimpan.")

# Inisialisasi jendela Tkinter
root = tk.Tk()
root.title("Cyberpunk 2077 Breach Protocol")

# Buat label dan opsi input
label_input = tk.Label(root, text="Pilih opsi input:")
label_input.pack()

input_var = tk.StringVar()
input_var.set("File")  # Set default value
radio_file = tk.Radiobutton(root, text="File", variable=input_var, value="File")
radio_file.pack()
radio_terminal = tk.Radiobutton(root, text="Terminal", variable=input_var, value="Terminal")
radio_terminal.pack()

# Tombol untuk menjalankan program
button_run = tk.Button(root, text="Jalankan Program", command=run_program)
button_run.pack()

# Label untuk menampilkan waktu eksekusi program
label_time = tk.Label(root, text="")
label_time.pack()

# Menampilkan jendela
root.mainloop()
