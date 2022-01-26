import click

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

def odchylenie(Lista):
    """
    Oblicza odchylenie standardowe dla liczb z podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        sigma (num): wyznaczone odchylenie standardowe.
    """
    sr = srednia(Lista)
    sigma = 0
    for i in Lista:
        sigma += (i - sr)**2
    sigma = (sigma / len(Lista))**0.5
    return sigma

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
    srX = srednia(X)
    srY = srednia(Y)
    tmp = 0
    a = 0
    for i in range(len(X)):
        a += (X[i] - srX) * (Y[i] - srY)
    for j in X:
        tmp += (j - srX)**2
    a /= tmp
    b = srY - a * srX
    return a, b

def korelacja(X, Y):
    """
    Oblicza korelację Piersona dwóch zestawów danych.
    
    Args:
        X (list): pierwsza lista z liczbami.
        Y (list): druga lista z liczbami.
        
    Returns:
        kor (num): wyznaczona korelacja.
    """
    srX = srednia(X)
    srY = srednia(Y)
    sX = odchylenie(X)
    sY = odchylenie(Y)
    kor = 0
    for i in range(len(X)):
        kor += (X[i] - srX) * (Y[i] - srY)
    kor = kor / (len(X) * sX * sY)
    return kor

def testshapiro(Lista):
    """
    Przeprowadza test Shapiro-Wilka dla podanej listy.
    
    Args:
        Lista (list): lista z liczbami.
        
    Returns:
        bool: wynik testu.
    """
    B = [[0.7071],[0.6872, 0.1677],[0.6646, 0.2413],[0.6431, 0.2806, 0.0875],[0.6233, 0.3031, 0.1401],
    [0.6052, 0.3164, 0.1743, 0.0561],[0.5888, 0.3244, 0.1976, 0.0947],[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]]# n: 3-10
    W = [0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842]# n: 3-10, 5%
    y = Lista.copy()
    y.sort()
    srY = srednia(y)
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
