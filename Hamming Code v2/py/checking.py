## String Checker coded by Vinay for Hamming Code...

import sys

str1=str(sys.argv[1])
str2=str(sys.argv[2])

#str1=input("Enter String 1 : ")
#str2=input("Enter String 2 : ")

str1_arr=[]
str2_arr=[]

for x in str1:
    str1_arr.append(int(x))
for x in str2:
    str2_arr.append(int(x))


z_str1_arr=[]
z_str2_arr=[]
z=1
for x in str1:
    z_str1_arr.append(x+str(z))
    z+=1
z=1
for x in str2:
    z_str2_arr.append(x+str(z))
    z+=1

#print(z_str1_arr)
#print(z_str2_arr)

indexes=[]
for x in z_str1_arr:
    ind=z_str1_arr.index(x)
    indexes.append(ind)

#print(indexes)   

#print("str1_arr : ",str1_arr)
#print("str2_arr : ",str2_arr)

print("")
print("=====ERROR-RESULT=====")
print("")
val=-1
for x in indexes:
    if str1_arr[x] != str2_arr[x]:
        val=str2_arr[x]
        place=x
        print("Error Bit in str2: ",val)
        print("Error Place : ",x+1)
        scope1=[]
        scope2=[]
        l=len(str2_arr)
        for x in range((x-2),(x+3)):
            if x >= 0 and x <= (l-1):
                scope1.append(str1_arr[x])
                scope2.append(str2_arr[x])
        print("Error Scope str1 : ",scope1)
        print("Error Scope str2 : ",scope2)
        print("")
            

if (val==-1):
    print("No Error Found")
    print("")

# Note : Error Place Starts from 1

## Coded by Vinay K. Davda Final Release 10:09 PM 27 AUGUST 2018
