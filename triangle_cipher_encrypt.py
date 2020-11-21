import string
import math

plaintext_list = [] 

#input
plaintext = str(input("Input Plaintext: "))

#tokenizing and append to list
for i in range(0, len(plaintext)): 
	plaintext_list.append(plaintext[i]) 
	i = i + 1

print ("Your Plaintext is: " + str(plaintext_list))

tingkat2 = 2
tingkat1 = 1
start = 0
banyak_tingkat1 = 0

while (tingkat1 < len(plaintext)):
	tingkat1 = tingkat1 + tingkat2
maks = int(math.sqrt(tingkat1))

tingkat1 = 1
ciphertext_start = []
j = 0
for i in range (0, maks):
	ciphertext_start.append(start)
	while (start < tingkat1):
		print(plaintext_list[start])
		start = start + 1
	print ('-------')
	start = start + tingkat1
	tingkat1 = tingkat1 + tingkat2