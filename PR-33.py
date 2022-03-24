Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> print("Hello")
Hello
>>> 9*19-int(float(9*19))
0
>>> 9**19
1350851717672992089
>>> 9*19
171
>>> 9**19-int(float(9**19))
89
>>> values = input()
print(values)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(values)
print(values)
>>> values = input()
5,4
>>> print(values)
5,4
>>> x = input()
5
>>> y = input()
9
>>> print(x)
5
>>> print(x+y)
59
>>> def func():
	x = input()
	y = input()
	print(int(x) + int(x))

	
>>> func()
5
4
10
>>> def func():
	x = input()
	y = input()
	print(int(x) + int(y))

	
>>> func()
5
4
9
>>> def func(X):
	seconds = int(X) / 60
	print(seconds)

	
>>> func(360)
6.0
>>> def func(X):
	seconds = int(int(X) / 60)
	print(seconds)

	
>>> func(360)
6
>>> def func(int time):
	seconds = int(time / 60)
	print(seconds)
	
SyntaxError: invalid syntax
>>> def func(minutes):
	hours = int(minutes) / 60
	minutes %= 60
	print(hours)
	print(seconds)

	
>>> func(190)
3.1666666666666665
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    func(190)
  File "<pyshell#52>", line 5, in func
    print(seconds)
NameError: name 'seconds' is not defined
>>> def func(minutes):
	hours = int(minutes) / 60
	minutes %= 60
	print(hours)
	print(minutes)

	
>>> func(190)
3.1666666666666665
10
>>> def func(minutes):
	hours = int(int(minutes) / 60)
	minutes %= 60
	print(hours)
	print(minutes)

	
>>> func(190)
3
10
>>> def Number5(hoursSleep, minutesSleep, timeToSleep):
	weakUpHours = int(hoursSleep) + int(int(timeToSleep) / 60)
	weakUpMinutes = int(minutesSleep) + int(int(timeToSleep) % 60)
	print(weakUpHours)
	print(WeakUpMinutes)

	
>>> Number5(3,15,180)
6
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    Number5(3,15,180)
  File "<pyshell#66>", line 5, in Number5
    print(WeakUpMinutes)
NameError: name 'WeakUpMinutes' is not defined
>>> def Number5(hoursSleep, minutesSleep, timeToSleep):
	weakUpHours = int(hoursSleep) + int(int(timeToSleep) / 60)
	weakUpMinutes = int(minutesSleep) + int(int(timeToSleep) % 60)
	print(weakUpHours)
	print(weakUpMinutes)

	
>>> Number5(3,15,180)
6
15
>>> def Number6(recomendSleep, higestToSleep, currentSleep)
SyntaxError: invalid syntax
>>> def Number6(recomendSleep, higestToSleep, currentSleep):
	if(currentSleep <= recomendSleep)
	
SyntaxError: invalid syntax
>>> def Number6(recomendSleep, higestToSleep, currentSleep):
	if(currentSleep == recomendSleep):
		print("Это норма")
	elif(currentSleep > recomendSleep):
		print("Пересып")
	else:
		print("Недосып")

		
>>> Number6(8,10,7)
Недосып
>>> def Number7(year):
	if((year % 4 == 0 and year % 100 !=0) or year % 400 == 0):
		print("Високосный")
	else:
		print("Невисокосный")

		
>>> Number7(2000)
Високосный
>>> Number8(2100)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    Number8(2100)
NameError: name 'Number8' is not defined
>>> Number7(2100)
Невисокосный
>>> def Number8(firstNum, secondNum, operator):
	if(operator == '+'):
		print(int(firstNum) + int(secondNum))
	elif(operator == '-'):
		print(int(firstNum)-int(secondNum))

		
>>> Number8(5,4,+)
SyntaxError: invalid syntax
>>> Number8(5,4,'+')
9
>>> def Number8(firstNum, secondNum, operator):
	if(operator == '+'):
		print(int(firstNum) + int(secondNum))
	elif(operator == '-'):
		print(int(firstNum)-int(secondNum))
	elif(operator == '/'):
		print(int(firstNum)-int(secondNum))
	elif(operator == '*'):
		print(int(firstNum)-int(secondNum))
	elif(operator == "mod"):
		print(int(firstNum)-int(secondNum))
	elif(operator == "pow"):
		print(int(firstNum)-int(secondNum))

	
>>> def Number8(firstNum, secondNum, operator):
	if(operator == '+'):
		print(int(firstNum) + int(secondNum))
	elif(operator == '-'):
		print(int(firstNum) - int(secondNum))
	elif(operator == '/'):
		if(secondNum == 0):
			print("Деление на ноль")
			return
		print(int(firstNum) / int(secondNum))
	elif(operator == '*'):
		print(int(firstNum) * int(secondNum))
	elif(operator == "mod"):
		print(int(firstNum) % int(secondNum))
	elif(operator == "pow"):
		print(pow(firstNum, secondNum))
	elif(operator == "div"):
		print(int(firstNum) // int(secondNum))

		
>>> Number8(2,8,"pow")
256
>>> Number8(8,3,"div")
2
>>> Number8(15,9,"mod")
6
>>> Number8(100,0,'/')
Деление на ноль
>>> def Number9(typeShape, a, b, c = 0, r = 0):
	if(typeShape = "Triangle"):
		
SyntaxError: invalid syntax
>>> def Number9(typeShape, a, b, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр 
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =" S)
		
SyntaxError: invalid syntax
>>> def Number9(typeShape, a, b, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр 
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)

		
>>> Number9("Triangle", 5, 4, 3)
Square = 6.0
>>> def Number9(typeShape, a, b, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр 
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		print(3.14 * r * r)

		
>>> def Number9(typeShape, a = 0, b = 0, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр 
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		print(3.14 * r * r)

		
>>> Number9("Circle",5)
0.0
>>> def Number9(typeShape, a = 0, b = 0, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр 
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		print(3.14 * float(r) * float(r))

		
>>> Number9("Circle",5)
0.0
>>> def Number9(typeShape, a = 0, b = 0, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		radius = float(a)
		S = 3.14 * radius * radius
		print("Square =" S)
		
SyntaxError: invalid syntax
>>> def Number9(typeShape, a = 0, b = 0, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		radius = float(a)
		S = 3.14 * radius * radius
		print("Square =", S)

		
>>> Number9("Circle",5)
Square = 78.5
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max" = b)
		
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>>  def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		
SyntaxError: unexpected indent
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average," a)
		
SyntaxError: invalid syntax
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average", a)
	elif(c > b):
		print("Max", c)
		print("Min", b)
		print("Average", a)

		
>>> Number10(5,4,3)
Max 5
Min 3
Average 4
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average", a)
	elif(c > b):
		print("Max", c)
		print("Min", a)
		print("Average", b)

		
>>> Number10(9,15,11)
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average", a)
	elif(c > b):
		print("Max", c)
		print("Min", a)
		print("Average", b)
	else:
		print("Max", b)
		print("Min", a)
		print("Average", c)Number10(9,15,11)
		
SyntaxError: invalid syntax
>>> def Number10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average", a)
	elif(c > b):
		print("Max", c)
		print("Min", a)
		print("Average", b)
	else:
		print("Max", b)
		print("Min", a)
		print("Average", c)

		
>>> Number10(9,15,11)
Max 15
Min 9
Average 11
>>> 