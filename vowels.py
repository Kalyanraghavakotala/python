word=input('enter word')
#word=word.lower()
v=('a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U')
for char in word:
    if char in v:
        print('contains vowels')
        break
else:
    print('not cntains vowels')
