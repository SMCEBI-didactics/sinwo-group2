import random
import click

def RandomNumberGeneratorGauss(bottom, top):
    """
    Funkcja generująca liczbe pseudolosową,
    oparta na rozkładzie Gaussa
    
    Argumenty:
    bottom - dolna granica przedziału losowania liczby
    top - górna granica przedziału losowania liczby
    
    Return:
    Funckja zwraca liczbę pseudolosową z podanego przedziału
    """

    bottom=float(bottom)
    top=float(top)
    while(True):
        mu=top-bottom
        sigma=top-bottom
        randomNumber=random.gauss(mu, sigma)
        if bottom<randomNumber<top:
        
            return randomNumber

        
                      
def RandomNumberGeneratorUniform(bottom ,top):
    """
    Funkcja generująca liczbe pseudolosową,
    oparta na rozkładzie jednorodnym
    
    Argumenty:
    bottom - dolna granica przedziału losowania liczby
    top - górna granica przedziału losowania liczby
    
    Return:
    Funckja zwraca liczbę pseudolosową z podanego przedziału
    """
    bottom=float(bottom)
    top=float(top)
    randomNumber=random.uniform(bottom, top)
    return randomNumber


def RandomNumberGeneratorNeumann(bottom, top):
    """
    Funkcja generująca liczbe pseudolosową,
    oparta na moetodzie eliminacji von Neumann'a
    
    Argumenty:
    bottom - dolna granica przedziału losowania liczby
    top - górna granica przedziału losowania liczby
    
    Return:
    Funckja zwraca liczbę pseudolosową z podanego przedziału
    """
    bottom=float(bottom)
    top=float(top)
    randomNumber=random.randrange(bottom, top)
    return randomNumber
   

@click.command()
@click.option('--rodzaj')
@click.option('--bottom', type=float)
@click.option('--top', type=float)
def main(rodzaj, bottom, top):
    
    bottom=float(bottom)
    top=float(top)
    if rodzaj=="Gauss":
        randomNumber = RandomNumberGeneratorGauss(bottom, top)
        print(randomNumber)
    elif rodzaj=="Neumann":
        randomNumber = RandomNumberGeneratorNeumann(bottom, top)
        print(randomNumber)
    elif rodzaj=="Uniform":
        randomNumber = RandomNumberGeneratorUniform(bottom, top)
        print(randomNumber)

    return None

if __name__ == '__main__':
    main()
