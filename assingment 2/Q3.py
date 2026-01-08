with open ("yearbook.txt","r") as f:
    lines=f.readlines()
    total_lines=len(lines)
lis_students=[]
num_student=[]
with open ("yearbook.txt","r") as f:
    for i in range (total_lines):
        line=f.readline()
        if i==total_lines-1:
            num_student.append(count)
        if ":" in line :
            lis_students.append(line)
            if i != 0:
                num_student.append(count)
            count=0
        else:
            a=line.split(",")
            num=eval(a[1])
            count+=num
index=-1
loaction_max=[]
loaction_min=[]
largest=0
smallest=0
for i in num_student:
    if largest<i:
        largest=i
    if smallest>i:
        smallest=i
for num_sig in num_student:
    index+=1
    if num_sig==largest:
        loaction_max.append(index)
    if num_sig==smallest:
        loaction_min.append(index)

# local max is a list of the indexes where max number of signatures are there
# local min is a list of the indexes where min number of signatures are there
print("\n")
var=-1
for i in lis_students:
    var+=1
    for j in loaction_max:
        if j==var:
            print(f"{(i.strip())} has maximum signatures = {largest}",end="\n")
    for j in loaction_min:
        if j==var:
            print(f"{(i.strip())} has minimum signatures = {smallest}",end="\n")
# print(lis_students)
# print(num_student)
print("\n")

