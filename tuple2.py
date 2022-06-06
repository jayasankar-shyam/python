list=[]
n=int(input("Enter the number of elements in the tuple : "))
for i in range(0,n):
    print("Enter element",i+1,":",end=" ")
    list.append(int(input()))
tup=tuple(list)
e_tup=()
o_tup=()
for i in range (0,n):
    if(tup[i]%2==0):
        e_tup+=(tup[i],)
    else:
         o_tup+=(tup[i],)
print("Original tuple : ",tup)
print("Even tuple : ",e_tup)
print("Odd tuple : ",o_tup)
