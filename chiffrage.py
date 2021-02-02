import binascii

def sommech(n):
    r = 0
    while n:
        # r = r + n % 10
        # n = n // 10
        r, n = r + n % 10, n // 10
    return r
p = input(int("quelle est la clep P ?"))
q = input(int("quelle est la clep Q ?"))

texte = input(str("entre un texte"))
n = p*q
liste_texte = list(texte.strip())

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = bin(ord(wh))[2:]
    wh = sommech(int(wh))
    liste_texte[i] = wh
#fin de la partie de préalable permutation
#on entre dans le chiffrement
