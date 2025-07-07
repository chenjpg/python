h = float (input('enter your height in meter: '))
w = float (input('enter your weight in kg: '))
bmi= float ((w/(h**2)))
if bmi < 18.5:
	print('too light')
elif bmi > 18.5 and bmi < 25:
	print('normal')
elif bmi > 25 and bmi < 28:
	print('too weight')
elif bmi > 28 and bmi < 32:
	print('you little fat')
else: 
	print('your are a fat ass!!!')

