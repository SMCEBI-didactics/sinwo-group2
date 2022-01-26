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

class MiejscaZerowe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fun = db.Column(db.Text)
    a = db.Column(db.Text)
    b = db.Column(db.Text)
    wynik = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return f'Na przedziale funkcji {self.fun} od {self.a} do {self.b} miejsce zerowe to {self.wynik}'
