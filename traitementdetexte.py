def transformation(texte):
    for i in range (0,len(texte)):
        if ord(texte[i])>122 or ord(texte[i])<97 :
            del texte[i]
        else :
            continue
    return

print(transformation("c'est l'été, j'ai joué"))
