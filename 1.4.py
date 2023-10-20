import random

alph1 = 'abcdefghijklmnopqrstuvwxyz'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
sequence = random.sample(letters, 26)
random.shuffle(sequence)
alph2 = ''.join([str(elem) for elem in sequence])
print(alph2)

A1=[]
for i in alph1:
    for j in alph1:
        itog=""+i+j
        A1.append(itog)

A2=[]
for i in alph2:
    for j in alph2:
        itog=""+i+j
        A2.append(itog)


s = input('введите сообщение')
res=''
'''
for i in range(len(...),step=2)
a1=massiv[i]
a2=i+1
a=a1+a2

===
'''

for i in range (0,len(s),2):
     a=s[i:i+2]
     for j in range(len(A1)):
         if (a == A1[j]):
             res+= A2[j]
             break
print(res)

deres=''
for i in range (0,len(res),2):
    f=res[i:i+2]
    for j in range (len(A2)):
        if (f == A2[j]):
            deres+=A1[j]
            break
print(deres)


'''
for i in range(len(A1)):
    if (a==A1[i]):
        a=A2[i]
        break
'''



'''
j = 0
for i in range(len(s)):
    if s[i].isalpha():
       res += alph2[alph1.index(s[j])]
       j+=1
    else:
        res += s[i]
print(res)

f=0
deres=''
for i in range (len(res)):
    if res[i].isalpha():
        deres+= alph1[alph2.index(res[f])]
        f+=1
    else:
        deres += res[i]
print(deres)
'''