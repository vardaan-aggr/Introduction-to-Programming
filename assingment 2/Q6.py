def lis_creater(filename,mode):
    unsorted_adress=[]
    with open(filename,mode) as f:
        num=len(f.readlines())
        f.close()
        f=open(filename,mode)
        for i in range(num):
            line=f.readline()
            unsorted_adress.append((line))
    adress=[eval(item.strip()) for item in unsorted_adress]
    return adress

def lis_to_tex(lis,tex):
    with open(tex,"w") as f:
        for i in lis:
            f.write(str(i))
            f.write("\n")

print("if you want to exit type --> exit \n if you want to add new entery type --> new\n if you want to find some person type --> find\n if you want to delete some persons entery type --> delete \n if you want to all the entries up to now in your adress book type --> see all \n ")
while True:
    print("        exit       find      new        see all       delete      ")
    order=input()

    if order=="exit":
        break

    elif order=="find":
            address=lis_creater("address_book.txt","r")
            person_find=(input("tell the name of person you want to find : ")).capitalize()
            find_index=[]
            index=-1
            for info in address:
                index+=1
                if info[0].capitalize()==person_find:
                    print(info)
                    # find_index.append(index)
                if index==len(address):
                    print("no such person found")



    elif  order=="new":
        adress=lis_creater("address_book.txt","r")

        new_entery=[]
        name=input("Name : ")
        new_entery.append(name)
        ads=input("adress :")
        new_entery.append(ads)
        phoneno=str( int (input("Phone num :")))
        new_entery.append(phoneno)
        email=input("email : ")
        new_entery.append(email)
        with open("address_book.txt","a") as f:
            f.write(str(new_entery))
            f.write("\n")
        new_entery=[]

    elif order=="delete":
        print("if you want to delete a person by name press --> 1\nif you want to delete a person by phone number press --> 2")
        delete_order=int(input())
        if delete_order==1:   #delete by name 
            address=lis_creater("address_book.txt","r")
            name_delete=input("enter the name of the person you want to delete : ")
            delet_index=[]
            index=-1
            for info in address:
                index+=1
                if info[0]==name_delete:
                    delet_index.append(index)
            delet_index.sort(key=None, reverse=True)
            if len(delet_index)>0:
                for i in delet_index:
                    del address[i]
                lis_to_tex(address,"address_book.txt")
                print("task completed.")
            else:
                print("no such name found")


        if delete_order==2: # delete by phone number
            ph=str(int(input("enter the phone number you want to delete : ")))
            index=-1
            address=lis_creater("address_book.txt","r")
            condition=0
            for info in address:
                index +=1
                if info[2]==ph:
                    condition=1
                    address.pop(index)
            if condition==0 :
                print("no such number in adress book")

            lis_to_tex(address,"address_book.txt")
            # condition=0

    elif order=="see all":
        adress=lis_creater("address_book.txt","r")
        for info in adress:
            print(info)
    else:
        print("please check the order you have put !!")
# print(address)