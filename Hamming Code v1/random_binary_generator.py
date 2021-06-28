## Binary Generator Coded by Vinay...

import random

size=int(input("Size for generated array : "))

binary=''

for x in range(size):
    binary+=str(random.randint(0,1))

print(binary)


#Developed by VINAY K. DAVDA
