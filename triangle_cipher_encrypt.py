import string
import math

def tokenizing_plaintext(plaintext, panjang_plaintext):
	#tokenizing and append to list
	plaintext_list = [] 
	for i in range(panjang_plaintext): 
		plaintext_list.append(plaintext[i]) 
	print ("Your Plaintext is: " + str(plaintext_list))


pola2 = 2
def baris_maks(panjang_plaintext):
	pola1 = 1
	while (pola1 < panjang_plaintext):
		pola1 = pola1 + pola2
	return int(math.sqrt(pola1))

def indeks_kiri(baris_maks):
	start = 0
	pola1 = 1
	ciphertext_start = []
	for i in range (baris_maks):
		ciphertext_start.append(start)
		start = start + pola1
		pola1 = pola1 + pola2
	print (ciphertext_start)

#kolom, baris = baris_maks(panjang_plaintext), 2 * baris_maks(panjang_plaintext) - 1
#matrix = [[0 for x in range(kolom)] for y in range(baris)]

def main():
	plaintext = str(input("Input Plaintext: "))
	panjang_plaintext = len(plaintext)

	tokenizing_plaintext(plaintext, panjang_plaintext)
	tingkat_segitiga = baris_maks(panjang_plaintext)
	indeks_kiri(tingkat_segitiga)
	

if __name__ == "__main__":
	main()
