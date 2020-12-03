import string
import math

def baris_maks(panjang_plaintext):
    pola1 = 1
    pola2 = 2 
    while (pola1 < panjang_plaintext):
        pola1 = pola1 + pola2
    return math.ceil(math.sqrt(pola1))


def enkripsi(barismaks, plaintext, kolom, baris):
    array = [['' for y in range(int(kolom))] for x in range(int(baris))]
    penghitung_string = 0
    hasil_enkripsi = ''
    dikunjungi = [False for x in range(kolom)]

    for i in range(int(baris)):
        kolom_mulai = baris - i - 1
        for j in range(int(kolom)):
            if (j >= kolom_mulai and j < kolom - kolom_mulai) and len(plaintext) >= penghitung_string:   
                if penghitung_string >= len(plaintext):
                    array[i][j] = 'x'
                else:
                    array[i][j] = plaintext[penghitung_string]
                    penghitung_string = penghitung_string + 1
        if penghitung_string == len(plaintext):
            break

    for i in range(int(baris)):
        for j in range(int(kolom)):
            if dikunjungi[j] == False:
                for k in range(int(baris)):
                    if array[k][j] != '':
                        hasil_enkripsi = hasil_enkripsi + array[k][j]
                dikunjungi[j] = True
            else:
                continue

    return hasil_enkripsi

c

def main():
    plaintext = 'ikanhiumakantomat'
    panjang_plaintext = len(plaintext)
    barismaks = baris_maks(panjang_plaintext)
    kolom, baris = 2 * barismaks - 1, barismaks
    print(enkripsi(barismaks, plaintext, kolom, baris))

    ciphertext = "tkxhaxkinxiautxnmoxamxaxx"
    panjang_ciphertext = len(ciphertext)
    barismaks = baris_maks(panjang_ciphertext)
    kolom, baris = 2 * barismaks - 1, barismaks
    print(dekripsi(barismaks, ciphertext, kolom, baris))

if __name__ == "__main__":
    main()