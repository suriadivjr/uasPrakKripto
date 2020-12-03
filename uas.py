from tkinter import * 
import tkinter.messagebox
import math
import string

root = Tk()

root.geometry('1000x500')

entry1 = StringVar()
entry2 = StringVar()
hasilenkripsi = StringVar()
hasildekripsi = StringVar()

def enkripsicolumnar(input_teks, input_kunci):
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

def dekripsicolumnar(input_teks, input_kunci):
    jumlah_kolom = len(input_kunci)
    jumlah_baris = math.ceil(len(input_teks)/jumlah_kolom)
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

def colenk():
    teks = entry1.get()
    kunci = entry2.get()

    hasil_enkripsi = enkripsicolumnar(teks, kunci)  
    hasilenkripsi.set(hasil_enkripsi)   
    
def coldek():
    teks = entry1.get()
    kunci = entry2.get()

    hasil_dekripsi = dekripsicolumnar(teks, kunci)  
    hasildekripsi.set(hasil_dekripsi)

def baris_maks(panjang_plaintext):
    pola1 = 1
    pola2 = 2 
    while (pola1 < panjang_plaintext):
        pola1 = pola1 + pola2
    return math.ceil(math.sqrt(pola1))


def enkripsitriangle(barismaks, plaintext, kolom, baris):
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

def dekripsitriangle(barismaks, plaintext, kolom, baris):
    array = [['' for y in range(int(kolom))] for x in range(int(baris))]
    hasil_dekripsi = ''
    penghitung_string = 0
    dikunjungi = [False for x in range(kolom)]

    for j in range(0, barismaks):
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

    for j in range(barismaks, kolom):
        penghitung_kosong = 0
        for k in range(1, barismaks):
            if penghitung_string == len(plaintext):
                break

            if j <= penghitung_kosong + barismaks:
                array[k][j] = plaintext[penghitung_string]
                penghitung_string =  penghitung_string + 1
            penghitung_kosong = penghitung_kosong + 1 

    for i in range(baris):
        for j in range(kolom):
            if array[i][j] != '':
                hasil_dekripsi = hasil_dekripsi + array[i][j]
    return hasil_dekripsi

def trienk():
    teks = entry1.get()
    panjang_plaintext = len(teks)
    barismaks = baris_maks(panjang_plaintext)
    kolom, baris = 2 * barismaks - 1, barismaks
    
    hasil_enkripsi = enkripsitriangle(barismaks, teks, kolom, baris)  
    hasilenkripsi.set(hasil_enkripsi)  

def tridek():
    teks = entry1.get()
    panjang_ciphertext = len(teks)
    barismaks = baris_maks(panjang_ciphertext)
    kolom, baris = 2 * barismaks - 1, barismaks

    hasil_dekripsi = dekripsitriangle(barismaks, teks, kolom, baris)  
    hasildekripsi.set(hasil_dekripsi)

def dropdown():
        print("hasilnya...")

def dropdowncolenk():
        
        label_1 = Label(root, text = "Masukkan PlainTeks")
        label_1.grid(row = 0, column=0)
        
        Entry(root, textvariable = entry1).grid(row=0, column=1, sticky=E) #entry textbox
        
        label_2 = Label(root, text = "Masukkan Kunci")
        label_2.grid(row = 1, column=0)
        
        Entry(root, textvariable = entry2).grid(row=1, column=1, sticky=E) #entry textbox

        hasil_Button = Button(root, text = "Enkripsi", command=colenk)
        hasil_Button.grid(row = 2, column=0)

        Label(root, textvariable = hasilenkripsi).grid(row=2, column=1, sticky=E) #entry textbox
        

def dropdowncoldek():

        label_1 = Label(root, text = "Masukkan Ciphertext")
        label_1.grid(row = 0, column=0)
        
        Entry(root, textvariable = entry1).grid(row=0, column=1, sticky=E) #entry textbox
        
        label_2 = Label(root, text = "Masukkan Kunci")
        label_2.grid(row = 1, column=0)
        
        Entry(root, textvariable = entry2).grid(row=1, column=1, sticky=E) #entry textbox

        hasil_Button = Button(root, text = "Dekripsi", command=coldek)
        hasil_Button.grid(row = 2, column=0)

        Label(root, textvariable = hasildekripsi).grid(row=2, column=1, sticky=E) #entry textbox

def dropdowntrienk():
        
        label_1 = Label(root, text = "Masukkan Teks")
        label_1.grid(row = 0, column=0)
        
        Entry(root, textvariable = entry1).grid(row=0, column=1, sticky=E) #entry textbox

        hasil_Button = Button(root, text = "Enkripsi", command=trienk)
        hasil_Button.grid(row = 2, column=0)

        Label(root, textvariable = hasilenkripsi).grid(row=2, column=1, sticky=E) #entry textbox

def dropdowntridek():
    
        label_1 = Label(root, text = "Masukkan Ciphertext")
        label_1.grid(row = 0, column=0)
        
        Entry(root, textvariable = entry1).grid(row=0, column=1, sticky=E) #entry textbox
        

        hasil_Button = Button(root, text = "Dekripsi", command=tridek)
        hasil_Button.grid(row = 2, column=0)

        Label(root, textvariable = hasildekripsi).grid(row=2, column=1, sticky=E) #entry textbox

#def reset():
#    destroy(Label)
#    destroy(Entry)

def main():
    label_1 = Label(root, text = "CALCULATOR CRYPTOGRAPHY : COLUMNAR & TRIANGLE")
    menu = Menu(root)
    root.config(menu = menu)
   
    columnarmenu = Menu(menu)
    menu.add_cascade(label = "Columnar", menu = columnarmenu)
    
    columnarmenu.add_command(label = "Enkripsi", command = dropdowncolenk)
    columnarmenu.add_command(label = "Dekripsi", command = dropdowncoldek)
    columnarmenu.add_separator()
    #columnarmenu.add_command(label = "Reset", command = reset)
    columnarmenu.add_command(label = "Exit", command = root.destroy)

    trianglemenu = Menu(menu)
    menu.add_cascade(label = "Triangle", menu = trianglemenu)
    trianglemenu.add_command(label = "Enkripsi", command = dropdowntrienk)
    trianglemenu.add_command(label = "Dekripsi", command = dropdowntridek)
    trianglemenu.add_separator()
    trianglemenu.add_command(label = "Exit", command = root.destroy)
    trianglemenu.add_separator()

    label_1 = Label(root, text = "CALCULATOR CRYPTOGRAPHY : COLUMNAR & TRIANGLE")
    root.mainloop()
    
    
if __name__ == "__main__":
    main()