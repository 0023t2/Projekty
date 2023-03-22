wynik_gracz1 = 0
wynik_gracz2 = 0
numer_rundy = 1

opcje_wyboru = ["papier", "kamień", "nożyce"]

while wynik_gracz1 != 3 and wynik_gracz2 !=3:
    print("Runda", numer_rundy)

    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
        wybor_gracza1 = input("Gracz1 podaj swój wybór : ")
        if wybor_gracza1 in opcje_wyboru:
            wybor_gracza_jest_poprawny = False

    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
        wybor_gracza2 = input("Gracz2 podaj swój wybór : ")
        if wybor_gracza2 in opcje_wyboru:
            wybor_gracza_jest_poprawny = False

    if wybor_gracza1 == "papier" and wybor_gracza2 == "kamień" \
    or wybor_gracza1 == "kamień" and wybor_gracza2 == "nożyce"\
    or wybor_gracza1 == "nożyce" and wybor_gracza2 == "papier":
        print("Gracz 1 wygrywa!")
        wynik_gracz1 +=1
    elif wybor_gracza1 == wybor_gracza2:
        print("Remis")
    else:
        print("Gracz 2 wygrywa!")
        wynik_gracz2 +=1
    print("Ilość wygranych gracza pierwszego")
    print(wynik_gracz1)
    print("Ilość wygranych gracza drugiego")
    print(wynik_gracz2)
    numer_rundy +=1

if wynik_gracz1 == 3:
    print("Grę wygrywa gracz 1!")
elif wynik_gracz2 == 3:
    print("Grę wygrywa gracz 2!")