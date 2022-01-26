from WebApp import app
from WebApp.models import *
from flask import render_template, request

from Dodaj.main import dodaj
import Statystyka.main as stat
"""
"""

@app.route("/")
def home_route():
    """
    Strona główna
    """
    return render_template("home.html")













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

@app.route("/method/statystyka", methods=["GET", "POST"])
def statystyka():
    status = "Oczekiwanie na listy"
    if request.method == "POST":
        X = request.form["lista1"]
        Y = request.form["lista2"]
        wybor = request.form["wybor"]
        
        if wybor == "srednia":
            wynik = stat._srednia(X)
            status = f"{wybor} {X} {wynik}"
        elif wybor == "mediana":
            wynik = stat._mediana(X)
            status = f"{wybor} {X} {wynik}"
        elif wybor == "odchylenie":
            wynik = stat._odchylenie(X)
            status = f"{wybor} {X} {wynik}"
        elif wybor == "regresjaliniowa":
            wynik = stat._regresjaliniowa(X,Y)
            status = f"{wybor} {X} {Y} {wynik}"
        elif wybor == "korelacja":
            wynik = stat._korelacja(X,Y)
            status = f"{wybor} {X} {Y} {wynik}"
        elif wybor == "testshapiro":
            wynik = stat._testshapiro(X)
            status = f"{wybor} {X} {wynik}"
        db_wynik = Statystyka(dzialanie=wybor, lista1=X, lista2=Y, wynik=wynik)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    stare_wyniki = Statystyka.query.filter().all() 


    return render_template("Statystyka.html", status=status, stare_wyniki=stare_wyniki)



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



               


  


               

               

               

               
