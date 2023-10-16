MIN = 32
MAX = 127

def shift(ch, shift_num):
    if shift_num<0:
        return shift(ch, MAX-MIN+shift_num)
    return chr((ord(ch)-MIN+shift_num)%(MAX-MIN)+MIN)

def cypher(string, shift_num):
    return "".join([shift(x,shift_num) for x in string])

def decypher(string, shift_num):
    return cypher(string, -shift_num)
    
a = input("Введите шифруемую строку ")
a1 = cypher(a,6)
a2 = decypher(a1,6)
print("Зашифрованная строка {a1}\nРазшифрованная строка {a2}".format(a1=a1, a2=a2))