#wap  to create  afile student.dat and store one record of the student that record contain name,marks and roll  ///write operation 
'''from text file to binary file'''
# import pickle
# f=open("student.dat","wb")
# d={"Rollno":23,"Name":"Amit","marks":67}
# data=pickle.dumps(d)
# f.write(data)
# print("succesfully")
# f.close
#WAP to read tha data from student.dat and display it on the screen.//read operation
'''from binary file to text file
import pickle
f=open("student.dat","rb")
data=f.read()
s=pickle.loads(data)
print("loaded succesfully")
print(s)
f.close()'''

# WAP to input number of records N and store such records whithin a file Employe.dat.Each record conatain Empid,EmpName,Designation,Salary.
'''import pickle
n=int(input("enter the number of records="))
l=[]
for i in range(n):
  empid=int(input("enter empid="))
  empname=input("enter Emp name=")
  des=input("enter Emp designation=")
  salary=int(input("enter the salary="))
  d={"empid":empid,"EmpName":empname,"designation":des,"salary":salary}
  l.append(d)
f=open("Employe.dat","wb")
data=pickle.dumps(l)
f.write(data)
print("successfully")
f.close()'''

# import pickle
# f=open("Employe.dat","rb")
# data=f.read()
# s=pickle.loads(data)
# # print(s)
# for i in s:
#   print(i)
# f.close() 

