file=open('word.txt','r')
contents=file.read()
words=contents.split()
sentences=contents.split(".")
lower=upper=digits=special=0
for ch in contents:
    if(ch.islower()):
        lower+=1
    elif(ch.isupper()):
        upper+=1
    elif(ch.isdigit()):
        digits+=1
    elif(ch!=" "):
        special+=1
print("Contents of the file : ",contents.strip())
print("Number of sentences:",len(sentences)-1)
print("Number of words:",len(words))
print("Number of lowercase charactes:",lower)
print("Number of uppercase characters:",upper)
print("Number of special characters:",special-1)
