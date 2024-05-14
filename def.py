import random
def addition():
    v1= random.randint(0,100)
    v2= random.randint(0,100)
    somme=v1+v2
    return {somme,v1,v2}
resultat = addition()
print(resultat)

