from WebApp import db
from datetime import datetime

# Struktura bazy danych
"""
Docstringi
"""


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return '<User {}>'.format(self.id)

class Dodawanie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    liczba1 = db.Column(db.Text)
    liczba2 = db.Column(db.Text)
    wynik = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return f'{self.liczba1}+{self.liczba2}={self.wynik}, '


class Dekodery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tekst = db.Column(db.Text)
    wynik = db.Column(db.Text)
    operacja = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.operacja}, Wejscie: {self.tekst}, Wyjscie: {self.wynik}"



class LiczbyPierwsze(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.Integer)
    wynik= db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return f'Najwieksza liczba pierwsza to {self.wynik} z {self.n}'


class Statystyka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lista1 = db.Column(db.Text)
    lista2 = db.Column(db.Text)
    wynik = db.Column(db.Text)
    dzialanie = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.dzialanie} Lista1: {self.lista1} Lista2: {self.lista2}, Wynik: {self.wynik}"

class Liczby_pseudolosowe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bottom = db.Column(db.Text)
    top = db.Column(db.Text)
    randomNumber = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return f'Dolna granica: {self.bottom} Gorna granica: {self.top} :losowa liczba to: {self.randomNumber}, '

