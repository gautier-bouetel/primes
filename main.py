"""
Programmme permmetant de verifier si un nombre est premier
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
determier si le nombre est premier
Args:
        p : valeur entière
return : 
True/False
    """
    i = int(sqrt(p))
    if p==1 :
        return False
    if p==2 :
        return True
    for d in range(2, i+1) :
        if p%d ==0 :
            return False
    return True

#### Fonction principale


def main():
    """
    appel la fonction pour la tester
    """
    isprime(6464)
    isprime(11)
    isprime(598563254543554878)

    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

if __name__ == "__main__":


    print()
    main()
