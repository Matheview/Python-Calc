import sys
from time import sleep

def add(a, b):
    print(a + b)
    sleep(1)

def sub(a, b):
    print(a - b)
    sleep(1)

def multi(a, b):
    print(a * b)
    sleep(1)

def div(a, b):
    print(a / b)
    sleep(1)

def userchoose():
    while True:
        choose = input("\nWybierz działanie:\n 1.Dodawanie\n 2.Odejmowanie\n 3.Mnozenie\n 4.Dzielenie\n 5.Zakoncz\n\n")
        if int(choose) < 5:
            numbers(int(choose))
        elif int(choose) == 5:
            sys.exit(0)
        else:
            print("Zly wybor, wybierz ponownie")
            userchoose()

def numbers(choose):
    try:
        first = float(input("Podaj pierwsza liczbe: "))
        second = float(input("Podaj druga liczbe: "))
    except:
        print("Blad podczas wprowadzania danych")
        numbers(choose)
    dzialanie(choose, first, second)     #moze wyskoczyc warunek o inicjalizacji przed uzyciem, a to dlatego, ze deklaracja dopiero wtedy nastapi, kiedy zostana wpisane liczby

def dzialanie(choose, a, b):
    if choose == 1:
        add(a, b)
    elif choose == 2:
        sub(a, b)
    elif choose == 3:
        multi(a, b)
    elif choose == 4:
        if a == 0 or b == 0:
            print("Nie mozna dzielic przez 0\n")
            sleep(1)
            numbers(choose)
        else:
            div(a, b)
    else:
        return
    userchoose()

if __name__ == "__main__":      # start programu
    userchoose()
