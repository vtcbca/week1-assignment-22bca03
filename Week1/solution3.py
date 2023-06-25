# write  python script to enter any number ,if it is integer number, then check its palindrome or not
n=int(input("Enter number:"))
num=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if s==num:
    print("{} is palindrome number".format(num))
else:
    print("{} is not palindrome number".format(num))

      
