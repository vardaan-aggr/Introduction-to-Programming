shape=[(1,2,0),(3,4,0),(5,6,0)]#this will  create a row wise matrix ex:(2,3,1)is the first row
scalex=int(input("enter scale x : "))

# scalex=2
scaley=int(input("enter scale y :"))
# scaley=3
multiply_matrix=[(scalex,0,0),(0,scaley,0),(0,0,1)]#this is a  create a colom wise matrix ex (scalx,0,0 )is the first colom
matrix_lis=[]
num_row=0
for row in shape:
    num_row+=1
    cr1=row[0]
    cr2=row[1]
    cr3=row[2]
    for colum in multiply_matrix:
        c1c=colum[0]
        c2c=colum[1]
        c3c=colum[2]
        element=cr1*c1c + cr2*c2c + cr3*c3c
        matrix_lis.append(element)
    print(matrix_lis)
    matrix_lis=[]

# print(matrix_lis)
# lis=[]
# for i in range(num_row):
#     a=[]
#     a.append(matrix_lis[i*3])
#     a.append(matrix_lis[i*3+1])
#     lis.append(a)
#     a=[]
# print(lis)