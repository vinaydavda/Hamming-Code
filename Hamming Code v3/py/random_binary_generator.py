## Binary Generator Coded by Vinay...

import random
import sys

#size=int(input("Size for generated array : "))

size=int(sys.argv[1])

#size=100

binary=''

for x in range(size):
    binary+=str(random.randint(0,1))

print(binary)


## Coded by Vinay K. Davda 10:11 PM 27 AUGUST 2018
