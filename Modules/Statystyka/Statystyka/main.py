import click

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def srednia(Lista):
    """
    Oblicza średnią z podanej listy.
    
    Args:
        Lista (str): lista z liczbami.
        
    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    return wynik

def _srednia(Lista):
    """
    Oblicza średnią z podanej listy.

    Args:
        Lista (str): lista z liczbami.

    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    return wynik

def __srednia(Lista):
    """
    Wewnętrzna funkcja do liczenia średniej.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = Lista.copy()
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    return wynik

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def mediana(Lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.
    
    Args:
        Lista (str): lista z liczbami.
        
    Returns:
        num: wyznaczona mediana.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    B.sort()
    if len(B) % 2 == 0:
        return ((B[len(B) // 2 - 1] + y[len(B) // 2]) / 2)
    return B[len(B) // 2]

def _mediana(Lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.

    Args:
        Lista (str): lista z liczbami.

    Returns:
        num: wyznaczona mediana.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    B.sort()
    if len(B) % 2 == 0:
        return ((B[len(B) // 2 - 1] + B[len(B) // 2]) / 2)
    return B[len(B) // 2]


@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def odchylenie(Lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.
    
    Args:
        Lista (str): lista z liczbami.
        
    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    return sigma

def _odchylenie(Lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.

    Args:
        Lista (str): lista z liczbami.

    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = list(map(int,Lista.replace(","," ").split()))
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    return sigma

def __odchylenie(Lista):
    """
    Wewnętrzna funkcja do liczenia odchylenia standardowego.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = Lista.copy()
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    return sigma

@click.command()
@click.option("--X", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: '1 3 4'")
@click.option("--Y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: '1 3 4'")
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
    A = list(map(int,X.replace(","," ").split()))
    B = list(map(int,Y.replace(","," ").split()))
    srX = __srednia(A)
    srY = __srednia(B)
    tmp = 0
    a = 0
    for i in range(len(A)):
        a += (A[i] - srX) * (B[i] - srY)
    for j in A:
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
    srX = __srednia(X)
    srY = __srednia(Y)
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
@click.option("--X", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: '1 3 4'")
@click.option("--Y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: '1 3 4'")
def korelacja(X, Y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.
    
    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.
        
    Returns:
        kor (num): wyznaczona korelacja.
    """
    A = list(map(int,X.replace(","," ").split()))
    B = list(map(int,Y.replace(","," ").split()))
    srX = __srednia(A)
    srY = __srednia(B)
    sX = __odchylenie(A)
    sY = __odchylenie(B)
    kor = 0
    for i in range(len(A)):
        kor += (A[i] - srX) * (B[i] - srY)
    kor = kor / (len(A) * sX * sY)
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
    srX = __srednia(X)
    srY = __srednia(Y)
    sX = __odchylenie(X)
    sY = __odchylenie(Y)
    kor = 0
    for i in range(len(X)):
        kor += (X[i] - srX) * (Y[i] - srY)
    kor = kor / (len(X) * sX * sY)
    return kor

@click.command()
@click.option("--Lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def testshapiro(Lista):
    """
    Przeprowadza test Shapiro-Wilka dla listy o wielkości 3-10.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        str: wynik testu.
    """
    y = list(map(int,Lista.replace(","," ").split()))
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401], [0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]
    W = [0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842]
    y.sort()
    srY = __srednia(y)
    S = 0
    for i in y:
        S += (i - srY) ** 2
    m = len(y) // 2
    b = 0
    for j in range(m):
        b += B[len(y) - 3][j] * (y[len(y) - 1 - j] - y[j])
    if W[len(y) - 3] < b * b / S:
        return "Tak"
    return "Nie"


def _testshapiro(Lista):
    """
    Przeprowadza test Shapiro-Wilka dla listy o wielkości 3-10.

    Args:
        Lista (list): lista z liczbami.

    Returns:
        str: wynik testu.
    """
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401],[0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]
    W = [0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842]
    y = Lista.copy()
    y.sort()
    srY = __srednia(y)
    S = 0
    for i in y:
        S += (i - srY) ** 2
    m = len(y) // 2
    b = 0
    for j in range(m):
        b += B[len(y) - 3][j] * (y[len(y) - 1 - j] - y[j])
    if W[len(y) - 3] < b * b / S:
        return "Tak"
    return "Nie"
