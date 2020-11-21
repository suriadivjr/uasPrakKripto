# Python3 code to demonstrate 
# Filling alphabets 
# using naive method 

# initializing empty list 
test_list = [] 

# using naive method 
# for filling alphabets 
numberOfAlphabets = int(input())
alpha = str(input())

for i in range(0, numberOfAlphabets): 
	test_list.append(alpha[i]) 
	i = i + 1

# printing resultant list 
print ("List after insertion : " + str(test_list)) 
