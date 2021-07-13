
a= 10
i= 1
while i<=a:
	b=6
	guess= int(input('enter your guess'))
	i= i+1
	if guess>b:
		print('guess bada hai')
	elif guess<b:
		print('guess chota hai')
	else:
		print("barabar hai")
		break