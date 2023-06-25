string=input("Enter  string: ")
string1=string
res=string
for i in string:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        x = string.index(i)
        string= string[:x] + str(x) + string[x+1:]
print("Old string: ",string)
print("New string: ",string1)
