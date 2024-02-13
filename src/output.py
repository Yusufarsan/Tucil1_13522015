# Modul output

def outputTerminal(hasilSearch, poin, index):
    # Menampilkan hasil search yang paling optimal ke terminal
    # hasilSearch: list of tuple of list of str and list of tuple of int
    # poin: int
    # index: int
    # Menampilkan hasil search yang paling optimal
    noSolution = True
    for i in range(len(hasilSearch)):
        if hasilSearch[i][0] != ([], [(0, 0)]):
            noSolution = False
            break

    if noSolution or poin == 0:
        print("Tidak ada solusi yang mungkin.\nPoin: 0")
        
    else:
        print("Hasil solusi yang paling optimal:")
        print("Poin:", poin)
        for i in range(len(hasilSearch[index][0])):
            print(hasilSearch[index][0][i], end=" ")
        print()
        for i in range(len(hasilSearch[index][1])-2, -1, -1):
            x, y = hasilSearch[index][1][i]
            x += 1  # Tambahkan 1 pada absis
            y += 1  # Tambahkan 1 pada ordinat
            print(f"({y}, {x})", end=" ")  # Cetak dengan urutan yang dibalik
        print()

def outputFile(hasilSearch, poin, index, exe_time):
    # Meminta nama file dari pengguna
    nama_file = input("Masukkan nama file dengan ekstensinya: ")

    # Membuka file dengan mode menulis (w)
    with open("../test/" + nama_file, 'w') as file:
        noSolution = True
        for i in range(len(hasilSearch)):
            if hasilSearch[i][0] != ([], [(0, 0)]):
                noSolution = False
                break

        if noSolution or poin == 0:
            file.write("0\nTidak ada solusi yang mungkin.\n")
        else:
            file.write(str(poin) + "\n")
            for i in range(len(hasilSearch[index][0])):
                file.write(str(hasilSearch[index][0][i]) + " ")
            file.write("\n")
            for i in range(len(hasilSearch[index][1])-2, -1, -1):
                x, y = hasilSearch[index][1][i]
                x += 1  # Tambahkan 1 pada absis
                y += 1  # Tambahkan 1 pada ordinat
                file.write(f"{y}, {x}\n")
            file.write("\n")
        file.write(f"{exe_time:.2f} ms\n")