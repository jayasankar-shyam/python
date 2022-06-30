file=open('nums.txt','r')
contents=file.read()
numbers=contents.split(',')
int_nums=[]
print("The file contents are : ",end="")
for i in numbers:
    print(i,end=" ")
    int_nums.append(int(i))
print("The prime numbers are : ",end="")
for num in int_nums:
     if (num > 1):
        for j in range(2,num):
            if (num%j == 0):
                flag=1
        if(flag==0):
            print(num,end=" ")
        flag=0
