import click

@click.command()
@click.option("--lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def srednia(lista):
    """
    Oblicza średnią z podanej listy.
    
    Args:
        lista (str): lista z liczbami.
        
    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = list(map(int,lista.replace(","," ").split()))
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    print(wynik)
    return wynik

def _srednia(lista):
    """
    Oblicza średnią z podanej listy.

    Args:
        lista (str): lista z liczbami.

    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = list(map(int,lista.replace(","," ").split()))
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    return wynik

def __srednia(lista):
    """
    Wewnętrzna funkcja do liczenia średniej.

    Args:
        lista (list): lista z liczbami.

    Returns:
        wynik (num): wyznaczona srednia.
    """
    B = lista.copy()
    wynik = 0
    for i in B:
        wynik += i
    wynik /= len(B)
    return wynik

@click.command()
@click.option("--lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def mediana(lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.
    
    Args:
        lista (str): lista z liczbami.
        
    Returns:
        num: wyznaczona mediana.
    """
    B = list(map(int,lista.replace(","," ").split()))
    B.sort()
    if len(B) % 2 == 0:
        print(((B[len(B) // 2 - 1] + B[len(B) // 2]) / 2))
        return ((B[len(B) // 2 - 1] + B[len(B) // 2]) / 2)
    print(B[len(B) // 2])
    return B[len(B) // 2]

def _mediana(lista):
    """
    Oblicza medianę (wynik środkowy) z podanej listy.

    Args:
        lista (str): lista z liczbami.

    Returns:
        num: wyznaczona mediana.
    """
    B = list(map(int,lista.replace(","," ").split()))
    B.sort()
    if len(B) % 2 == 0:
        return ((B[len(B) // 2 - 1] + B[len(B) // 2]) / 2)
    return B[len(B) // 2]


@click.command()
@click.option("--lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def odchylenie(lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.
    
    Args:
        lista (str): lista z liczbami.
        
    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = list(map(int,lista.replace(","," ").split()))
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    print(sigma)
    return sigma

def _odchylenie(lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.

    Args:
        lista (str): lista z liczbami.

    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = list(map(int,lista.replace(","," ").split()))
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    return sigma

def __odchylenie(lista):
    """
    Wewnętrzna funkcja do liczenia odchylenia standardowego.

    Args:
        lista (list): lista z liczbami.

    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    B = lista.copy()
    sr = __srednia(B)
    sigma = 0
    for i in B:
        sigma += (i - sr)**2
    sigma = (sigma / len(B))**0.5
    return sigma

@click.command()
@click.option("--x", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: '1 3 4'")
@click.option("--y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: '1 3 4'")
def regresjaliniowa(x, y):
    """
    Oblicza regresję liniową dwóch zestawów danych.
    
    Args:
        x (str): pierwsza lista z liczbami.
        y (str): druga lista z liczbami.
        
    Returns:
        a (num): nachylenie linii regresji
        b (num): wyraz wolny
    """
    A = list(map(int,x.replace(","," ").split()))
    B = list(map(int,y.replace(","," ").split()))
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
    print(str(a)+" "+str(b))
    return str(a)+" "+str(b)

def _regresjaliniowa(x, y):
    """
    Oblicza regresję liniową dwóch zestawów danych.

    Args:
        x (str): pierwsza lista z liczbami.
        y (str): druga lista z liczbami.

    Returns:
        a (num): nachylenie linii regresji
        b (num): wyraz wolny
    """
    A = list(map(int,x.replace(","," ").split()))
    B = list(map(int,y.replace(","," ").split()))
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
    return str(a)+" "+str(b)

@click.command()
@click.option("--x", help="podaj listę", prompt="podaj pierwszą listę z 3-10 danymi typu: '1 3 4'")
@click.option("--y", help="podaj listę", prompt="podaj drugą listę z 3-10 danymi typu: '1 3 4'")
def korelacja(x, y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.
    
    Args:
        x (str): pierwsza lista z liczbami.
        y (str): druga lista z liczbami.
        
    Returns:
        kor (num): wyznaczona korelacja.
    """
    A = list(map(int,x.replace(","," ").split()))
    B = list(map(int,y.replace(","," ").split()))
    srX = __srednia(A)
    srY = __srednia(B)
    sX = __odchylenie(A)
    sY = __odchylenie(B)
    kor = 0
    for i in range(len(A)):
        kor += (A[i] - srX) * (B[i] - srY)
    kor = kor / (len(A) * sX * sY)
    print(kor)
    return kor

def _korelacja(x, y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.

    Args:
        x (str): pierwsza lista z liczbami.
        y (str): druga lista z liczbami.

    Returns:
        kor (num): wyznaczona korelacja.
    """
    A = list(map(int,x.replace(","," ").split()))
    B = list(map(int,y.replace(","," ").split()))
    srX = __srednia(A)
    srY = __srednia(B)
    sX = __odchylenie(A)
    sY = __odchylenie(B)
    kor = 0
    for i in range(len(A)):
        kor += (A[i] - srX) * (B[i] - srY)
    kor = kor / (len(A) * sX * sY)
    return kor

@click.command()
@click.option("--lista", help="podaj listę", prompt="podaj listę z 3-10 danymi typu: '1 3 4'")
def testshapiro(lista):
    """
    Przeprowadza test Shapiro-Wilka dla listy o wielkości 3-10.
    
    Args:
        lista (str): lista z liczbami.
        
    Returns:
        str: wynik testu.
    """
    y = list(map(int,lista.replace(","," ").split()))
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
        print("Tak")
        return "Tak"
    print("Nie")
    return "Nie"


def _testshapiro(lista):
    """
    Przeprowadza test Shapiro-Wilka dla listy o wielkości 3-10.

    Args:
        lista (str): lista z liczbami.

    Returns:
        str: wynik testu.   
    """
    y = list(map(int,lista.replace(","," ").split()))
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401],[0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]
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
