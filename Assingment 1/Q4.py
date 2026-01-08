# grp=str(input(" enter population of each group seperated by a coma (,) : " ))
grp= "50, 1450, 1400, 1700, 1500, 600, 1200"
a=grp.split(",")

def total_pop(q):   #q is a list of pop of differt grp 
    current_pop=0
    for i in range (len(q)):
        current_pop +=float(q[i])

    return current_pop

def pop_aft_y_of_ele(y,i,b):
    for ye in range (y+1):
        growth_rate = (2.5 - (0.4 * i)) - (0.1 * ye)
        b*=(1+growth_rate/100)
    return b

def pop_at_year_y(x,y):     #x is the list of pop of diff grp initially  and y is the year after which we want the list of pop
    lis=[]
    for i in range(len(x)):
        b=float(x[i])
        c=pop_aft_y_of_ele(y,i,b)
        lis.append(c)

    return lis # list with new pop

def year_of_max_pop(x):

    y=0
    while True:

        if total_pop(pop_at_year_y(x,y))>=total_pop(pop_at_year_y(x,y+1)):
            break
        y+=1

    return y

maxpop=total_pop(pop_at_year_y(a,year_of_max_pop(a)))


print("current population of the world",total_pop(a))
print("maximum population will be reached after : ",year_of_max_pop(a)," years ")
print ("maximum population will be :",maxpop)


