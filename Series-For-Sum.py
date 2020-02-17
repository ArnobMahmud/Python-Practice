'''
   Author : Arnob Mahmud
   Mail : arnob.tech.me @ gmail.com
'''

# 1 + 2 + 3 + ...................... + n

num = int(input("Enter the last number : "))

sum = 0
for x in range( 1, num + 1, 1):
    sum = sum + x

print("Sum is :", sum)

# 2 + 4 + 6 + ..................... + n

num1 = int(input("Enter last value :"))

sum1 = 0
for x in range( 2, num1 + 1, 1):
    sum1 = sum1 + x

print("Sum is :", sum1)

# 1 + 2*2 + 3*3 + 4*4 + ............. + n*n

num2 = int(input("Enter last value :"))

sum2 = 0
for x in range( 2, num2 + 1, 1):
    sum2 = sum2 + x * x

print("Sum is :", sum2)

