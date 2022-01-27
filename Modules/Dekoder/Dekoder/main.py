import click
import base64
import hashlib
# __all__=["to_bin", "to_hex", "to_base64", "from_base64", "hash_md5", "hash_sha256"]
"""
Ten moduł odpowiada za wykonywanie różnych operacji enkodujących oraz dekodujących. 
"""

@click.command()
@click.option("--liczba")
def to_bin(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na binarną

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie binarnym
    :rtype: str

    """
    wynik = bin(int(liczba))
    print(wynik)
    return wynik

def _to_bin(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na binarną

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie binarnym
    :rtype: str

    """
    wynik = bin(int(liczba))
    return wynik

@click.command()
@click.option("--liczba")
def to_hex(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na heksadecymalna

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie heksadecymalnym
    :rtype: str

    """
    wynik = hex(int(liczba))
    print(wynik)
    return wynik

def _to_hex(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na heksadecymalna

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie heksadecymalnym
    :rtype: str

    """
    wynik = hex(int(liczba))
    return wynik

@click.command()
@click.option("--tekst")
def to_base64(tekst: str) -> str:
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

def _to_base64(tekst: str) -> str:
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
    return wynik


@click.command()
@click.option("--tekst")
def from_base64(tekst: str) -> str:
    """
    Zamienia zakodowany string w base64 na czytelny tekst

    :param tekst: zakodowany tekst
    :type str

    :return: czytelny odkodowany tekst
    :rtype: str

    """
    bytes1 = tekst.encode('ascii')
    bytes2 = base64.b64decode(bytes1)
    wynik = bytes2.decode('ascii')
    print(wynik)
    return wynik

def _from_base64(tekst: str) -> str:
    """
    Zamienia zakodowany string w base64 na czytelny tekst

    :param tekst: zakodowany tekst
    :type str

    :return: czytelny odkodowany tekst
    :rtype: str

    """
    bytes1 = tekst.encode('ascii')
    bytes2 = base64.b64decode(bytes1)
    wynik = bytes2.decode('ascii')
    return wynik

@click.command()
@click.option("--tekst")
def hash_md5(tekst: str):
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

def _hash_md5(tekst: str):
    """
    Zwraca hash md5 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.md5(tekst.encode())
    return wynik.hexdigest()


@click.command()
@click.option("--tekst")
def hash_sha256(tekst: str):
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

def _hash_sha256(tekst: str):
    """
    Zwraca hash SHA256 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.sha256(tekst.encode('ascii'))
    return wynik.hexdigest()

