def time_to_sec(a):
    try:
        hour=int(a.split(":")[0])
        min=int(a.split(":")[1])
        sec=int(a.split(":")[2])
        return (hour*3600 + min*60 + sec)
    except:
        print("time not in right format ")

def particular_data_getter(mega_dict,student_name ,index):
    student_info=mega_dict[student_name]
    status=student_info["crossing"][index]
    gate=student_info["gate_num"][index]
    time=student_info["time"][index]
    out=f" {student_name} , {status} , {gate} , {time} " 
    return out

def gate_keeper(gate_number_lis,entery_exit_status_lis,gateNum):
    index=-1
    ge1=0  # enter
    ge2=0
    ge3=0
    ge4=0
    ge5=0

    go1=0  # out / exit
    go2=0
    go3=0
    go4=0
    go5=0

    for gate_num in gate_number_lis:
        index+=1
        if entery_exit_status_lis[index]=="EXIT":
            if int(gate_num)==1:go1+=1
            if int(gate_num)==2:go2+=1
            if int(gate_num)==3:go3+=1
            if int(gate_num)==4:go4+=1
            if int(gate_num)==5:go5+=1
        else:
            if int(gate_num)==1:ge1+=1
            if int(gate_num)==2:ge2+=1
            if int(gate_num)==3:ge3+=1
            if int(gate_num)==4:ge4+=1
            if int(gate_num)==5:ge5+=1
    if int(gateNum)==1:return ge1,go1
    if int(gateNum)==2:return ge2,go2
    if int(gateNum)==3:return ge3,go3
    if int(gateNum)==4:return ge4,go4
    if int(gateNum)==5:return ge5,go5




student_status={}

with open("sorted_data.txt") as f:
# with open("try.txt") as f:
    data=f.readlines()
    entery=0
    exit=0
    names=[]
    for info in data[1:]:
        breaked_info=info.split(",")
        if len(breaked_info)!=4:
            continue
        student=breaked_info[0].strip()
        crossing=breaked_info[1].strip()
        gate_num=breaked_info[2].strip()
        time=breaked_info[3].strip()

        student_status[student]=student_status.get(student,{})
        if len(student_status[student])==0:  #normal case
            names.append(student)
            student_status[student]["crossing"]=[crossing]
            student_status[student]["gate_num"]=[gate_num]
            student_status[student]["time"]=[time]

        else:
            if student_status[student]["crossing"][-1]==crossing:
                if crossing=="EXIT": #if exit two times
                    exit+=1
                    student_status[student]["crossing"].pop()
                    student_status[student]["gate_num"].pop()
                    student_status[student]["time"].pop()

                    student_status[student]["crossing"].append(crossing)
                    student_status[student]["gate_num"].append(gate_num)
                    student_status[student]["time"].append(time)
                else:  #if entery two times
                    entery+=1 
            
            else: #normal case
                student_status[student]["crossing"].append(crossing)
                student_status[student]["gate_num"].append(gate_num)
                student_status[student]["time"].append(time)


        
# print(names)
# print(student_status["Snehal"]["crossing"])
while True:
    request=input("enter the action you would like to perform ")

    if request=="1":
        student_name=input("enter the name :").strip()
        current_time=input("enter the time which info you want to get ")
        if student_name not in names:
            print("please check the entered name ")
        else:
            index=-1
            index_txt_creater=-1
            info_dict=student_status[student_name]
            with open (f"{student_name}_all_day_activity.txt","w") as f:
                f.write(f"{student_name} , status")
                f.write("\n")
            for time in info_dict["time"]:
                index_txt_creater+=1
                with open (f"{student_name}_all_day_activity.txt","a") as f:
                    if info_dict["crossing"][index_txt_creater]=="EXIT":
                        f.write(f"{time} , out")
                        f.write("\n")
                    else:
                        f.write(f"{time} , in")
                        f.write("\n")

            for all_time in info_dict["time"]:
                index+=1
                if time_to_sec(all_time)>=time_to_sec(current_time):
                    if info_dict["crossing"][index]=="EXIT":
                        print(f"{student_name} is inside the college")
                        break
                    else:
                        print(f"{student_name} is outside the college")
                        break


    elif request=="2":

        start_time=time_to_sec(input("enter the start time in 00:00:00 format "))
        end_time=time_to_sec(input("enter the end time in 00:00:00 format "))
        for btech in names:
            info_time=student_status[btech]["time"]
            index_new=-1
            for stu_time in info_time:
                index_new+=1
                if time_to_sec(stu_time)>=start_time and time_to_sec(stu_time)<= end_time:
                    with open("output_time.txt","a") as f :

                        f.write(particular_data_getter(student_status,btech,index_new))
                        f.write("\n")
        print("                task completed                   ")




    elif request=="3":
        which_gate=int(input("enter the gate number whose info you want : "))
        gate_entery=0
        gate_exit=0

        for stu in names:
            gate_info_st=student_status[stu]["gate_num"]
            student_crossing=student_status[stu]["crossing"]
            number_of_crossing=gate_keeper(gate_info_st,student_crossing,which_gate)
            gate_entery+=number_of_crossing[0]
            gate_exit+=number_of_crossing[1]
        print(f"number of times students have entered through gate {which_gate} is {gate_entery}")
        print(f"number of times students have exited through gate {which_gate} is {gate_exit}")





    else:
        break