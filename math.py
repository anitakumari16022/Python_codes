import csv
f=open("course.csv","r")
data=csv.reader(f)
a=open("course_mca.csv","w")
a=csv.writer(a)
for row in data:
  if(row[2]=="mca"):
    a.writerow(row)
print("course  created") 
a.close()
f.close()
