import numpy as np
from inputUser import *
from process import *
from output import *
import time

print('''\nWelcome to Cyberpunk 2077
Breach Protocol
-------------------------

Pilih opsi input
1. File
2. Terminal
''')

opsiInput = None
while opsiInput not in [1, 2]:
    try:
        opsiInput = int(input("Masukkan opsi input (1 atau 2): "))
        if opsiInput not in [1, 2]:
            print("Masukkan tidak valid. Harap masukkan angka 1 atau 2.")
    except ValueError:
        print("Masukkan tidak valid. Harap masukkan angka 1 atau 2.")
        
print("-------------------------\n")

if opsiInput==1:
    buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq = inputFile()

else:
    buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq = inputTerminal()
#   int        , int       , int       , int[][], int      , int[][]  , int[]

print("-------------------------\n")

##############################
# Nge test file inputUser.py
# print("Hasil input:")
# print("Ukuran buffer:", buffer_size)
# print("Ukuran kolom matrix:", col_matrix)
# print("Ukuran baris matrix:", row_matrix)
# print("Matrix:")
# print(matrix)
# print("Banyak sequence:", banyak_seq)
# print("Sequence:")
# print(sequences)
# print("Reward sequence:")
# print(reward_seq)
# print("-------------------------\n")
# exit()
##############################

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
    print("Tidak ada buffer yang mungkin")
    hasilSearch = [([], [(0, 0)])]
else:
    hasilSearch = []
    for i in range (minLen, buffer_size+1):
        result = search(matrix, row_matrix, col_matrix, buffer_size, i, buffer, 0, 0, visitedMat, True)
        if result != [([], [(0, 0)])]:              
            # print(result)
            # print()
            # print(result[0][0])
            # print(result[0][1])
            # print()
            hasilSearch.extend(result)

        else:
            hasilSearch.extend(result)
            print("Tidak ada buffer yang mungkin")


    
# Mencari solusi yang paling optimal
poin, index = solusi(hasilSearch, sequences, reward_seq)

# Hitung waktu eksekusi dalam milidetik
execution_time_ms = (time.time() - start_time) * 1000

outputTerminal(hasilSearch, poin, index)
    
# Cetak waktu eksekusi ke terminal
print(f"\nWaktu eksekusi program: {execution_time_ms:.2f} ms")

# Apakah ingin menyimpan hasil
save = ""
while save not in ['Y', 'N', 'y', 'n']:
    save = input("\nApakah ingin menyimpan solusi? (y/n): ")
    save = save.upper()  # Ubah input menjadi huruf besar (uppercase)
    if save not in ['Y', 'N', 'y', 'n']:
        print("\nMasukkan tidak valid. Silakan masukkan 'y' atau 'n'.")
print()

if save == 'Y':
    outputFile(hasilSearch, poin, index, execution_time_ms)
    print("Solusi berhasil disimpan.")
else:
    print("Solusi tidak disimpan.")