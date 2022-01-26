import click

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: [1,3,4]")
def srednia(Lista):
    """
    Oblicza średnią z podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        wynik (num): wyznaczona srednia.
    """
    wynik = 0
    for i in Lista:
        wynik += i
    wynik /= len(Lista)
    return wynik

def _srednia(Lista):
    """
    Oblicza średnią z podanej listy.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        wynik (num): wyznaczona srednia.
    """
    wynik = 0
    for i in Lista:
        wynik += i
    wynik /= len(Lista)
    return wynik

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: [1,3,4]")
def mediana(Lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        num: wyznaczona mediana.
    """
    y = Lista.copy()
    y.sort()
    if len(y) % 2 == 0:
        return ((y[len(y) // 2 - 1] + y[len(y) // 2]) / 2)
    return y[len(y) // 2]

def _mediana(Lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        num: wyznaczona mediana.
    """
    y = Lista.copy()
    y.sort()
    if len(y) % 2 == 0:
        return ((y[len(y) // 2 - 1] + y[len(y) // 2]) / 2)
    return y[len(y) // 2]

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: [1,3,4]")
def odchylenie(Lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    sr = _srednia(Lista)
    sigma = 0
    for i in Lista:
        sigma += (i - sr)**2
    sigma = (sigma / len(Lista))**0.5
    return sigma

def _odchylenie(Lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    sr = _srednia(Lista)
    sigma = 0
    for i in Lista:
        sigma += (i - sr)**2
    sigma = (sigma / len(Lista))**0.5
    return sigma

@click.command()
@click.option("--X", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: [1,3,4]")
@click.option("--Y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: [1,3,4]")
def regresjaliniowa(X, Y):
    """
    Oblicza regresję liniową dwóch zestawów danych.
    
    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.
        
    Returns:
        a (num): nachylenie linii regresji
        b (num): wyraz wolny
    """
    srX = _srednia(X)
    srY = _srednia(Y)
    tmp = 0
    a = 0
    for i in range(len(X)):
        a += (X[i] - srX) * (Y[i] - srY)
    for j in X:
        tmp += (j - srX)**2
    a /= tmp
    b = srY - a * srX
    return a, b

def _regresjaliniowa(X, Y):
    """
    Oblicza regresję liniową dwóch zestawów danych.

    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.

    Returns:
        a (num): nachylenie linii regresji
        b (num): wyraz wolny
    """
    srX = _srednia(X)
    srY = _srednia(Y)
    tmp = 0
    a = 0
    for i in range(len(X)):
        a += (X[i] - srX) * (Y[i] - srY)
    for j in X:
        tmp += (j - srX)**2
    a /= tmp
    b = srY - a * srX
    return a, b

@click.command()
@click.option("--X", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: [1,3,4]")
@click.option("--Y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: [1,3,4]")
def korelacja(X, Y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.
    
    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.
        
    Returns:
        kor (num): wyznaczona korelacja.
    """
    srX = _srednia(X)
    srY = _srednia(Y)
    sX = _odchylenie(X)
    sY = _odchylenie(Y)
    kor = 0
    for i in range(len(X)):
        kor += (X[i] - srX) * (Y[i] - srY)
    kor = kor / (len(X) * sX * sY)
    return kor

def _korelacja(X, Y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.

    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.

    Returns:
        kor (num): wyznaczona korelacja.
    """
    srX = _srednia(X)
    srY = _srednia(Y)
    sX = _odchylenie(X)
    sY = _odchylenie(Y)
    kor = 0
    for i in range(len(X)):
        kor += (X[i] - srX) * (Y[i] - srY)
    kor = kor / (len(X) * sX * sY)
    return kor

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: [1,3,4]")
def testshapiro(Lista):
    """
    Przeprowadza test Shapiro-Wilka dla podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        bool: wynik testu.
    """
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401], [0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]
    W = [0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842]
    y = Lista.copy()
    y.sort()
    srY = _srednia(y)
    S = 0
    for i in y:
        S += (i - srY) ** 2
    m = len(y) // 2
    b = 0
    for j in range(m):
        b += B[len(y) - 3][j] * (y[len(y) - 1 - j] - y[j])
    if W[len(y) - 3] < b * b / S:
        return True
    return False


def _testshapiro(Lista):
    """
    Przeprowadza test Shapiro-Wilka dla podanej listy.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        bool: wynik testu.
    """
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401],[0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]
    W = [0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842]
    y = Lista.copy()
    y.sort()
    srY = _srednia(y)
    S = 0
    for i in y:
        S += (i - srY) ** 2
    m = len(y) // 2
    b = 0
    for j in range(m):
        b += B[len(y) - 3][j] * (y[len(y) - 1 - j] - y[j])
    if W[len(y) - 3] < b * b / S:
        return True
    return False
