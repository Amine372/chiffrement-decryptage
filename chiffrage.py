import binascii
#from upyduino import *

def sommech(n):
    r = 0
    while n:
        # r = r + n % 10
        # n = n // 10
        r, n = r + n % 10, n // 10
    return r
p = input("Quelle est la clef P ?")
q = input("Quelle est la clef Q ?")
c = input("Quelle est la clef C ?")
p = int(p)
q = int(q)
c = int(c)

texte = input(str("Entrez un texte"))
gn = p*q
pn = (p-1)*(q-1)
liste_texte = list(texte.strip())

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = bin(ord(wh))[2:]
    wh = sommech(int(wh))
    wh = pow(wh,c)%gn
    liste_texte[i] = wh
print(liste_texte)
#fin de la partie de préalable permutation
#on entre dans le chiffrement
