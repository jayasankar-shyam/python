n=int(input("Enter the number of elements"))
list=[]
for i in range(0,n):
	print("Enter element",i+1," :",end=" ")
	list.append(int(input()))
print(list)
x=int(input("Enter element to be removed : "))
while(x in list):
	list.remove(x)
print(list)
