import math
a = 10
b = 1.05
c = 1
d = 1.06
def dem(p):
    dem_p=math.exp(a - b*p)
    return dem_p

def sup(p):
    sup_p=math.exp(c + d*p)
    return sup_p

def cp_dem_sup(p):
    p=0.5


    while p<600:
        if  -10<sup(p)-dem(p)<10 :
            return p   
        p*=1.05

   
         

if cp_dem_sup(1)==None:
    print(" no solution in range")
else:
    print("price at which equilibrium is achived " ,cp_dem_sup(0.00001))
    print("demand in market = ",dem(cp_dem_sup(0.00001)))
    print("supply in market = ",sup(cp_dem_sup(0.00001)))
    




