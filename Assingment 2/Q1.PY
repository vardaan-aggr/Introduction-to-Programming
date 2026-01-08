menu={"Samosa": 15 ,
      "Idli": 30 ,
      "Maggie": 50 ,
      "Dosa": 70 ,
      "Tea": 10 ,
      "Coffee": 20,
      "Sandwich": 35,
      "ColdDrink": 25 }
def multi(a,b):
    return a*b


print ("this is the list of all the items that are avilable in the canteen :",menu.items())
print("please enter your order : ")
breaked_order=[]
number_of_items=0
total_amount=0
while True:
    lit_order=[]
    b=input()
    c=b.split(",")
    if len(c)<2:
        print("thanks for the order")
        break
    else:
        breaked_order.append(c)
        price=menu[c[0]]
        quantity=int(c[1])
        netvalue=multi(price,quantity)
        number_of_items +=quantity
        total_amount+=netvalue
        print("Rs ",netvalue)
print("Total ,",number_of_items," items , Rs ",total_amount)

def test():
     assert multi(2,3)==6
     assert multi(7,2)==14
     assert multi(5,3)==15
test()