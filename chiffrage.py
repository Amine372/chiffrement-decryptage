import binascii

def sommech(n):
    r = 0
    while n:
        # r = r + n % 10
        # n = n // 10
        r, n = r + n % 10, n // 10
    return r

texte = input(str("entre un texte"))

liste_texte = list(texte.strip())

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = bin(ord(wh))[2:]
    wh = sommech(wh)
    liste_texte[i] = wh
print(liste_texte)
