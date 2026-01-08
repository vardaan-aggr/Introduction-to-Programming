def gcd(a,b):
    if a>b:
        a,b=a,b
    
    else:
        b,a=a,b    

    for i in range (b,0,-1):
        if a%i==0 and b%i==0:
            return i

d=6/(3.14)**2
def no_points(n):
    lis=[]
    count=0
    for i in range (0,n):
        for j in range (0,n):
            if gcd(i,j)==1:
                c=(i,j)
                lis.append(c)
                # lis.append(j) 
                count+=1
    # print(lis)
    return count
def density(n):
    return no_points(n)/(n**2)
def fin_den(d):
    n=1
    while n>-1:
        if d*1.5>density(n)>d*0.5:
            return n
        else:
            n+=1

# print(no_points(6))
# print(gcd(1,1))
print("density is achived at n = ",fin_den(d))
print("density which we wanted to get is :" ,d)
print("density which we got at this point is : ",density(fin_den(d)))

