import binascii

texte = input(str("entre un texte"))
texte = bin(ord(texte))[2:]
for i in range(0,texte):
    
liste_texte = list(texte.strip())
print(liste_texte)
