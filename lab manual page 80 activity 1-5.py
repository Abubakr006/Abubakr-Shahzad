Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sum=0
>>> for i in range(5):
...     sum=sum+i
... print("sum=",sum)
SyntaxError: invalid syntax
>>> print("sum=",sum)
sum= 0
>>> sum=0
>>> for i in range(11):
...     sum=sum+i
...     print("sum=",sum)
... 
...     
sum= 0
sum= 1
sum= 3
sum= 6
sum= 10
sum= 15
sum= 21
sum= 28
sum= 36
sum= 45
sum= 55
>>> sum=0
>>> i=1
>>> while i<=10:
...     sum=sum+i
...     i=i+1
...     print("sum=",sum)
... 
...     
sum= 1
sum= 3
sum= 6
sum= 10
sum= 15
sum= 21
sum= 28
sum= 36
sum= 45
sum= 55
sum=0
for i in range(5):
    s=input("enter an integer value...")
    n=int(s)
    sum=sum+n
    print("sum of given values is ",sum)

    
enter an integer value...1
sum of given values is  1
enter an integer value...2
sum of given values is  3
enter an integer value...3
sum of given values is  6
enter an integer value...4
sum of given values is  10
enter an integer value...5
sum of given values is  15
sum=0
s=input("enter an in teger value...")
enter an in teger value...1
n=int(s)
while n!=0:
    sum=sum+n
    s=input("enter an integer value...")
    n=int(s)
    print("sum of given values is ",sum)

    
enter an integer value...10
sum of given values is  1
enter an integer value...521
sum of given values is  11
enter an integer value...5
sum of given values is  532
enter an integer value...22
sum of given values is  537
enter an integer value...0
sum of given values is  559
s=input("enter an integer value...")
enter an integer value...21
n=int(s)
f=0
for i in range(2,int(n/2)):
    r=n%i
    if r==0:
        f=1
        break
    if f==0:
        print("the given number is prime")
    else:
        print("the given number is not prime")

        
the given number is prime
