list1 = [2,3,5,6]
userinputNumber = int(input('enter a number>>>>>>>>>>: '))

if(userinputNumber in list1):
  index = list1.index(userinputNumber)
  print('number exist ', userinputNumber , "in index number", index)
else:
  print('value doesnot exist in list')  



#   //////////////using function //////////////


list1 = [2,3,5,6,7,9,0,1,90,80,67,45,23,45,70]
userinputNumber = int(input('enter a number>>>>>>>>>>>>>>: '))
def number(userinputNumber,list1):
  if(userinputNumber in list1):
    index = list1.index(userinputNumber)
    print('number exist ', userinputNumber , "in index number", index)
  else:
    print('value doesnot exist in list')  

number(userinputNumber,list1)    