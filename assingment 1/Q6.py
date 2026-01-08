x=float(input("enter assumed root less than 100 : "))

def comp_val(x):
    y= x**3 - 10.5*x**2 + 34.5*x - 35
    return y

def slope( x):
    diff=3*(x**2) -21*x + 34.5
    return diff

def xnew(x):
    x1= (x- comp_val(x)/slope(x))
    return round(x1,2)
  
def root(x): 
    # for x in range (100):
    while x<100:
        if -0.2<comp_val(xnew(x))<0.2:
            return xnew(x)
        else:
            x=xnew(x)

            root(xnew(x))

# def ran(x1,x2):
#     lis=[]
#     final=[]
#     for i in range (x1,x2+1):
#         c= root(i)
#         lis.append(c)

#     for roots in lis:
#         if all(abs(roots - other) >= 0.1 for other in final):
#             final.append(roots)

#         return final
    
#         # for i in range(len(lis)) :
#         #     if x2>lis[0]>x1 :
#         #         final.append(lis[0])
#         #     if len()
      

#     # return(lis)
    
# # def remsame(a)
# #     for i range(1,len(a)):
# #         if len
# #     # return(lis)


print ("closest root to assumed root is :  ",root(x))
# x1=int( input("enter lower limit of range : "))
# x2=int( input("enter upper limit of range less than 100 : "))
# print(ran(x1,x2))

