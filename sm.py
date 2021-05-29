s1=input('enter ur first word')
s2=input('enter ur second word')
for i in range(len(s1)):
    s="".join(s1[i]+s2[i])
    print(s,end="")
#s="".join(s)
#print(s)
