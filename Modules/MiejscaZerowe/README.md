## Moduł MiejscaZerowe

# Użycie modułu z Dockerfile
```
cd abc/sinwo-group2/Modules/MiejscaZerowe
pip install .

sudo docker build . -t roots_test:v1.01
sudo docker run --rm roots_test:v1.01 POLECENIE
```
# Dostępne polecenia
Wyznaczanie miejsca zerowego metoda bisekcji
```
metoda_bisekcji --fun "x ** 2 - 2" --a 1 --b 3
```
Wyznaczanie miejsca zerowego metoda siecznych
```
metoda_siecznych --fun "2 ** (1 / 2) * x ** 3" --a -1 --b 1
```

