# Python3 code to demonstrate 
# Filling plaintextbets 
# using naive method 

# initializing empty list 
plaintextlist = [] 

# using naive method 
# for filling plaintextbets 
numberOfplaintextbets = int(input())
plaintext = str(input())

for i in range(0, numberOfplaintextbets): 
	plaintextlist.append(plaintext[i]) 
	i = i + 1

# printing resultant list 
print ("List after insertion : " + str(plaintextlist)) 
