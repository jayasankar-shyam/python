tup=(1,2,3,4,5,6,7,8,9)
e_tup=()
o_tup=()
for i in range (0,len(tup)):
    if(tup[i]%2==0):
        e_tup+=(tup[i],)
    else:
         o_tup+=(tup[i],)
print("Original tuple : ",tup)
print("Even tuple : ",e_tup)
print("Odd tuple : ",o_tup)
