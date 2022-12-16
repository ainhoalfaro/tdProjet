def transformation(texte):
    l=''
    for i in range (0,len(texte)):
        if ord(texte[i])<=122 and ord(texte[i])>=97 :
            l=l+texte[i]
        else :
            continue
    return l

print(transformation("c'est l'été, j'ai joué"))

def majuscule(texte):
    l=''
    for i in range(0,len(texte)):
       l+=chr(ord(texte[i])-32)
    return l

print(majuscule("c'est l'été, j'ai joué"))

def majuscule2 (texte):
    return texte.upper()
print(majuscule2("texte"))

def cesar (text,s) :
    result = ""
    for i in range(0,len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

print(cesar("TVTZVJKLEKVOKVYPGVITFEWZUVEKZVCCVDFKUVGRJJVVJKOBGCFKZWEBJHFV",25))

fichier = open("nouveau", "w")
fichier.write(cesar(majuscule(transformation("c'est l'été, j'ai joué")),4))
fichier.close()

message = 'SUSYUIJKDJUNJUXOFUHSEDVYTUDJYUBBUCEJTUFQIIUUIJNAFBEJYVDAIGEU'
Lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for clef in range(len(Lettres)):
   traduction = ''
   for symbol in message:
      if symbol in Lettres:
         num = Lettres.find(symbol)
         num = num -  clef
         if num < 0:
            num = num + len(Lettres)
         traduction = traduction + Lettres[num]
      else:
         traduction = traduction + symbol
print('Hacking key #%s: %s' % (clef, traduction))