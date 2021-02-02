import binascii

texte = input(str("entre un texte"))
texte = bin(ord(texte))[2:]
liste_texte = list(texte.strip())
print(liste_texte)
