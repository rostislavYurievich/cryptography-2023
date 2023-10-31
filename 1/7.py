MIN = 97
MAX = 123

def shift(ch, shift_num):
    if not(ch.isalpha()):
        return ch
    if shift_num<0:
        return shift(ch, MAX-MIN+shift_num)
    return chr((ord(ch.lower())-MIN+shift_num)%(MAX-MIN)+MIN)

def cypher(string, shift_num=(MAX-MIN)//2):
    return "".join([shift(x,shift_num) for x in string])
    
a = input("Введите шифруемую строку ")
a1 = cypher(a)
a2 = cypher(a1)
print("Зашифрованная строка {a1}".format(a1=a1))
print("Разшифрованная строка {a1}".format(a1=a2))