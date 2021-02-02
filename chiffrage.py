import binascii

def chiffres(n):
...     c = []
...     while n != 0:
...         c.append(n % 10)
...         n = n / 10
...     return c

texte = input(str("entre un texte"))

liste_texte = list(texte.strip())

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = bin(ord(wh))[2:]
    liste_texte[i] = wh

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = list(wh.strip())
