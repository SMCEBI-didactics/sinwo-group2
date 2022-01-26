import random
import click

@click.command()
@click.option('--bottom', type=float, prompt="Podaj dolna granice")
@click.option('--top', type=float, prompt="Podaj gorna granice")
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

    #bottom=float(bottom)
    #top=float(top)
    while(True):
        mu=top-bottom
        sigma=top-bottom
        randomNumber=random.gauss(mu, sigma)
        if bottom<randomNumber<top:
            print(randomNumber)
        
            return randomNumber

def _RandomNumberGeneratorGauss(bottom, top):
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
        print(randomNumber)
        if bottom<randomNumber<top:
            
            return randomNumber
        
            
@click.command()
@click.option('--bottom', type=float, prompt="Podaj dolna granice")
@click.option('--top', type=float, prompt="Podaj gorna granice")           
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
    randomNumber=random.uniform(bottom, top)
    print(randomNumber)
    return randomNumber

def _RandomNumberGeneratorUniform(bottom ,top):
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

@click.command()
@click.option('--bottom', type=float, prompt="Podaj dolna granice")
@click.option('--top', type=float, prompt="Podaj gorna granice")
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
    randomNumber=random.randrange(bottom, top)
    print(randomNumber)
    return randomNumber
    
def _RandomNumberGeneratorNeumann(bottom, top):
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
