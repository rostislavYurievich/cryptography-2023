import random

alph1 = 'abcdefghijklmnopqrstuvwxyz'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

sequence = random.sample(letters, 26)

random.shuffle(sequence)
alph2 = ''.join([str(elem) for elem in sequence])
print(alph2)

s = input('введите сообщение')
res=''
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