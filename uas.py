from tkinter import * 
import tkinter.messagebox
import math

root = Tk()

entry1 = StringVar()
entry2 = StringVar()
hasilenkripsi = StringVar()

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

"""def columnar(input_mode, input_teks, input_kunci):
    if input_mode == '1':
        hasil_enkripsi = enkripsi(input_teks, input_kunci)
        print("Hasil enkripsi : " + hasil_enkripsi)

    elif input_mode == '2':
        hasil_dekripsi = dekripsi(input_teks, input_kunci)
        print("Hasil dekripsi: " + hasil_dekripsi)"""

def dropdown():
        print("hasilnya...")

def colenk():
    teks = entry1.get()
    kunci = entry2.get()
    print(entry1.get())
    print(entry2.get())

    hasil_enkripsi = enkripsi(teks, kunci)  
    hasilenkripsi.set(hasil_enkripsi)
    print(hasilenkripsi.get())     
    
def coldek():
    hasil_dekripsi = dekripsi(input_teks, input_kunci)
    hasildekripsi(0,hasil_dekripsi)

def dropdowncolenk():
    
        label_1 = Label(root, text = "Masukkan Teks")
        label_1.grid(row = 0, column=0)
        
        Entry(root, textvariable = entry1).grid(row=0, column=1, sticky=E) #entry textbox
        
        label_2 = Label(root, text = "Masukkan Kunci")
        label_2.grid(row = 1, column=0)
        
        Entry(root, textvariable = entry2).grid(row=1, column=1, sticky=E) #entry textbox

        hasil_Button = Button(root, text = "Enkripsi", command=colenk)
        hasil_Button.grid(row = 2, column=0)

        Label(root, textvariable = hasilenkripsi).grid(row=2, column=1, sticky=E) #entry textbox
        
        """topframe = Frame(root)
        topframe.pack()
        button1 = Button(topframe, text = "Columnar", fg = "red")
        button1.pack()"""

def main():
    """print("Masukkan mode (1 untuk enkripsi, 2 untuk dekripsi) : ")
    input_mode = input()
    if input_mode != '1' or input_mode != 2:
        print("Input salah!")

    print("Masukkan teks : ")
    input_teks = input()

    print("Masukkan kunci : ")
    input_kunci = input()

    columnar(input_mode, input_teks, input_kunci)"""    

    menu = Menu(root)
    root.config(menu = menu)

    columnarmenu = Menu(menu)
    menu.add_cascade(label = "Columnar", menu = columnarmenu)
    columnarmenu.add_command(label = "Enkripsi", command = dropdowncolenk)
    columnarmenu.add_command(label = "Dekripsi", command = dropdown)
    columnarmenu.add_separator()
    columnarmenu.add_command(label = "Exit", command = dropdown)

    trianglemenu = Menu(menu)
    menu.add_cascade(label = "Triangle", menu = trianglemenu)
    trianglemenu.add_command(label = "Enkripsi", command = dropdown)
    trianglemenu.add_command(label = "Dekripsi", command = dropdown)
    trianglemenu.add_separator()
    trianglemenu.add_command(label = "Exit", command = dropdown)


    root.mainloop()
    
if __name__ == "__main__":
    main()
