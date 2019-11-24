zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
spravne_zaznamy = []
chybne_zaznamy = []
opravene_zaznamy = []
for i in zaznamy:
    i = i.split()
    spravne = True
    opravene = []
    for j in i:
        if j.islower():
            spravne = False
        opravene.append(j.capitalize())
    if spravne:
        spravne_zaznamy.append(" ".join(i))
        opravene_zaznamy.append(" ".join(i))
    else:
        chybne_zaznamy.append(" ".join(i))
        opravene_zaznamy.append(" ".join(opravene))
print(spravne_zaznamy)
print(chybne_zaznamy)
print(opravene_zaznamy)
