import random
import math
import binascii
clef = 6264522023
texte = input(str("entre un texte"))
texte= list(texte.strip())
texte1= []
Lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Tableau_Reference = []
Tableau_pondere =[]
for i in range (0,25):
    Tableau_Reference.append(random.randint(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
for i in range(0,25):
    texte1[i] = bin(int(binascii.hexlify(texte[i]), 16))[2:]
print(texte1)
