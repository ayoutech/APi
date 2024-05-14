import random
a = input('choose between T or F')

v1=int(input('valeur entre 0 et 15'))
v2=int(input('valeur entre 0 et 15'))
v3=int(input('valeur entre 0 et 15'))
def alt(a,L,max):
    L=[]
    L.append('v1','v2','v3')
    if a == 'T' :
        return random.choice(L)
    else :
        return random.randomint(0,max)
r=alt(a,L,100)
print(r)


        

    


        

