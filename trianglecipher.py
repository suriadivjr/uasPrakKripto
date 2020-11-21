plaintext_list = [] 

#input
number_of_alphabets = int(input())
plaintext = str(input())

#tokenizing and append to list
for i in range(0, number_of_alphabets): 
	plaintext_list.append(plaintext[i]) 
	i = i + 1

print ("List after insertion : " + str(plaintext_list)) 