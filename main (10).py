#code by Vidhiya S B
n=int(input())
m=n
c=3
a=0
while(n>0):
    d=n%10
    n=n//10
    a+=int(d**c)
    c-=1
if(m==a):
    print("It is a Disarium Number")
else:
    print("It is not a Disarium Number")
    