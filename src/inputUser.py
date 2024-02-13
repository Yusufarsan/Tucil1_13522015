# Modul input

import random
# Input dari File (TO DO VALIDASI TIAP MASUKKAN)
def inputFile():        # Diasumsikan masukkan file melalui txt sesuai dengan format yang diinginkan
    fileName = input("Masukkan nama file dengan ekstensinya: ")
    print()
    
    try:
        with open("../test/" + fileName, 'r') as file:
            # Membaca buffer_size
            buffer_size = int(file.readline())

            # Membaca matrix_width dan height dan memvalidasi bahwa matrix_width dan matrix_height harus berupa bilangan bulat yang lebih besar dari 0
            line = file.readline().strip()
            matrix_width, matrix_height = line.split()  # Memisahkan data menjadi dua bagian berdasarkan spasi
            if int(matrix_width) <= 0 or int(matrix_height) <= 0:
                raise ValueError("Lebar dan tinggi matrix harus lebih besar dari 0.")
            col_matrix = int(matrix_width)
            row_matrix = int(matrix_height)

            # Membaca Matrix
            matrix = []
            for _ in range(row_matrix):
                row = list(map(str, file.readline().strip().split()))
                # Pastikan panjang setiap baris sesuai dengan jumlah kolom yang diharapkan
                if len(row) != col_matrix:
                    raise ValueError("Kesalahan pada ukuran matrix.")
                # Memvalidasi setiap elemen matrix
                for elem in row:
                    if not (elem.isalnum() and len(elem) == 2):
                        raise ValueError("Setiap token dalam matrix harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
                    if (any(map(lambda x: x.isalpha(), elem)) and not elem.isupper()):
                        raise ValueError("Setiap token dalam matrix harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
                matrix.append(row)
            
            # Membaca banyak_seq dan memvalidasi bahwa banyak_seq harus berupa bilangan bulat yang lebih besar dari 0
            banyak_seq = int(file.readline().strip())
            if banyak_seq <= 0:
                raise ValueError("Banyak sequence harus lebih besar dari 0.")

            # Membaca sequences dan memvalidasi bahwa:
            # 1. Jumlah sequence yang dimasukkan sesuai dengan yang diinginkan
            # 2. Setiap sequence terdiri dari token yang harus alfanumerik dan terdiri dari dua buah karakter serta harus dalam bentuk uppercase
            # 3. Reward harus berupa bilangan bulat (bisa saja berupa bilangan negatif)
            sequences = []
            reward_seq = []
            for _ in range(banyak_seq):
                sequence_tokens = list(map(str, file.readline().strip().split()))
                sequences.append(sequence_tokens)
                reward_seq.append(int(file.readline().strip()))
                # if len(sequences[-1]) > buffer_size:
                #     raise ValueError("Sequence tidak boleh lebih panjang dari buffer.")
                # print(sequences[-1][0])
                # if not all(map(lambda x: x.isalnum() and len(x) == 2 and x.isupper(), sequences[-1])):
                #     raise ValueError("Setiap token dalam sequence harus alfanumerik dan terdiri dari dua buah karakter serta harus dalam bentuk uppercase.")
                for token in sequence_tokens:
                    if not (token.isalnum() and len(token) == 2):
                        raise ValueError("Setiap token dalam sequence harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
                    if (any(map(lambda x: x.isalpha(), token)) and not token.isupper()):
                        raise ValueError("Setiap token dalam sequence harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
            
            # Memvalidasi jika len(sequences) == banyak_seq
            if len(sequences) != banyak_seq:
                raise ValueError("Jumlah sequence yang dimasukkan tidak sesuai dengan yang diinginkan.")
            
            return buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq
            
    except FileNotFoundError:
        print(f"File {fileName} tidak ditemukan.")
        print()
        return inputFile()
    except ValueError as e:
        print("Terjadi kesalahan saat membaca file:", e)
        print()
        return inputFile()
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", e)
        print()
        return inputFile()

# Input dari Terminal
def inputTerminal():

    while True:
        try:
            banyak_token = int(input("Masukkan jumlah token unik: "))
            if banyak_token <= 0:
                print("Jumlah token unik harus lebih besar dari 0.\n")
            else:
                break
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    # Validasi:
    # 1. Jumlah token yang dimasukkan harus sesuai dengan yang diinginkan
    # 2. Setiap token harus unik
    # 3. Setiap token harus alfanumerik dan terdiri dari dua buah karakter serta harus dalam bentuk uppercase
    while True:
        # Menerima input token
        token = input("Masukkan token: ").split()
        
        # Memeriksa panjang token
        if len(token) != banyak_token:
            print(f"Jumlah token yang dimasukkan harus {banyak_token}")
            continue
        
        # Memeriksa uniknya setiap token
        if len(set(token)) != banyak_token:
            print("Setiap token harus unik")
            continue
        
        # Memeriksa setiap token secara terpisah
        for token_elem in token:
            if not (token_elem.isalnum() and len(token_elem) == 2):
                print("Setiap token dalam sequence harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
                break
            if (any(map(lambda x: x.isalpha(), token_elem)) and not token_elem.isupper()):
                print("Setiap token dalam sequence harus alfanumerik, terdiri dari dua buah karakter, dan dalam bentuk uppercase.")
                break
        else:
            # Jika semua token valid, keluar dari loop
            break
        
    print()
    
    while True:
        try:
            buffer_size = int(input("Masukkan ukuran buffer: "))
            if buffer_size <= 0:
                print("Ukuran buffer harus lebih besar dari 0.\n")
            else:
                break  # Keluar dari perulangan saat masukan valid
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    while True:
        try:
            col_matrix = int(input("Masukkan lebar matrix: "))
            if col_matrix <= 0:
                print("Lebar matrix harus lebih besar dari 0.\n")
            else:
                break  # Keluar dari perulangan saat masukan valid
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    while True:
        try:
            row_matrix = int(input("Masukkan tinggi matrix: "))
            if row_matrix <= 0:
                print("Tinggi matrix harus lebih besar dari 0.\n")
            else:
                break  # Keluar dari perulangan saat masukan valid
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    while True:
        try:
            banyak_seq = int(input("Masukkan banyak sequence: "))
            if banyak_seq <= 0:
                print("Banyak sequence harus lebih besar dari 0.\n")
            else:
                break  # Keluar dari perulangan saat masukan valid
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    while True:
        try:
            ukuran_max_seq = int(input("Masukkan ukuran maksimum sequence: "))
            if ukuran_max_seq <= 0:
                print("Ukuran maksimum sequence harus lebih besar dari 0.\n")
            else:
                break  # Keluar dari perulangan saat masukan valid
        except ValueError:
            print("Masukan harus berupa bilangan bulat.\n")
    print()

    print("-------------------------\n")

    matrix = []
    # melakukan random dari token yang dimasukkan dan menyusun nya sehingga terbentuk matrix sesuai dengan ukurannya
    for i in range(row_matrix):
        row = []
        for j in range(col_matrix):
            row.append(token[random.randint(0, banyak_token-1)])
        matrix.append(row)

    # Menampilkan matrix
    print("Berikut matriks permainan anda:")
    for i in range(row_matrix):
        for j in range(col_matrix):
            print(matrix[i][j], end=" ")
        print()
    print()

    # Proses me-random sequence dan reward
    sequences = []
    reward_seq = []
    for i in range(banyak_seq):
        # Melakukan random dari token yang dimasukkan untuk membentuk sequence
        sequence = ""
        for j in range(random.randint(1, ukuran_max_seq)):
            sequence = sequence + token[random.randint(0, banyak_token-1)]
            if j != ukuran_max_seq-1:
                sequence = sequence + " "
        sequences.append(sequence)
        # Melakukan random reward untuk setiap sequence dari 1 hingga 50
        reward_seq.append(random.randint(-50, 50))                              # Concern: Reward bisa negatif

    # Menampilkan sequence dan reward
    print("Berikut sequence dan rewardnya:")
    for i in range(banyak_seq):
        print(f"Sequence {i+1}: {sequences[i]} \nReward: {reward_seq[i]}")
        print()

    return buffer_size, col_matrix, row_matrix, matrix, banyak_seq, sequences, reward_seq