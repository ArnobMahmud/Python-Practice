'''
   Author : Arnob Mahmud

   Mail : arnob.tech.me @ gmail.com
'''
def myfunc():
  x = 300
  y = 200
  z = x + y
  def myinnerfunc():
    print(z)
  myinnerfunc()

myfunc()