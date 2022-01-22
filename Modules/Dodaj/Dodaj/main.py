import click

def dodaj(a,b):
    """
    Dodaj 2 liczby

    :param liczba1: pierwsza liczba
    :type float
    :param liczba2: druga liczba
    :type float

    :return: Suma liczb 
    :rtype: float
    
    """
    return a+b

@click.command()
@click.option("--liczba1", help="podaj liczbe 1", prompt="podaj liczbę 1")
@click.option("--liczba2", help="podaj liczbe 2", prompt="Podaj liczbę 2")
def main(liczba1, liczba2):
    wynik = dodaj(liczba1, liczba2)
    print(f"Wynik: {liczba1}+{liczba2}={wynik}")
    return None

if __name__ == "__main__":
    main()
