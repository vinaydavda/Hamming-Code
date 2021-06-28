## Coded by Vinay K. Davda

import sys

#smsg=input("SENDER : ")

#vinn=open("binary.txt","r")

smsg=str(sys.argv[1])

smsg_arr=[]
new_msg_arr=[]#it is backup of smsg_arr
for x in smsg:
        smsg_arr.append(int(x))
        new_msg_arr.append(int(x))


sl=len(smsg_arr)

sfac=[1]
sval=1
while sval < (sl+1):
	sval*=2
	sfac.append(sval)

#print("sfac : ",sfac)

len_sfac=len(sfac)
s_count=0

for x in range(0,len_sfac):
	cur_fac=sfac[x]#start from 0
	if(len(smsg_arr)>=cur_fac):
		smsg_arr.insert((cur_fac-1),'S{}'.format(cur_fac))
		s_count+=1

sl=len(smsg_arr)##VERY IMPORTANT -- never forget it...#it is new length after adding R values...




for v in range(0,s_count):# v = 0 to 4
    n=('{}'.format(sfac[v]))# 1
    val="S"+n#R1 R2 R4 R8 R16....#R1
    #print(r_val)
    
    if val in smsg_arr:#R1 in scale
        f=int(n)#here first time f=1 #f=1
        locals()['s{}_arr'.format(f)]=[]
        s_point=int(n)-1

        while s_point < sl:
            flag=0
            while flag < f:
                if s_point < sl:
                    locals()['s{}_arr'.format(f)].append(smsg_arr[s_point])
                    s_point+=1
                flag+=1
            s_point+=f
        locals()['s{}_arr'.format(f)].pop(0)
        #==#print('s{}_arr'.format(f)," : ",locals()['s{}_arr'.format(f)])


s_store=[]
s_data=[]
for z in range(0,s_count):
	check='S'+str(sfac[z])
	if check in smsg_arr:
		#print(check)
		s_val=('{}'.format(sfac[z]))
		s_store.append(int(s_val))
		n=0
		locals()['S{}'.format(sfac[z])]=0
		for d in locals()['s{}_arr'.format(sfac[z])]:
			if d == 1:
				n+=1
		if n%2 != 0:
			locals()['S{}'.format(sfac[z])]=1
		#==#print('S'+str(s_store[z])," : ",locals()['S{}'.format(sfac[z])])
		s_data.append(locals()['S{}'.format(sfac[z])])



####---S value insertion starts---###

s_count=0
for x in range(0,len_sfac):#0123
	cur_fac=sfac[x]#1248
	if(len(smsg_arr)>=cur_fac):
		new_msg_arr.insert((cur_fac-1),s_data[x])
		s_count+=1

#print("s_count : ",s_count)
#=#print("new_msg_arr [updated] : ",new_msg_arr)

new_msg=""
for c in new_msg_arr:
	new_msg+=str(c)

#print("Sending this Encoded msg... : ",new_msg)
print(new_msg)
#print("------------------------------")


#Coded by Vinay K. Davda 10:13 PM 27 AUGUST 2018
