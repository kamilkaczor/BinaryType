import re
tekst = input('text to translate')
tekst_list = []
for i in tekst:
    tekst_list.append(i)
encrypted_tekst = [re.sub('0b', '', bin(ord(x))) for x in tekst_list]
print(' '.join(encrypted_tekst))