import string
import math

plaintext_list = [] 

#input
plaintext = str(input("Input Plaintext: "))

#tokenizing and append to list
for i in range(len(plaintext)): 
	plaintext_list.append(plaintext[i]) 
	i = i + 1
#print ("Your Plaintext is: " + str(plaintext_list))


pola2 = 2
pola1 = 1
start = 0
while (pola1 < len(plaintext)):
	pola1 = pola1 + pola2
maks = int(math.sqrt(pola1))

pola1 = 1
ciphertext_start = []
j = 0
for i in range (0, maks):
	ciphertext_start.append(start)
	start = start + pola1
	pola1 = pola1 + pola2
#print (ciphertext_start)

kolom, baris = maks, 2 * maks - 1
matrix = [[0 for x in range(kolom)] for y in range(baris)] 