alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = '12345678'
s = input('введите сообщение')
res = ''
deres=''
j = 0
for i in range(len(s)):
    if s[i].isalpha():
        k = int(key[j%5])
        res += alph[(alph.index(s[i]) + k)%33]
        j += 1
    else:
        res += s[i]
print(res)

f=0
for i in range(len(res)):
    if res[i].isalpha():
        k = int(key[f%5])
        deres+= alph[(alph.index(res[i]) - k)%33]
        f+=1
    else:
        deres += s[i]
print(deres)
