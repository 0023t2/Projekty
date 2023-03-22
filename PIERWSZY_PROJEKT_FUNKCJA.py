wynik_gracz1 = 0
wynik_gracz2 = 0
numer_rundy = 1

opcje_wyboru = ["papier", "kamień", "nożyce"]

def pobierz_wybor(Gracz):
    while True:
        wybor_gracza = input(f"{Gracz} podaj swój wybór : ")
        if wybor_gracza in opcje_wyboru:
            return wybor_gracza 
    
def obecny_wynik(wynik_gracz1, wynik_gracz2):
    print(f"Ilość wygranych gracza pierwszego: {wynik_gracz1}")
    print(f"Ilość wygranych gracza drugiego: {wynik_gracz2}")

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == "papier" and wybor_gracza2 == "kamień" \
    or wybor_gracza1 == "kamień" and wybor_gracza2 == "nożyce"\
    or wybor_gracza1 == "nożyce" and wybor_gracza2 == "papier":
        print("Gracz 1 wygrywa!") 
        return 1
    elif wybor_gracza1 == wybor_gracza2:
        return 0
    else:
        print("Gracz 2 wygrywa!")
        return -1

while wynik_gracz1 != 3 and wynik_gracz2 !=3:
    print("Runda", numer_rundy)

    wybor_gracza1 = pobierz_wybor("Gracz1")
    wybor_gracza2 = pobierz_wybor("Gracz2")
    wynik=sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik == 1:
        wynik_gracz1 +=1
    elif wynik == -1:
        wynik_gracz2 -=0
    numer_rundy +=1

    obecny_wynik(wynik_gracz1, wynik_gracz2)

if wynik_gracz1 == 3:
    print("Grę wygrywa gracz 1!")
elif wynik_gracz2 == 3:
    print("Grę wygrywa gracz 2!")