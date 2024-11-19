# import csv
# f=open("course.csv","r")
# data=csv.reader(f)

# f=open("cCourseMCA.csv","w",newline="")
# h=csv.writer(f)
# for row in data:
#   if(row[2]=="MCA"):
#     h.writerow(row)
# print("CourseMCA created succesfully")
# f.close()  

f=open("code.txt","r")
print(f.read())
print("read succesfully")

    