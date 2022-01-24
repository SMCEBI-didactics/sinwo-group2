import click
import base64
import hashlib

@click.command()
@click.option("--liczba", help="podaj liczbe", prompt="podaj liczbe")
def toBin(liczba : int) -> str:
    """
    Zamienia liczbe dziesiętną na binarną

    :param a: liczba do zamiany
    :type int

    :return: liczba w zapisie binarnym
    :rtype: str
    
    """
    wynik = bin(int(liczba))
    print(wynik)
    return wynik


@click.command()
@click.option("--liczba", help="podaj liczbe", prompt="podaj liczbe")
def toHex(liczba: int) -> str:
    """
    Zamienia liczbe dziesiętną na heksadecymalna

    :param a: liczba do zamiany
    :type int

    :return: liczba w zapisie heksadecymalnym
    :rtype: str

    """
    wynik = hex(int(liczba))
    print(wynik)
    return wynik


@click.command()
@click.option("--tekst", help="podaj tekst", prompt="podaj tekst")
def toBase64(tekst : str) -> str:
    """
    Zamienia tekst na jego reprezentacje w base64

    :param tekst: tekst do zamiany
    :type str

    :return: tekst zapisany w base64
    :rtype: str

    """
    bytes1 = tekst.encode('ascii')
    bytes2 = base64.b64encode(bytes1)
    wynik = bytes2.decode('ascii')
    print(wynik)
    return wynik

@click.command()
@click.option("--tekst", help="podaj tekst", prompt="podaj tekst")
def fromBase64(tekst : str) -> str:
    """
    Zamienia zakodowany string w base64 na czytelny tekst

    :param b64string: zakodowany tekst
    :type str

    :return: czytelny odkodowany tekst
    :rtype: str

    """
    bytes1 = tekst.encode('ascii')
    bytes2 = base64.b64decode(bytes1)
    wynik = bytes2.decode('ascii')
    print(wynik)
    return wynik

@click.command()
@click.option("--tekst", help="podaj tekst", prompt="podaj tekst")
def hashMD5(tekst : str):
    """
    Zwraca hash md5 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.md5(tekst.encode())
    print(wynik.hexdigest())
    return wynik.hexdigest()

@click.command()
@click.option("--tekst", help="podaj tekst", prompt="podaj tekst")
def hashSHA256(tekst : str):
    """
    Zwraca hash SHA256 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.sha256(tekst.encode('ascii'))
    print(wynik.hexdigest())
    return wynik.hexdigest()
