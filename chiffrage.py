import binascii

texte = input(str("entre un texte"))

liste_texte = list(texte.strip())

for i in range(0,len(liste_texte)):
    wh = liste_texte[i]
    wh = bin(ord(texte))[2:]




wh = bin(ord(texte))[2:]
