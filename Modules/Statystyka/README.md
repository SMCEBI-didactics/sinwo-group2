## Moduł Statystyka

###Użycie modułu z Dockerfile
```
cd abc/sinwo-group2/Modules/Statystyka
pip install .

sudo docker build . -t stats_test:v1.02
sudo docker run --rm stats_test:v1.02 POLECENIE
```
###Dostępne polecenia
Średnia
```
srednia --lista "1 2 3 4"
```
Mediana
```
mediana --lista "7 8 7 7 2"
```
Odchylenie standardowe
```
odchylenie --lista "3 2 3 3 2"
```
Regresja liniowa z dwóch list o RÓWNEJ długości
```
regresjaliniowa --x "10 12 14 16" --y "9 5 8 4"
```
Korelacja Piersona z dwóch list o RÓWNEJ długości
```
korelacja --x "1 9 4 4 5" --y "5 9 5 7 6"
```
Test Shapiro-Wilka dla listy o długości 3-10
```
testshapiro --lista "1 2 3 4 5 6"
```
