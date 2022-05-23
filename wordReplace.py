a=input("Enter the sentence : ")
old=input("Enter word to be replaced : ")
new=input("Enter the new word : ")
words=a.split()
b=""
for i in words:
    if(i==old):
        b=b+" "+new
    else:
        b=b+" "+i
print(b)
