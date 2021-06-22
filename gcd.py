n1=int(input('enter n1'))
n2=int(input('enter n2'))
if n1<n2:
    n1,n2=n2,n1
for i in range(n2,0,-1):
    if n1%i==0 and n2%i==0:
        print(f"gcd of {n1} and {n2} is {i}")
        break
