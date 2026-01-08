total_course=[]
count=0
condition=True
while True:
    course=input()
    a=course.split(" ")
    total_course.append(a)
    count+=1
    if len(a)<2:
        # condition=False
        count-=1
        total_course.pop()
        print(total_course)
        break
    else:

        if not a[1].isdigit()==True:
            print("incorrect credit")
            condition=False
            a.pop()
            count-=1

            break


        if not a[0].isalnum()==True:
            print("incorrect credit")
            a.pop()
            count-=1
            condition=False
            break

        if not (a[2]=="A+" or a[2]=="A" or a[2]=="A-" or a[2]=="B" or a[2]=="C" or a[2]=="C-" or a[2]=="D" or  a[2]=="D-" or a[2]=="F"):
            print("incorrect grade")
            a.pop()
            count-=1
            condition=False
            break
if condition==True:
    for i in range(count):
        print(total_course[i][0]," : ",total_course[i][2])
 
    def SGPA(count,total_course):
        grade=0
        gpa=[]
        total_credit=0


        for num in range(count):
            symbol=total_course[num][2]
            if symbol=="A+":grade=10
            if symbol=="A":grade=10
            if symbol=="A-":grade=9
            if symbol=="B":grade=9-1
            if symbol=="B-":grade=8-1
            if symbol=="c":grade=7-1
            if symbol=="c-":grade=6-1
            if symbol=="D":grade=5-1
            if symbol=="D-":grade=4-1
            if symbol=="F":grade=3-1
            credit=(int(total_course[num][1]))
            total_credit+=credit

            gpa.append(credit*grade)

        return(sum(gpa)/total_credit)
    

    print(round(SGPA(count,total_course),2))

def test():
    assert SGPA(1,[['CSE101', '4', 'D',]])==4     
    assert SGPA(1,[['CSAI301', '4', 'A',]])==10      
    assert SGPA(1,[['ECE201', '2', 'B',]])==8       

test()
