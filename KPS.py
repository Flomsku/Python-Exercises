import random

def main():

    jatkuu = True
    tappio = 0
    voitto = 0
    tasapelit = 0
    kierrokset = 0
    count = 0
    lista = ["Torakka", "Jalka", "Ydinase"]

    while jatkuu:
        if len(lista) > 3:
            break

        valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if kierrokset == 3:
            print("Pelasit", kierrokset, "kierrosta, joista voitit", voitto, "ja pelasit tasan", tasapelit, "peliä.")
            quit()
        elif valinta == "Lopeta":
            print("Pelasit", kierrokset, "kierrosta, joista voitit", voitto, "ja pelasit tasan", tasapelit, "peliä.")
            quit()

        print("Sinä valitsit: ", valinta)
        kierrokset = kierrokset+1
        tietokone = lista[random.randint(0, 2)]
        print("Tietokone valitsi: ", tietokone)
        if valinta == tietokone:
            print("Tasapeli!")
            tasapelit = +1
        elif valinta == "Jalka":
            if tietokone == "Ydinase":
                print("Hävisit!")
                tappio = +1
            else:
                print("Voitit!")
                voitto = +1
        elif valinta == "Ydinase":
            if tietokone == "Jalka":
                print("Voitit!")
                voitto = +1
            else:
                print("Hävisit!")
                tappio = +1
        elif valinta == "Torakka":
            if tietokone == "Jalka":
                print("Hävisit!")
                tappio = +1
            else:
                print("Voitit!")
                voitto = +1
        count = +1
if __name__ == "__main__":
    main()