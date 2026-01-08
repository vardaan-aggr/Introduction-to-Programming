ang=float(input("angle in degrees= "))
radians=ang*3.14/180
dis=float(input("distance from pole = "))

def sinfn(radians):
    sin=0
    fac=1
    count=1
    for a in range(1,100,2):
        for i in range (1,a+1):
            fac*=i

        # count=1
        # while count<=6:
        count+=1
        sin=sin+ ((-1)**count)*((radians**a)/fac)
        fac=1
    return sin
def cosfn(radians):
    cos=0
    fac=1
    count=1
    for a in range(0,100,2):
        for i in range (1,a+1):
            fac*=i

        # count=1
        # while count<=6:
        count+=1
        cos=cos+ ((-1)**count)*((radians**a)/fac)
        fac=1
    return cos
def tanfn(radians):
    tan=sinfn(radians)/cosfn(radians )
    return tan

# print(tanfn(radians))
# print(sinfn(radians))
# print(cosfn(radians))


pol=dis/tanfn(radians)
hypo=dis/cosfn(radians)

print("height of pole = ",pol)
print("distance between person to tip of pole = ",hypo)