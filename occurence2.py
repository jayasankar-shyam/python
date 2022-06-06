list=[]
n_list=[]
n=int(input("Enter the number of elements in the list : "))
for i in range(0,n):
    print("Enter element",i+1,":",end=" ")
    list.append(int(input()))
print(list)
x=int(input("Enter the element to be removed : "))
for i in range(0,n):
    if(list[i]!=x):
        n_list.append(list[i])
print("New List :",n_list)
