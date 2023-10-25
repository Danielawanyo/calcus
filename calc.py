cal = 0
while cal < 5:
  
  x = float(input('Enter the first number: '))
  y = float(input('Enter the second number: '))

  print('1 for add')
  print('2 for subtract')
  print('3 for multiply')
  print('4 for divide')
  print( '5 to exist')
  ch = int(input('Enter your operator: '))

  if ch == 1:
     c = x + y
     print('sum:', c )

  elif ch == 2:
     c = x - y
     print('Difference:', c )
 
  elif ch == 3:
     c = x * y
     print('Product:', c )

  elif ch == 4:
     if y != 0:
       c = x / y
       print('Division:', c )
     else:
        print('Denominator cannot be 0')
  
  elif ch == 5:
     break
  
  else:
     print('INVALID INPUT.')