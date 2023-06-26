n=int(input("Enter number:"))
if n>1:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print("{} is not prime number".format(n))
            break
    else :
             print("{} is prime number".format(n))
else :
    print ("{} is not prime number".format(n))
             
    
