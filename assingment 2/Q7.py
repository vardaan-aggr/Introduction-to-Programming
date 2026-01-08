with open("pages.txt") as f:
    data= f.readlines()

portiondata=[]
newdata=[]
condition=1
count_url=[]
for i in data:
    a=(i.split(": This page links to")[1]).split(",")
    # print(a)
    portiondata.append((i.split(": This page links to")[0]).split(",")[0].strip())
    portiondata.append((i.split(": This page links to")[0]).split(",")[1].strip())
    num_url=-1
    while True:    # this loop will take as many number of links from 2 to infinity
        num_url+=1
        # portiondata.append(a[1].strip())
        if (a[num_url].strip() ).startswith("and"):
            # condition=0
            portiondata.append(a[num_url].split("and")[1].strip())
            count_url.append(num_url+1)
            num_url=-1

            break
        else:
            portiondata.append(a[num_url].strip())

    newdata.append(portiondata)
    portiondata=[]

url_record={}
for info in newdata:
    url=info[0]
    ratio=float(info[1])
    url_record[url]=ratio

info_count=-1
for info in newdata:
    info_count+=1
    url=info[0]
    ratio=info[1]
    at_current=0
    while True:
        at_current+=1
        link=info[at_current]
        url_record[link]=url_record.get(link,0)+round(float(ratio)/count_url[info_count] , 3)
        if at_current==count_url[info_count]:
            break


final_num=0
final_url=None
for i,j in url_record.items():
    if final_num <=j:
        final_num=j
        final_url=i
print("************",end="\n")
print(f"{final_url} has occured the max number of times and its init_importance is {final_num}")
print("                                              ************",end="\n")
# print("\n")
# print(newdata)
# print(url_record)
# print("\n")
 