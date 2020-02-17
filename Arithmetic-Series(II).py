'''
   Author : Arnob Mahmud
   Mail : arnob.tech.me @ gmail.com
'''

num1 = int(input("Enter first value :"))
num2 = int(input("Enter last value :"))
sum = 0

i = num1
while i <= num2:
    print(i)
    sum = sum + pow(i , 2)
    i = i + 2

print("Square sum is :", sum)