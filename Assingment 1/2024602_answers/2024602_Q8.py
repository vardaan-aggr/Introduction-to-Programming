# x=int(input("enter value of x : "))
# inix=0
# iniy=1

def slope (x,y):
    slo=x+y
    return slo
def vari_slo(x1,y1,x,h=0.1):
    yf=y1

    while x1<x:
        yf+= h*slope(x1,y1)
        x1+=h
    return yf

    
x=int(input("enter value of x : "))
ini_x=0
ini_y=1
print("value of function at given x is  ",vari_slo(ini_x,ini_y,x))