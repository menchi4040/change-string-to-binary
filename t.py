#run it to vscode 

import math


x = (input('enter the word     :'))

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
print(toBinary(x))

k = (input('if you want do it again press y if you dont want press n    : '))
if k == 'n' :
  print('tnx for using this app')
if k == "y" :
 print('enter the world     :')
 v = (input())
 def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
 print(toBinary(v))
 print('tnx for using this app')











