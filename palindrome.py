# to check whether a string is palindrome or not
num=int (input("enter a number:"))
rev=0
temp=num
while(num>0):
  dig=num%10
  rev=rev*10+dig
  num=num//1
if(rev==temp):
  print("number is palindrome")
else:
  print("not a palindrome"),,,
#pg  
n=input("enter a string")
S=[]
for i in n:
  if(i.isalpha()):
    S.append(i)
print(S) 
