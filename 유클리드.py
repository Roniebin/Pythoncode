a,b=24,14

def Euclid(a,b):
    if b ==0:
        return a
    else :
        return Euclid(b,a%b)

print(Euclid(a,b))