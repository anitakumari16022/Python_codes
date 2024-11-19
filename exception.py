# ''' to create your own exception classs'''
# class MCAerror(Exception):
#   pass
  
# try:
#   a=int(input("enter a number="))
#   if(a==0):
#     raise MCAerror("IT IS DIVIVED BY ZERO")
#   b=34/a
#   print(b)
# finally:
#   print("in finally")  



''' WAP to define an Exception PythonError that will be called when we try to access a key in dictionary that is not exist and it shows a message "such key not be exist". '''

# class PythonError(Exception):
#   pass
# try:
#   data ={"Name":"Anita","Course":"MCA","Section":"c"}
#   search=input("enter the key")

#   if (search  not in data.keys()):
#         raise PythonError("Such key does not exist.")
    
# finally:
#   print("key is found dictionery")  



'''WAP to input two numbers from keyboard,then do following tasks on bases of following cases.
case1: if first number is grater than second number then it will raise a user defined exception NumberError with a message that successor is small 
case2: if second number is greater than first number then it will raise a predefined exception IndexError
case3:if both numbers are equal then it will simply display the mathmatical table of an input number'''

class NumberError(Exception):
  try:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    if(n1>n2):
      raise NumberError("Successor is small")
    elif(n1<n2):
      raise IndexError
    else:
      for  i in range(1,11):
        print(n1,"*",i,"=",n1*i)
        
  finally:
    print("succesfull")    
