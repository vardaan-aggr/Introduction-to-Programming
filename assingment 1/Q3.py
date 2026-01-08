no=int (input("enter number : "))

def num_100(no):
    lis1=["","one","two",'three',"four",'five',"six",'seven','eight',"nine"]
    lis2=[ "ten" ,"eleven","twelve","thirteen","fourteen", "fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
    list3=[ " ","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
# 1 to 99
    if  no < 20 and  no > 10 : # 11 to 19
        a=no%10
        return lis2[a]
    
    elif(99>=no>=20): #20 to 99
        a=no%10
        b=no//10
        return list3[b] + lis1[a]
    
    elif no<10:
        return lis1[no]
    
    else :
        return " ten"
    


def bonus(no):
    p=""
    cr=no//10000000
    a=no%10000000
    lc=a//100000
    a=a%100000
    th=a//1000
    a=a%1000
    hun=a//100
    a=a%100
    din2=a


    if no>=10000000:
        p+= num_100(cr) + " crore "

    if no>=100000 and lc>0:
        p+=num_100(lc) + " lackh "

    if no>=1000 and th>0:
        p+=num_100(th) + " thousand "

    if no>=100 and hun>0:
        p+=num_100(hun) + " hundred "

    if  din2>0:
        p+=num_100(din2)

    if no==0:
        return " zero"

    return p + " only"


print(bonus(no))
