import click

def primes_method1(n):
    '''
    Funkcja primes_method1
    sluzy do znajdowania najwiejkszej 
    liczby pierwszej dzieki operacji 
    na liczbach modulo.

    args: int: n  

    return:max(list)
    '''
    
    out = list()
    for num in range(1, int(n)+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return max(out)


def SieveOfEratosthenes(n):

    '''
    Funkcja SieveOfEratosthenes
    sluzy do znajdowania najwiejkszej 
    liczby pierwszej dzieki operacji 
    matematycznej na sicie.

    args: int: n  

    return:max(list)
    '''
    n = int(n)
    prime = [True for i in range(n+1)]
    lis = []
    p = 2
    while (p * p <= n):
 
        if (prime[p] == True):
 

            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 

    for p in range(2, n+1):
        if prime[p]:
            lis.append(p)
            
    return max(lis)




@click.command()
@click.option("--liczba1", help="podaj liczbe 1", prompt="podaj liczbę 1")
def main(n):
    wynik = SieveOfEratosthenes(n)
    wynik1 = primes_method1(n)
    print(f"Najwieksza liczba pierwsza(metoda modulo) {primes_method1}")
    print(f"Najwieksza liczba pierwsza(metoda sita) {SieveOfEratosthenes}")
    return None

if __name__ == "__main__":
    main()
