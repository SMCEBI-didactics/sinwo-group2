# Aplikacja webowa

## Aby uruchomić aplikacje należy wykonać poniższe instrukcje

### Instalacja zależności:

Użyj wirtualnego środowiska:

```console
user@host:~$ virtualenv flask_venv
user@host:~$ source flask_venv/bin/activate
(flask_venv) user@host:~$ pip install -r requirements.txt

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
#
## Alternatywnie można uruchomić aplikacje jako kontener

```
make run
```
lub 
```
sudo docker-compose up
```
