from Modules.LiczbyPierwsze.LiczbyPierwsze.main import SieveOfEratosthenes
from WebApp import app
from WebApp.models import *
from flask import render_template, request

import Dekoder.main as dk
import LiczbyPierwsze.main as LP
import Liczby_pseudolosowe.main as LPL
import MiejscaZerowe.main as MZ
import Statystyka.main as stat


@app.route("/")
def home_route():
    """
    Strona główna
    """
    wybory = ['liczby pierwsze', 'calkowanie', 'liczby losowe', 'dekodery', 'statystyka', 'miejsca zerowe']
    opcje = []
    for el in wybory:
        file_name = "_".join(el.split(" "))
        opcje.append({'name': el, 'filename': file_name})
    return render_template("home.html", opcje=opcje)


@app.route("/method/<var>", methods=["GET", "POST"])
def method_route(var):
    """
    przykład adres:port/method/cos
    """
    site = var + '.html'
    return render_template(site, var=var)
    return render_template("dodawanie.html", status=status, stare_wyniki=stare_wyniki)

@app.route("/method/statystyka", methods=["GET", "POST"])
def statystyka():
    status = "Oczekiwanie na listy"
    if request.method == "POST":
        X = request.form["lista1"]
        Y = request.form["lista2"]
        wybor = request.form["wybor"]
        
        if wybor == "srednia":
            wynik = stat._srednia(X)
            status = f"{X} {wybor} {wynik}"
        elif wybor == "mediana":
            wynik = stat._mediana(X)
            status = f"{X} {wybor} {wynik}"
        elif wybor == "odchylenie":
            wynik = stat._odchylenie(X)
            status = f"{X} {wybor} {wynik}"
        elif wybor == "regresjaliniowa":
            wynik = stat._regresjaliniowa(X,Y)
            status = f"{X} ; {Y} {wybor} {wynik}"
        elif wybor == "korelacja":
            wynik = stat._korelacja(X,Y)
            status = f"{X} ; {Y} {wybor} {wynik}"
        elif wybor == "testshapiro":
            wynik = stat._testshapiro(X)
            status = f"{X} {wybor} {wynik}"
        db_wynik = Statystyka(dzialanie=wybor, lista1=X, lista2=Y, wynik=wynik)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")
            
    stare_wyniki = Statystyka.query.filter().all() 
    return render_template("statystyka.html", status=status, stare_wyniki=stare_wyniki)
            
@app.route("/method/liczby_losowe", methods=["GET", "POST"])
def liczby_losowe():
    """
    """
    status = "Oczekiwanie na granice"
    if request.method == "POST":
        bottom = request.form["bottom"]
        top = request.form["top"]
        wybor = request.form["wybor"]
        
        if wybor=="Gauss":
            randomNumber = LPL.RandomNumberGeneratorGauss(bottom, top)
        elif wybor=="Neumann":
            randomNumber = LPL.RandomNumberGeneratorNeumann(bottom, top)
        elif wybor=="Uniform":
            randomNumber = LPL.RandomNumberGeneratorUniform(bottom, top)

        
        status = f"{randomNumber}"
        db_wynik = Liczby_pseudolosowe(bottom=bottom, top=top, randomNumber=randomNumber)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    stare_wyniki = Liczby_pseudolosowe.query.filter().all() 
    return render_template("liczby_losowe.html", status=status, stare_wyniki=stare_wyniki)

@app.route("/method/dekodery", methods=["GET", "POST"])
def dekoder():
    status = "Oczekiwanie na liczby"
    if request.method == "POST":
        tekst = request.form["tekst"]
        wybor = request.form["wybor"]
        operacja = ''

        operacje = {
        'to_bin': dk.to_bin,
        'to_hex': dk.to_hex,
        'to_base64': dk.to_base64,
        'from_base64': dk.from_base64,
        'md5': dk.hash_md5,
        'sha256': dk.hash_sha256,
        }

        if wybor == "to_bin":
            wynik = dk.to_bin(tekst)
            status = f"{tekst} = 0b{wynik}"
            operacja = 'toBin'
        elif wybor == "to_hex":
            wynik = dk.to_hex(tekst)
            status = f"{tekst} = 0x{wynik}"
            operacja = 'toHex'
        elif wybor == "to_base64":
            wynik = dk.to_base64(tekst)
            status = f"'{tekst}' w base64 to '{wynik}'"
            operacja = 'toBase64'
        elif wybor == "from_base64":
            wynik = dk.from_base64(tekst)
            status = f"{tekst} = 0b{wynik}"
            operacja = 'fromBase64'
        elif wybor == "to_sha":
            wynik = dk.hash_sha256(tekst)
            status = f"'{tekst}' w sha256 to '{wynik}'"
            operacja = 'toHashSha256'
        elif wybor == "to_md5":
            wynik = dk.hash_md5(tekst)
            status = f"'{tekst}' w md5 to '{wynik}'"
            operacja = 'toHashMd5'

        wynik = operacje[wybor](tekst)
        operacja = operacje

        db_wynik = Dekodery(tekst=tekst, wynik=wynik, operacja=operacja)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    stare_wyniki = Dekodery.query.filter().all()

    return render_template("dekodery.html", status=status, stare_wyniki=stare_wyniki)
    
@app.route("/method/liczby_pierwsze", methods=["GET", "POST"])
def liczby_pierwsze():
    """
    Przykład: Znajdowanie najwiekszej liczby pierwszej
    """
    status = "Oczekiwanie na liczbe"
    if request.method == "POST":
        n = request.form["n"]
        wybor = request.form["wybor"]

        if wybor == "primes_method1":
            wynik = LP.primes_method1(n)
        elif wybor == "SieveOfEratosthenes":
            wynik = LP.SieveOfEratosthenes(n)
        status = f"Najwieksza liczba pierwsa to {wynik} z {n}"
        db_wynik = LiczbyPierwsze(n=n, wynik=wynik)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")
            
    stare_wyniki = LiczbyPierwsze.query.filter().all() 
    return render_template("liczby_pierwsze.html", status=status, stare_wyniki=stare_wyniki)

@app.route("/method/miejsca_zerowe", methods=["GET", "POST"])
def miejsca_zerowe():
    
    """
    Obliczanie miejsc zerowych
    """
    status = "Oczekiwanie na dane"
    if request.method == "POST":
        fun = request.form["fun"]
        a = request.form["a"]
        b = request.form["b"]
        wybor = request.form["wybor"]
        
        if wybor == "metoda_bisekcji":
            wynik = MZ._metoda_bisekcji(fun, a, b)
        elif wybor == "metoda_siecznych":
            wynik = MZ._metoda_bisekcji(fun, a, b)
              
        status = f"{wynik}"
        db_wynik = MiejscaZerowe(fun=fun, a=a, b=b, wynik=wynik)

        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    stare_wyniki = MiejscaZerowe.query.filter().all()
    return render_template("miejsca_zerowe.html", status=status, stare_wyniki=stare_wyniki)
        

@app.route("/api/<var>")
def api_route(var):
    """
    przykład adres:port/api/cos
    """
    return render_template("api.html", var=var)

@app.route("/loginbeta", methods=["GET", "POST"])
def login_route():
    """
    przykład adres:port/loginbeta
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)

@app.route("/prompt", methods=["GET", "POST"])
def prompt():
    """
    testuj polecenia 
    """
    state = "empty"
    if request.method == "POST":
        prompt = request.form["prompt"]
        prompt = eval(prompt)
        state = f"{prompt}"
    return render_template("prompt.html", state=state)