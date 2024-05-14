import random
def alt(boolen,L,min,max):
    if boolen == True :
        res = random.choice(L)
        return res
    else :
        res = random.randint(min,max)
        return res
L=[2,3,9]
sol = alt(False,L,1,4)
print(sol)


        

    


        

