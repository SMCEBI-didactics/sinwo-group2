import click


@click.command()
@click.option('--fun')
@click.option('--a')
@click.option('--b')
def metoda_bisekcji(fun, a, b):
    
    """
    Funkcja wyznaczająca miejsce zerowe metodą bisekcji
    
    :param f: wzór funkcji rozpatrywanej pod kątem znalezienia miejsca zerowego
    :type: str
    :param a: poczatek rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    :param b: koniec rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    
    :return: znalezione miejsce zerowe
    :rtype: int
    
    """

    
    assert all([((c.isalpha() and c == 'x') or not c.isalpha()) for c in fun]), "tylko x moze zostac uzyty jako argument"
    assert all([c != '^' for c in fun]), "potegowanie odbywa sie zgodnie z pythonem za pomocom operatorow **"
#     assert isinstance(f(1), (int, float)), "Podane dane nie jest działaniem"
    assert any([c == 'x' for c in fun]), "Brak argumentu"

    epsilon=0.01
    imax=25
    
    a = int(a)
    b = int(b)
    
    if a > b:
        a, b = b, a
    
    fa = wylicz(fun, a)
    
    if abs(fa) < epsilon:
        return a
    
    fb = wylicz(fun, b)
    
    if abs(fb) < epsilon:
        return b
    
    if fa * fb > 0:
        return None
    
    for i in range(imax):
        
        c = (a + b) / 2
        fc = wylicz(fun, c)
        
        if abs(b - a) < epsilon:
            break
            
        if abs(fc) < epsilon:
            break
        
        if fa * fc > 0:
            a, fa = c, fc
            
        if fb * fc > 0:
            b, fb = c, fc
    
    if c is None:
        print("Nie istnieje miejsce zerowe dla danego zakresu")
    else:
        print(c)
    return c

def _metoda_bisekcji(fun, a, b):
    
    """
    Funkcja wyznaczająca miejsce zerowe metodą bisekcji
    
    :param f: wzór funkcji rozpatrywanej pod kątem znalezienia miejsca zerowego
    :type: str
    :param a: poczatek rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    :param b: koniec rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    
    :return: znalezione miejsce zerowe
    :rtype: int
    
    """

    
    assert all([((c.isalpha() and c == 'x') or not c.isalpha()) for c in fun]), "tylko x moze zostac uzyty jako argument"
    assert all([c != '^' for c in fun]), "potegowanie odbywa sie zgodnie z pythonem za pomocom operatorow **"
#     assert isinstance(f(1), (int, float)), "Podane dane nie jest działaniem"
    assert any([c == 'x' for c in fun]), "Brak argumentu"

    epsilon=0.01
    imax=25
    
    a = int(a)
    b = int(b)
    
    if a > b:
        a, b = b, a
    
    fa = wylicz(fun, a)
    
    if abs(fa) < epsilon:
        return a
    
    fb = wylicz(fun, b)
    
    if abs(fb) < epsilon:
        return b
    
    if fa * fb > 0:
        return None
    
    for i in range(imax):
        
        c = (a + b) / 2
        fc = wylicz(fun, c)
        
        if abs(b - a) < epsilon:
            break
            
        if abs(fc) < epsilon:
            break
        
        if fa * fc > 0:
            a, fa = c, fc
            
        if fb * fc > 0:
            b, fb = c, fc
    
    return c


@click.command()
@click.option('--fun')
@click.option('--a')
@click.option('--b')
def metoda_siecznych(fun, a, b):
    
    """
    Funkcja wyznaczająca miejsce zerowe metodą siecznych
    
    :param f: wzór funkcji rozpatrywanej pod kątem znalezienia miejsca zerowego
    :type: str
    :param a: poczatek rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    :param b: koniec rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    
    :return: znalezione miejsce zerowe
    :rtype: int/None
    
    """
    
    assert all([((c.isalpha() and c == 'x') or not c.isalpha()) for c in fun]), "tylko x moze zostac uzyty jako argument"
    assert all([c != '^' for c in fun]), "potegowanie odbywa sie zgodnie z pythonem za pomocom operatorow **"
#     assert isinstance(f(1), (int, float)), "Podane dane nie jest działaniem"
    assert any([c == 'x' for c in fun]), "Brak argumentu"
    
    epsilon=0.01
    imax=25
    
    a = int(a)
    b = int(b)
    
    if a > b:
        a, b = b, a
    
    
    fa = wylicz(fun, a)
    
    if abs(fa) < epsilon:
        return a
    
    fb = wylicz(fun, b)
    if abs(fb) < epsilon:
        return b
    
    if fa * fb > 0:
        return None
    
    for i in range(imax):

        
        c = (a * fb - b * fa) / (fb - fa)
        fc = wylicz(fun, c)
        
        if abs(b - a) < epsilon:
            break
            
        if abs(fc) < epsilon:
            break
        
        if fa * fc > 0:
            a, fa = c, fc
            
        if fb * fc > 0:
            b, fb = c, fc
    
    if c is None:
        print("Nie istnieje miejsce zerowe dla danego zakresu")
    else:
        print(c)
    return c


def _metoda_siecznych(fun, a, b):
    
    """
    Funkcja wyznaczająca miejsce zerowe metodą siecznych
    
    :param f: wzór funkcji rozpatrywanej pod kątem znalezienia miejsca zerowego
    :type: str
    :param a: poczatek rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    :param b: koniec rozpatrywanego zakresu pod kątem szukanego miejsca zerowego
    :type: int
    
    :return: znalezione miejsce zerowe
    :rtype: int/None
    
    """
    
    assert all([((c.isalpha() and c == 'x') or not c.isalpha()) for c in fun]), "tylko x moze zostac uzyty jako argument"
    assert all([c != '^' for c in fun]), "potegowanie odbywa sie zgodnie z pythonem za pomocom operatorow **"
#     assert isinstance(f(1), (int, float)), "Podane dane nie jest działaniem"
    assert any([c == 'x' for c in fun]), "Brak argumentu"
    
    epsilon=0.01
    imax=25
    
    a = int(a)
    b = int(b)
    
    if a > b:
        a, b = b, a
    
    
    fa = wylicz(fun, a)
    
    if abs(fa) < epsilon:
        return a
    
    fb = wylicz(fun, b)
    if abs(fb) < epsilon:
        return b
    
    if fa * fb > 0:
        return None
    
    for i in range(imax):

        
        c = (a * fb - b * fa) / (fb - fa)
        fc = wylicz(fun, c)
        
        if abs(b - a) < epsilon:
            break
            
        if abs(fc) < epsilon:
            break
        
        if fa * fc > 0:
            a, fa = c, fc
            
        if fb * fc > 0:
            b, fb = c, fc
        
    return c

            
def wylicz(fun, x):
    """
    Funkcja pomocnicza wyznaczajaca wartosc funkcji podanej w postaci lancucha znakow w podanym punkcie
    
    :param fun: funkcja, której ma zostać wyznaczona wartość w punkcie  
    :type: str
    :param x: argument funkcji, w którym ma zostać wyznaczona wartość funkcji
    :type: int
    
    :return: wartość funkcji
    :rtype int
    
    """
    wynik = eval(fun)
    return wynik


