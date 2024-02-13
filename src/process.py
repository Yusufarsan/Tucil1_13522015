# Modul pemrosesan data dari masukkan user

def search(matrix, row_matrix, col_matrix, maxBufferSize, size, buffer, x, y, visitedMat, udahVertikal):   # Mengembalikan kumpulan buffer yang mungkin dalam bentuk list of list of str
    results = []  # Inisialisasi list untuk menyimpan semua kemungkinan array yang memenuhi syarat

    if len(buffer) == size or len(buffer) == maxBufferSize or maxBufferSize < size:
        return [(buffer.copy(), [(x, y)])]  # Jika buffer sudah mencapai panjang yang diinginkan, tambahkan ke hasil bersama dengan koordinatnya

    elif udahVertikal:
        for i in range(col_matrix):
            if not visitedMat[x][i]:
                visitedMat[x][i] = True
                buffer.append(matrix[x][i])
                results.extend(search(matrix, row_matrix, col_matrix, maxBufferSize, size, buffer, x, i, visitedMat, False))
                buffer.pop()  # Kembalikan kondisi buffer sebelumnya
                visitedMat[x][i] = False

    else:
        for i in range(row_matrix):
            if not visitedMat[i][y]:
                visitedMat[i][y] = True
                buffer.append(matrix[i][y])
                results.extend(search(matrix, row_matrix, col_matrix, maxBufferSize, size, buffer, i, y, visitedMat, True))
                buffer.pop()  # Kembalikan kondisi buffer sebelumnya
                visitedMat[i][y] = False

    # Tambahkan koordinat saat memperpanjang hasil
    for result in results:
        result[1].append((x, y))

    return results


def solusi(hasilSearch, sequences, reward_seq):
    # Mengembalikan hasil search yang paling optimal
    # hasilSearch: list of tuple of list of str and list of tuple of int
    # Mengembalikan poin tertinggi dan index hasilSearch yang paling optimal
    # Namun, jika hasilSearch kosong, maka mengembalikan 0 dan -1
    poin_arr =[0] * len(hasilSearch)  # Inisialisasi array untuk menyimpan poin dari setiap hasilSearch
    # Melakukan string matching dengan setiap buffer pada hasilSearch
    for i in range(len(hasilSearch)):
        for j in range(len(sequences)):
            # print("hasilSearch[i][0]: ", hasilSearch[i][0])
            # print("sequences[j]: ", sequences[j])
            poin_arr[i] += reward_seq[j] * matching(hasilSearch[i][0], sequences[j])
    # Mencari poin tertinggi
    poin = max(poin_arr)
    index = poin_arr.index(poin)
    
    return poin, index

def matching(buffer, sequence):
    # Mengembalikan 1 jika sequence ada di buffer, 0 jika tidak
    # buffer: list of str
    # sequence: list of str
    # Mengembalikan 1 jika sequence ada di buffer, 0 jika tidak
    # Menggunakan algoritma string matching (brute force)
    for i in range(len(buffer) - len(sequence) + 1):
        found = True
        for j in range(len(sequence)):
            if buffer[i+j] != sequence[j]:
                found = False
                break
        if found:
            return 1
    return 0