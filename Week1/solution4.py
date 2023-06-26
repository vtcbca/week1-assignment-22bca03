# write python program to check number is armstrong or not
n=int(input("Enter number:"))
s=0
num=n
while n>0:
    r=n%10
    n=n//10
    s=(r*r*r)+s
if s==num:
    print("{} is armstrong number".format(num))
else :
    print("{} is not armstrong number".format(num))
    
    
    
