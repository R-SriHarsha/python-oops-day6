#write a python program to print factorial of a given number using class
#and methods

class number:
   
    def factorial(self,n):
        
        p=1
        for i in range(1,n+1):
            p*=i
        
        print("factorial of given no:",p)
        

obj=number()
obj.factorial(int(input()))
