from itertools import repeat

a = input("Введите шифруемую строку ")

def cypher(string, column):
    l = list()
    for i in range(column):
        l.append(string[i::column])
    return "".join(l)

def decypher(string, column):
    l = list(repeat("",len(string)//column+1))
    i = 0
    cnt = 0
    last_line_len = len(string)%column
    for c in string:
        if i >= (len(string)//column+(0 if cnt>=last_line_len else 1)):
            i = 0
            cnt+=1
        l[i]+=c
        i+=1  
    return "".join(l)

a1 = cypher(a,6)
a2 = decypher(a1,6)
print("Зашифрованная строка {a1}\nРазшифрованная строка {a2}".format(a1=a1, a2=a2))