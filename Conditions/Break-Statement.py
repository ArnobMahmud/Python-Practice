'''
   Author : Arnob Mahmud
   Mail : arnob.tech.me @ gmail.com
'''

num = int(input("Enter starting number :"))
n = int(input("Enter ending number :"))

i = num
while i <= n:
    print(i)
    if i % 13 == 0:
        break;                 # Breaks the loop if the upper condition been right
    i = i + 1
