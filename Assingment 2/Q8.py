def hours_to_mins(h:str):
    time=h.split(":")
    return int(time[0])*60 +int(time[1])
def mins_to_hrs(m):
    hr=m//60
    mins=m%60
    if mins<10 and hr <10:
        return "0"+str(hr)+ ":"+"0"+str(mins)
        
    elif mins<10 and hr >=10:
        return str(hr)+ ":"+"0"+str(mins)
    
    elif mins>=10 and hr <10:
        return "0"+str(hr)+ ":"+str(mins)
    else:
        return str(hr)+ ":"+str(mins)

# alice_schedule=input("enter the free time slot for Alice : ")
# bob_schedule=input("enter the free time slot for Bob : ")
# cameron_schedule=input("enter the free time slot for Cameron : ")
alice_schedule = ["15:00-16:00", "12:00-13:15","13:09-15:45"]
bob_schedule = ["14:00-14:30", "12:30-13:30"]
cameron_schedule = ["09:00-10:00", "15:30-16:30"]

all_slots=[]
for ts0 in alice_schedule:
    for ts1 in bob_schedule:
        for ts2 in cameron_schedule:
            start_lis=[]
            end_lis=[]
            start0=hours_to_mins(ts0.split("-")[0])
            start_lis.append(start0)
            start1=hours_to_mins(ts1.split("-")[0])
            start_lis.append(start1)
            start2=hours_to_mins(ts2.split("-")[0])
            start_lis.append(start2)
            
            end0=hours_to_mins(ts0.split("-")[1])
            end_lis.append(end0)
            end1=hours_to_mins(ts1.split("-")[1])
            end_lis.append(end1)
            end2=hours_to_mins(ts2.split("-")[1])
            end_lis.append(end2)

            start=max(start_lis)
            end=min(end_lis)

            if end-start>=30:
                all_slots.append(f"{mins_to_hrs(start)}-{mins_to_hrs(start +30)}")

slot_2=[]
a=[(alice_schedule,bob_schedule,"alice and bob"),(bob_schedule,cameron_schedule,"bab and cameron"),(cameron_schedule,alice_schedule,"cameron and alice")]

for i,j,c in a:
    for ts1 in i:
        for ts2 in j:
            start_lis=[]
            end_lis=[]
            start1=hours_to_mins(ts1.split("-")[0])
            start_lis.append(start1)
            start2=hours_to_mins(ts2.split("-")[0])
            start_lis.append(start2)

            end1=hours_to_mins(ts1.split("-")[1])
            end_lis.append(end1)
            end2=hours_to_mins(ts2.split("-")[1])
            end_lis.append(end2)

            start=max(start_lis)
            end=min(end_lis)

            if end-start>=30:
                slot_2.append(f"{c} can have a meeting at {mins_to_hrs(start)}-{mins_to_hrs(start +30)}")

if len (all_slots)>=1:
    for slots in all_slots:
        print(f"a meting can be scheduled at {slots}")
elif len(slot_2) >=1:
    for slots in slot_2:
        print(slots)
else:
    print("no common slot found")

def test():
    assert hours_to_mins("11:45")==705
    assert hours_to_mins("06:56")==416
test()

def _test():
    assert mins_to_hrs(705)=="11:45"
    assert mins_to_hrs(416)=="06:56"
_test()

# print(all_slots)
# print(slot_2)