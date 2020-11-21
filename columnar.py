import math

def enkripsi(input_teks, input_kunci):
    jumlah_kolom = len(input_kunci)
    jumlah_baris = math.ceil(len(input_teks)/jumlah_kolom)
    matriks_inisialisasi =[['x' for y in range(jumlah_kolom)]
                        for x in range(jumlah_baris)]
    penghitung_string = 0
    hasil_enkripsi = ''
    urutan = [0 for x in range(jumlah_kolom)]
    dikunjungi = [False for x in range(jumlah_kolom)]

    for i in range(jumlah_kolom):
        urutan[i] = ord(input_kunci[i])

    urutan.sort()

    for i in range(jumlah_baris):
        for j in range(jumlah_kolom):
            matriks_inisialisasi[i][j] = input_teks[penghitung_string]
            penghitung_string = penghitung_string + 1
            
            if penghitung_string == len(input_teks):
                break

        if penghitung_string == len(input_teks):
            break

    for i in range(jumlah_kolom):
        for j in range(jumlah_kolom):
            if (urutan[i] == ord(input_kunci[j])) and dikunjungi[j] == False:
                for k in range(jumlah_baris):
                    hasil_enkripsi = hasil_enkripsi + matriks_inisialisasi[k][j]
                
                dikunjungi[j] = True
            
            else:
                continue

    return hasil_enkripsi

def dekripsi(input_teks, input_kunci):
    jumlah_kolom = len(input_kunci)
    jumlah_baris = math.ceil(len(input_teks)/jumlah_kolom)
    print(jumlah_baris)
    matriks_inisialisasi =[['x' for y in range(jumlah_kolom)]
                        for x in range(jumlah_baris)]
    dikunjungi = [False for x in range(jumlah_kolom)]
    penghitung_string = 0
    hasil_dekripsi = ''
    urutan = [0 for x in range(jumlah_kolom)]

    for i in range(jumlah_kolom):
        urutan[i] = ord(input_kunci[i])

    urutan.sort()
    
    for i in range(jumlah_kolom):
        for j in range(jumlah_kolom):
            if (urutan[i] == ord(input_kunci[j])) and dikunjungi[j] == False:
                for k in range(jumlah_baris):
                    matriks_inisialisasi[k][j] = input_teks[penghitung_string]
                    penghitung_string = penghitung_string + 1

                    if penghitung_string == len(input_teks):
                        break
                
                dikunjungi[j] = True

            else:
                continue

            if penghitung_string == len(input_teks):
                break
            
        if penghitung_string == len(input_teks):
            break
            
    for i in range(jumlah_baris):
        for j  in range(jumlah_kolom):
            hasil_dekripsi = hasil_dekripsi + matriks_inisialisasi[i][j]

    return hasil_dekripsi

def columnar(input_mode, input_teks, input_kunci):
    if input_mode == '1':
        hasil_enkripsi = enkripsi(input_teks, input_kunci)
        print("Hasil enkripsi : " + hasil_enkripsi)

    elif input_mode == '2':
        hasil_dekripsi = dekripsi(input_teks, input_kunci)
        print("Hasil dekripsi: " + hasil_dekripsi)

def main():
    print("Masukkan mode (1 untuk enkripsi, 2 untuk dekripsi) : ")
    input_mode = input()
    if input_mode != '1' or input_mode != 2:
        print("Input salah!")

    print("Masukkan teks : ")
    input_teks = input()

    print("Masukkan kunci : ")
    input_kunci = input()

    columnar(input_mode, input_teks, input_kunci)
    
if __name__ == "__main__":
    main()