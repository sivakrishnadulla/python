#to find calendar using year and month
import calendar   
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))    
print(calendar.month(yy,mm))  

#to find prime number
n = int(input("Enter a number: "))  
  
if n>1:  
   for i in range(2,n):  
       if (n % i) == 0:  
           print(n,"is not a prime number")  
           print(i,"times",n//i,"is",n)  
           break  
   else:  
       print(n,"is a prime number")  
         
else:  
   print(n,"is not a prime number")


for num in range(100,150):
    if all(num%i!=0 for i in range (2,num)):
        print(num)
