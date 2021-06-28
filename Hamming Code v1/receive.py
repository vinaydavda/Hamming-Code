rmsg=input("RECEIVER : ")
#print("rmsg : ",rmsg)

rmsg_arr=[]
org_rmsg_arr=[]
for x in rmsg:
    rmsg_arr.append(int(x))
    org_rmsg_arr.append(int(x))
#print("rmsg_arr : ",rmsg_arr)

rl=len(rmsg_arr)
#print("rl : ",rl)

rfac=[1]
rev_rfac=[1]
rval=1
while rval < (rl+1):
    rval*=2
    if rval < (rl+1):
        rfac.append(rval)
        rev_rfac.append(rval)
#print("rfac : ",rfac)


### GETTING S1 S2...
s_store=[]
s_data=[]

print(rfac)
print(rmsg_arr)
for x in rfac:
    locals()['S{}'.format(x)]=rmsg_arr[x-1]
    print('S{}'.format(x)," : ",locals()[('S{}'.format(x))])
###########    


##Reversing factorials...
rev_rfac.reverse()
#print("rev_rfac : ",rev_rfac)
len_rfac=len(rev_rfac)
#print("len_rfac : ",len_rfac)

for x in range(0,len_rfac):#123
    rem=rev_rfac[x]-1
    if len(rmsg_arr) > 0:
            rmsg_arr.pop(rem)

#print("rmsg_arr [without R] : ",rmsg_arr)



##Converted Received string from list for checking purpose...
rmsg_wor=''

for x in rmsg_arr:
        rmsg_wor+=str(x)

print("rmsg_without_r [for checking Purpose] : ",rmsg_wor)

#================
## Adding R values
#================

r_count=0

for x in range(0,len_rfac):
	cur_fac=rfac[x]#start from 0
	if(len(rmsg_arr)>=cur_fac):
		rmsg_arr.insert((cur_fac-1),'R{}'.format(cur_fac))
		r_count+=1
#print("rmsg_arr : ",rmsg_arr)


#================
## r_arr finding...
#================

for v in range(0,r_count):# v = 0 to 4
    n=('{}'.format(rfac[v]))# 1
    r_val="R"+n#R1 R2 R4 R8 R16....#R1
    #print(r_val)
    
    if r_val in rmsg_arr:#R1 in smsg
        f=int(n)#here first time f=1 #f=1
        locals()['r{}_arr'.format(f)]=[]
        r_point=int(n)-1
        #print("s_point : ",s_point)

        while r_point < rl:
            flag=0
            while flag < f:
                if r_point < rl:
                    locals()['r{}_arr'.format(f)].append(rmsg_arr[r_point])
                    r_point+=1
                flag+=1
            r_point+=f
        if len('r{}_arr'.format(f)) > 0:
                locals()['r{}_arr'.format(f)].pop(0)
        #==#print('r{}_arr'.format(f)," : ",locals()['r{}_arr'.format(f)])

#================
## R value finding...
#================


r_store=[]
r_data=[]
for z in range(0,r_count):
	check='R'+str(rfac[z])
	if check in rmsg_arr:
		#print(check)
		val=('{}'.format(rfac[z]))
		r_store.append(int(val))
		num=0
		locals()['R{}'.format(rfac[z])]=0
		for d in locals()['r{}_arr'.format(rfac[z])]:
			if d == 1:
				num+=1
		if num%2 != 0:
			locals()['R{}'.format(rfac[z])]=1
		#==#print('R'+str(r_store[z])," : ",locals()['R{}'.format(rfac[z])])
		r_data.append(locals()['R{}'.format(rfac[z])])

#print("r_store : ",r_store)
#print("r_data : ",r_data)

#==#print("operated_rmsg_arr : ",rmsg_arr)
#==#print("org_rmsg_arr : ",org_rmsg_arr)



#################################################
##########   Combination Starts Here   ##########
#################################################
###########  - Code by Vinay Davda -  ###########
#################################################

#==#print("------------------------------")
#==#for x in s_store:    
    #==#print('s{}_arr'.format(x),' : ',locals()['s{}_arr'.format(x)])
    #==#print('S{}'.format(x),' : ',locals()['S{}'.format(x)])
    #==#print('r{}_arr'.format(x),' : ',locals()['r{}_arr'.format(x)])
    #==#print('R{}'.format(x),' : ',locals()['R{}'.format(x)])
    #==#print("------------------------")

error_arr=[]

for x in r_store:
        cur_s=locals()['S{}'.format(x)]
        cur_r=locals()['R{}'.format(x)]

        if cur_s != cur_r:
                error_arr.append(x)
#==#print("error_arr : ",error_arr)


#Finding Error Bit
error_bit_place=-1#starts from 0 index that's why here -1

for x in error_arr:
        error_bit_place+=x

#==#print("error_bit_place : ",error_bit_place)

#==#print("org_rmsg_arr [old] : ",org_rmsg_arr)

##Changing Error Bit
if error_bit_place != -1:
        if org_rmsg_arr[error_bit_place] == 0:
                org_rmsg_arr[error_bit_place]=1
        elif org_rmsg_arr[error_bit_place] == 1:
                org_rmsg_arr[error_bit_place]=0

#==#print("org_rmsg_arr [updated] : ",org_rmsg_arr)


##Correct msg without R values:
for x in rev_rfac:
        if len(org_rmsg_arr) > 0:
                org_rmsg_arr.pop(x-1)


##Receiver Msg

real_msg=''

for x in org_rmsg_arr:
        real_msg+=str(x)

print("Real Msg : ",real_msg)


#DEVELOPED BY VINAY K. DAVDA
