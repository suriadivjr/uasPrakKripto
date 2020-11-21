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

#triangle cipher encryyption
def pascals_triangle(rows):
	result = []
	p = 1
	q = 1
	for count in range(rows):
		row = []
		for i in range(count + 1):
			row.append(plaintext_list[count])
			count += i+1
		p += q
		q += 1
		result.append(row)
	return result

# now we can print a result:
for row in pascals_triangle(5):
	print(row)