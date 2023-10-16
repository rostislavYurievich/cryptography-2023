#a = input("Введите шифруемую строку ")
a = "abcdefghijk0123456789"
""" 
abcdefghijk

012345
abcdef
ghijk

024135
acebdf
gikhj

agciekbhdjf
"""
from itertools import repeat

def cypher(string, column):
    l = list()
    for i in range(column):
        l.append(string[i::column])
    return "".join(l[::2]+(l[1::2]))

def decypher(string, column):
    l = list(repeat("",len(string)//column+1))
    i = 0
    last_line_len = len(string)%column-1
    for c in string:
        l[i]+=c
        i+=1
        if i == (len(string)//column+(0 if i==last_line_len else 1)):
            i = 0
    return l

a1 = cypher(a,6)
a2 = decypher(a1,6)
print("Зашифрованная строка {a1}\nРазшифрованная строка {a2}".format(a1=a1, a2=a2))