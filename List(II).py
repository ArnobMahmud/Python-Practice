'''
   Author : Arnob Mahmud
   Mail : arnob.tech.me @ gmail.com
'''

num1 = [10, 82, 30, 43, 50]
num1.reverse()                     # numbers orients by reverse style
print(num1)

num2 = [20, 33, 56, 89, 19]        
num2.sort()
print(num2)

num3 = [11, 56, 765, 980, 444]
num3.pop()                          # Delete number from back
num3.pop()                          # 2nd of last number will be deleted
print(num3)

num4 = num3.copy()                  # Copy a list to another list
print(num4)

pos = num3.index(56)                 # Show the position of a element from the list
print(pos)

num5 = [1, 2, 5, 5, 7, 9, 5]
con = num5.count(5)                  # Counts how many time one element remains into the list
print(con)