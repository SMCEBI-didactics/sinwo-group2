# Aplikacja webowa

## Aby uruchomić aplikacje należy wykonać poniższe instrukcje

### Instalacja zależności:

sklad grupy:

```
* Jakub Krukowski 
* Aleksander Kopec
* Adam Martyniak
* Adam Wowra
* Oliwier Przeniczko

```
```
Program do prostych obliczeń numerycznych.
```
## Funkcjonalności: 

# Wyliczenie liczb pierwszych: 
```
Pokaż maksymalną liczbę pierwszą z podanego przedziału (max do 30000) z czasem wykonania metody.
przy pomocy metody modulo oraz przy pomocy sita Eratostenesa.
```
# Generator liczb losowych:
```
Z wybranego przedziału wylosuj liczbę z rozkładu jednorodnego i Gaussa
Wylosuj liczbę z wybranego przedziału oraz rozkładu opisanego przez wprowadzoną funkcję (metoda eliminacji von Neumanna)
```
# Dekodery:
```
Zapisz wprowadzoną liczbę w systemie dwójkowym, decymalnym oraz hex-decymalnym.
Zapisz wprowadzony tekst w formacie base64 (i odwrotnie).
Dla wprowadzonego tekstu wylicz hash: sha256 oraz md5
```
# Statystyka:
```
wylicz średnią, medianę i odchylenia dla wprowadzonych liczb
wyznacz korelację Pearsona
wylicz współczynniki regresji liniowej
wykonaj test Shapiro-Wilka
```

# Dla wprowadzonej funkcji znajdź miejsca zerowe:
```
metoda bisekcji
metoda siecznych
metoda iteracji
metoda newtona

```

### Użycie:

#### Inicjalizacja bazy sqlite (jeżeli nie istnieje)

```console

(flask_venv) user@host:~$ mkdir database
(flask_venv) user@host:~$ flask db init -d database
(flask_venv) user@host:~$ flask db migrate -d database # po modyfikacji models.py wystarczy wykonać tylko 2 ostatnie polecenia 
(flask_venv) user@host:~$ flask db upgrade -d database

```

#### Uruchamianie serwera

```console
# ustawienie zmiennych środowiskowych
(flask_venv) user@host:~$ export FLASK_APP=app.py 
(flask_venv) user@host:~$ export FLASK_ENV=development
#uruchomienie na wszystkich interfejsach i porcie 9999
(flask_venv) user@host:~$ flask run -h 0.0.0.0 -p 9999
```

adres oraz port może być również zdefiniowany przez zmienne środowiskowe:

```console
(flask_venv) user@host:~$ export FLASK_RUN_HOST=0.0.0.0
(flask_venv) user@host:~$ export FLASK_RUN_PORT=9999
```
