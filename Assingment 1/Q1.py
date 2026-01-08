import math

ti=float(input("enter start : "))
tf=int(input("enter end : "))
tt=ti
s_total=0

def vel(x):
    lnin=140000/(140000-2100 *x)
    p1=math.log (lnin)
    v=2000*p1 - 9.8*x
    return v

while tt<=tf-0.25:
    u=vel(tt)
    tt+=0.25
    v=vel(tt)
    v_avg=(u+v)/2
    s_avg=v_avg*0.25
    s_total+=s_avg


print(("total distance traveled by the rocket = ",s_total)    )
