n=int(input('enter'))
k=65
for i in range(n,0,-1):
    for j in range(1,i+1):
            print(chr(k),end=' ')
    print('\n')



n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print('\n')


n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n')



n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n//2)+1 or j==(n//2)+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n//2)+1 or j==(n//2)+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        for n in range(1,n//2):
            if i==n or j==n:
                print('*',end=' ')
        else:
             print(' ',end=' ')
    print('\n')

            
        

n=int(input())
for i in range(1,n+1):
    for j in range(n+1):
        if j>=i:
            print(" ",end=" ")
    else:
        print("*",end=" ")
    print()

