import click
import base64
import hashlib
# __all__=["to_bin", "to_hex", "to_base64", "from_base64", "hash_md5", "hash_sha256"]
"""
Ten moduł odpowiada za wykonywanie różnych operacji enkodujących oraz dekodujących. 
"""

def to_bin(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na binarną

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie binarnym
    :rtype: str

    """
    wynik = bin(int(liczba))
    return wynik


def to_hex(liczba: str) -> str:
    """
    Zamienia liczbe dziesiętną na heksadecymalna

    :param liczba: liczba do zamiany
    :type str

    :return: liczba w zapisie heksadecymalnym
    :rtype: str

    """
    wynik = hex(int(liczba))
    return wynik


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
    return wynik


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
    return wynik


def hash_md5(tekst: str):
    """
    Zwraca hash md5 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.md5(tekst.encode())
    return wynik.hexdigest()


def hash_sha256(tekst: str):
    """
    Zwraca hash SHA256 dla wprowadzonego tekstu

    :param tekst: tekst do zahashowania
    :type str

    :return: hash dla tekstu
    :rtype: _Hash

    """
    wynik = hashlib.sha256(tekst.encode('ascii'))
    return wynik.hexdigest()



@click.command()
@click.argument("operacja")
@click.argument("dane")
def main(operacja, dane):
    operacje = {
        'to_bin': to_bin,
        'to_hex': to_hex,
        'to_base64': to_base64,
        'from_base64': from_base64,
        'md5': hash_md5,
        'sha256': hash_sha256,
    }
    print(operacje[operacja](dane))

