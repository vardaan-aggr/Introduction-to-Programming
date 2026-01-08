def corse_helper(corse_name,credits,assesment,grading_policy,marks_file="marks.txt"):
    def marks_cal(file_line,marking_scheme):
        content=file_line.strip().split(",")
        roll_number=content[0]
        content.pop(0)
        marks=0
        total_marks=sum(marking_scheme)
        all_marks=[]
        index=-1
        for num in content:
            index+=1
            try:
                particular_marks=float(num)
            except:
                particular_marks=0
            marks+=(particular_marks/total_marks)*100
            all_marks.append(f"{particular_marks}/{marking_scheme[index]}")
    
        return [roll_number,marks,all_marks]

    marking_scheme=[]# list of marks weightege for each component lab,assingment etc
    papper_name=[]
    for grades in assesment:
        marking_scheme.append(grades[1])
        papper_name.append(grades[0])
    lis_output=[]# will be of the form[[rollnum,percentage],......,] initially and then after last few lines of code[(rollnum,percent,grade),..]
    final_student_dict={}
    with open(marks_file,"r") as f:
        data=f.readlines()
        for line in data:
            output=marks_cal(line.strip(),marking_scheme)
            final_student_dict[output[0]]=dict()
            final_student_dict[output[0]]["percent"]=f"{output[1]}%"
            final_student_dict[output[0]]["assessments"]=[]
            final_student_dict[output[0]]["grade"]=None
            index_temp=-1
            for particular in output[2]:
                index_temp+=1
                final_student_dict[output[0]]["assessments"].append(f"{papper_name[index_temp]} : {particular}")
            lis_output.append(output[:2])
    
    # for num in grading_policy:
    dict_of_lists={
    "lis_1":[],
    "lis_2":[],
    "lis_3":[],
    "lis_4":[],
    "lis_5":[]
    }
    grading_policy.sort(reverse=True)
    grading_scheme=grading_policy.copy()
    max1=max(grading_scheme)#above for A
    grading_scheme.remove(max(grading_scheme))
    max2=max(grading_scheme)# for B
    grading_scheme.remove(max(grading_scheme))
    max3=max(grading_scheme)#for C
    grading_scheme.remove(max(grading_scheme))
    max4=max(grading_scheme)#greater for D and if less then F
    grading_scheme.remove(max(grading_scheme))


    for info in lis_output:
        student_marks=info[1]
        if max1-2<student_marks<max1+2:
            dict_of_lists["lis_1"].append(student_marks)
        elif max2-2<student_marks<max2+2:
            dict_of_lists["lis_2"].append(student_marks)
        elif max3-2<student_marks<max3+2:
            dict_of_lists["lis_3"].append(student_marks)
        elif max4-2<student_marks<max4+2:
            dict_of_lists["lis_4"].append(student_marks)
        else:
            continue

    for i in range(1,5):
        lis_name=f"lis_{i}"
        dict_of_lists[lis_name].sort()
        info_grade=dict_of_lists[lis_name]
        if len(info_grade)==0:
            continue
        elif len(info_grade)==1:
            continue
        else:
            final_max=0
            final_min=0
            previous_diff=0
            new_diff=-1
            for i in len(info_grade)-1:
                previous_diff=info_grade[i+1]-info_grade[i]
                if previous_diff>new_diff:
                    new_diff=previous_diff
                    final_max=info_grade[i+1]
                    final_min=info_grade[i]
            dict_of_lists[lis_name]=[(final_max+final_min)/2]


    index=-1
    final_grade_dict={x:0 for x in ["A", "B", "C", "D"]}
    for grade in ["A", "B", "C", "D"]:
        index+=1
        lis_name=f"lis_{index+1}"
        info_grade=dict_of_lists[lis_name]
        if len(info_grade)==0:
            final_grade_dict[grade]=grading_policy[index]
        else:final_grade_dict[grade]=info_grade[0]
    final_grade_dict["F"]=f"below {final_grade_dict["D"]}"
    assessments_weight=["assesment and theier weights :"]
    for some_assesment in assesment:
        assessments_weight.append(f"{some_assesment[0]} : {some_assesment[1]}")

    a=final_grade_dict["A"]
    b=final_grade_dict["B"]
    c=final_grade_dict["C"]
    d=final_grade_dict["D"]
    total_a=0
    total_b=0
    total_c=0
    total_d=0
    total_f=0

    for student_info in lis_output:
        roll=student_info[0]
        student_marks=int(student_info[1])
        if student_marks>=a:
            student_info.append("A")
            final_student_dict[roll]["grade"]="A"
            total_a+=1
        elif student_marks>=b:
            student_info.append("B")
            final_student_dict[roll]["grade"]="B"
            total_b+=1
        elif student_marks>=c:
            student_info.append("C")
            final_student_dict[roll]["grade"]="C"
            total_c+=1
        elif student_marks>=d:
            student_info.append("D")
            final_student_dict[roll]["grade"]="D"
            total_d+=1
        else: 
            student_info.append("F")
            final_student_dict[roll]["grade"]="F"
            total_f+=1
    grading_summary=["gradding summary : ",f"total A : {total_a}",f"total B : {total_b}",f"total C : {total_c}",f"total D : {total_d}",f"total F : {total_f}"]

    return corse_name,credits, assessments_weight,final_grade_dict,grading_summary,lis_output,final_student_dict

def prof_interface(cname, credits,assessments,grading_policy):
    final_data=corse_helper(cname, credits,assessments,grading_policy)
    name=final_data[0]
    creds=final_data[1]
    assment_weg=final_data[2]
    final_grade_dict=final_data[3]
    grading_summary=final_data[4]
    student_final=final_data[5]
    final_studen_summ=final_data[6]
    while True:
        order=input("enter the task you would like to perform 1[summary] , 2[all record] , 3[serch student record(by rollnum)]  :")
        if order=="1":
            print(f"{name}   ,      {creds}")
            for assessment in assment_weg:
                print(assessment)
            for k,v in final_grade_dict.items():
                print(f"{k} : {v}")
            for summary in grading_summary:
                print(summary)

        elif order=="2":
            with open("student_final_result.txt","w") as f:
                for data in student_final:
                    for component in data:
                        f.write(f"{component}  ")
                    f.write("\n")


        elif order=="3":
            roll_num=input("enter the roll number of the student : ")
            try:
                particular_student_info=final_studen_summ[roll_num]
                print(particular_student_info["assessments"])
                print(f"Total marks: {particular_student_info["percent"]}")
                print(f"Final grade : {particular_student_info["grade"]}")
            except:
                print("no such student found in the record")


        else:
            break

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
grading_policy = [80, 65, 50, 40] #will have 4 different schemes only

prof_interface(cname,credits,assessments,grading_policy)