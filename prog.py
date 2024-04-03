def is_armstrong(n):
    sum=0
    l=len(n)
    for  i in n:
        sum+=(int(i)**l)
    if sum==int(n):
        print(n,'is armstrong.')
    else:
        print(n,'Not armstrong.')

n=input('Enter Number: ')
is_armstrong(n)