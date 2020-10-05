import random
import math
import binascii
import hashlib
clef = 6264522023
serure = str(clef)
serure =serure[0]+serure[1]
serure= int(serure)
texte = input(str("entre un texte"))
texte= list(texte.strip())
Lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Lettres_binaire =['01100001','01100010','01100011','01100100','01100101','01100110','01100111','01101000','01101001','01101010','01101011','01101100','01101101','01101110','01101111','01110000','01110001','01110010','01110011','01110100','01110101','01110110','01110111','01111000','01111001','01111010','00100000']
bgh=[]
vb =0
for i in range(0,len(texte)):
    if(texte[i]=="a"):
        texte[i] = Lettres_binaire[0]
    elif(texte[i]=="b"):
        texte[i] = Lettres_binaire[1]
    elif(texte[i]=="c"):
        texte[i] = Lettres_binaire[2]
    elif(texte[i]=="d"):
        texte[i] = Lettres_binaire[3]
    elif(texte[i]=="e"):
        texte[i] = Lettres_binaire[4]
    elif(texte[i]=="f"):
        texte[i] = Lettres_binaire[5]
    elif(texte[i]=="g"):
        texte[i] = Lettres_binaire[6]
    elif(texte[i]=="h"):
        texte[i] = Lettres_binaire[7]
    elif(texte[i]=="i"):
        texte[i] = Lettres_binaire[8]
    elif(texte[i]=="j"):
        texte[i] = Lettres_binaire[9]
    elif(texte[i]=="k"):
        texte[i] = Lettres_binaire[10]
    elif(texte[i]=="l"):
        texte[i] = Lettres_binaire[11]
    elif(texte[i]=="m"):
        texte[i] = Lettres_binaire[12]
    elif(texte[i]=="n"):
        texte[i] = Lettres_binaire[13]
    elif(texte[i]=="o"):
        texte[i] = Lettres_binaire[14]
    elif(texte[i]=="p"):
        texte[i] = Lettres_binaire[15]
    elif(texte[i]=="q"):
        texte[i] = Lettres_binaire[16]
    elif(texte[i]=="r"):
        texte[i] = Lettres_binaire[17]
    elif(texte[i]=="s"):
        texte[i] = Lettres_binaire[18]
    elif(texte[i]=="t"):
        texte[i] = Lettres_binaire[19]
    elif(texte[i]=="u"):
        texte[i] = Lettres_binaire[20]
    elif(texte[i]=="v"):
        texte[i] = Lettres_binaire[21]
    elif(texte[i]=="w"):
        texte[i] = Lettres_binaire[22]
    elif(texte[i]=="x"):
        texte[i] = Lettres_binaire[23]
    elif(texte[i]=="y"):
        texte[i] = Lettres_binaire[24]
    elif(texte[i]=="z"):
        texte[i] = Lettres_binaire[25]
    elif(texte[i]==" "):
        texte[i] = Lettres_binaire[26]
    else:
        print("erreur")
for i in range(0,len(texte)):
    bgh.append(texte[i])
    while(vb!=serure):
        bgh[i] = hashlib.sha224(bgh[i]).hexdigest()
        
