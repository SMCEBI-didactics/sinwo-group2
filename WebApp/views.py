from WebApp import app
from WebApp.models import *
from flask import render_template, request

from Dodaj.main import dodaj
import Dekoder.main as dk
import Liczby_pseudolosowe.main as LPL

"""
"""


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

#######################
#######################
#######################
#   Przykłady użycia  #
# praca z bazą danych #
#######################

@app.route("/przyklad", methods=["GET", "POST"])
def przyklad():
    """
    Przykład: dodawanie 2 liczb
    """
    # pobranie zawartości liczb
    status = "Oczekiwanie na liczby"
    if request.method == "POST":
        liczba1 = request.form["liczba1"]
        liczba2 = request.form["liczba2"]

        #  osobny moduł (funkcjonalność), Patrz Modules/Dodaj
        wynik = dodaj(float(liczba1), float(liczba2))
        status = f"{liczba1} + {liczba2} = {wynik}"

        # komunikacja z bazą; dodanie wyniku do bazy
        db_wynik = Dodawanie(liczba1=liczba1, liczba2=liczba2, wynik=wynik)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    # komunikacja z bazą: pobieranie zawartości tablicy
    stare_wyniki = Dodawanie.query.filter().all() 
    # zwraca tablice obiektów, zamiast all() można użyć first() (pierwszy obiekt), 
    # dostęp do zawartości przez np. stare_wyniki[1].liczba1. 
    # Aby dodać warunek można użyć: Dodawanie.query.filter(Dodawanie.wynik=="3.0").first()

    #################################################
    # Aktualizacja zawartości bazy możliwa przez:
    #   wpis = Dodawanie.query.filter(id==3).first() # istnieje również metoda one()
    #   wpis.liczba1 = 111
    #   wpis.liczba2 = 999
    #   db.session.commit()
    #################################################
    # Usuwanie wpisów z bazy: 
    #   wpis = Dodawanie.query.filter(id==3).first()
    #   db.session.delete(wpis) #używaj try:
    #   db.session.commit()
    #################################################

    return render_template("dodawanie.html", status=status, stare_wyniki=stare_wyniki)

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

        if wybor == "to_bin":
            wynik = dk._to_bin(tekst)
            status = f"{tekst} = 0b{wynik}"
            operacja = 'toBin'
        elif wybor == "to_hex":
            wynik = dk._to_hex(tekst)
            status = f"{tekst} = 0x{wynik}"
            operacja = 'toHex'
        elif wybor == "to_base64":
            wynik = dk._to_base64(tekst)
            status = f"'{tekst}' w base64 to '{wynik}'"
            operacja = 'toBase64'
        elif wybor == "from_base64":
            wynik = dk._from_base64(tekst)
            status = f"{tekst} = 0b{wynik}"
            operacja = 'fromBase64'
        elif wybor == "to_sha":
            wynik = dk._hash_sha256(tekst)
            status = f"'{tekst}' w sha256 to '{wynik}'"
            operacja = 'toHashSha256'
        elif wybor == "to_md5":
            wynik = dk._hash_md5(tekst)
            status = f"'{tekst}' w md5 to '{wynik}'"
            operacja = 'toHashMd5'

        db_wynik = Dekodery(tekst=tekst, wynik=wynik, operacja=operacja)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    stare_wyniki = Dekodery.query.filter().all()

    return render_template("dekodery.html", status=status, stare_wyniki=stare_wyniki)


##################
# inne przykłady #
##################

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



               


  


               

               

               

               
