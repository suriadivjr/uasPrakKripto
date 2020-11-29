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

def dekripsi(barismaks, plaintext, kolom, baris):
    array = [['' for y in range(int(kolom))] for x in range(int(baris))]
    hasil_dekripsi = ''
    penghitung_string = 0
    dikunjungi = [False for x in range(kolom)]

    for j in range(kolom):
        if dikunjungi[j] == False and j < barismaks:
            penghitung_kosong = 1
            for k in range(barismaks):

                if penghitung_string == len(plaintext):
                    break

                if j >= barismaks - penghitung_kosong:
                    array[k][j] = plaintext[penghitung_string]
                    penghitung_string = penghitung_string + 1
                penghitung_kosong = penghitung_kosong + 1    
                
            dikunjungi[j] = True

            
        elif dikunjungi[j] == False and j > barismaks:
              
            penghitung_kosong = barismaks - 1
        
            for k in range(barismaks):
                print(k)
                print(j)
                if penghitung_string == len(plaintext):
                    break

                if j <= barismaks - penghitung_kosong:
                    array[k][j] = plaintext[penghitung_string]
                    penghitung_string = penghitung_string + 1
                penghitung_kosong = penghitung_kosong - 1
                
            dikunjungi[j] = True

        if penghitung_string == len(plaintext):
            break

    """"
    for i in range(kolom):
        if penghitung_string == len(plaintext):
            break
        if i < barismaks:
            penghitung_kosong = 1
            for j in range(barismaks):
                if penghitung_string == len(plaintext):
                    break
                if j >= barismaks - penghitung_kosong:
                    array[i][j] = plaintext[penghitung_string]
                    penghitung_string = penghitung_string + 1
            penghitung_kosong = penghitung_kosong + 1    
        else:
            penghitung_kosong = barismaks - 1
        
            for j in range(barismaks):
                if penghitung_string == len(plaintext):
                    break

                if j >= barismaks - penghitung_kosong:
                    array[i][j] = plaintext[penghitung_string]
                    penghitung_string = penghitung_string + 1

        penghitung_kosong = penghitung_kosong - 1
"""    
    return array

    for i in range(baris):
        for j in range(kolom):
            if array[i][j] != '':
                hasil_dekripsi = hasil_dekripsi + array[i][j]

    

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