a=int(input("a="))
n=int(input("n="))
ans=1
while n>0:
    if n&1:
        ans=ans*a
    n>>=1
    a*=a
print(ans)

