n=int(input("enter the number"))
rev=0
while(n!=0):
    rev=rev*10
    rev=rev+n%10
    n=n//10
    print("reverse number of entered number is",rev)
