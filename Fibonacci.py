def Fibonacci(number):
   a = 0
   b = 0
   c = 1
   i = 0
   while i <= number:
      print (str(c)) 
      a = b 
      b = c
      c = b + a 
      i = i + 1 
      
number = int(input("Enter the  number of numbers u want: "))
Fibonacci(number)

