import string

plaintext_list = [] 

#input
plaintext = str(input("Input Plaintext: "))

#tokenizing and append to list
for i in range(0, len(plaintext)): 
	plaintext_list.append(plaintext[i]) 
	i = i + 1

print ("List after insertion : " + str(plaintext_list)) 