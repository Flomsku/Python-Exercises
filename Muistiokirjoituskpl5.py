nimi = "muistio.txt"
kysymys = "(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n"
uusikirjaus = "Kirjoita uusi merkintä:"
error = "Tiedostoa ei ole olemassa"
jatkuu = True


while jatkuu:
    print(kysymys)
    valinta = int(input("Mitä haluat tehdä?: "))


    if valinta == 1:
        try:
            tiedosto = open(nimi, "r")
            teksti = tiedosto.readline()
            teksti = teksti[:-1]
            tiedosto.close()
            print(teksti)

        except IOError:
            print(error)

    if valinta == 2:

        kirjaus = str(input(uusikirjaus))
        tiedosto = open(nimi, "a")
        tiedosto.write(kirjaus + "\n")
    if valinta == 3:
        tiedosto = open(nimi, "w")
        tiedosto.close()
        print("Muistio tyhjennetty.")
    if valinta == 4:
        jatkuu = False
        print("Lopetetaan.")