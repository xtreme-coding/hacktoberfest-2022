flag = 0

flag2 = 1

while True:

	command = input ('> ').lower()	if (command == 'start'):

		if flag == 0:

			print (' Car Started ...')

			flag = 1 

			flag2 = 0

		else :

			print (' Car Already Started ...')

	elif (command == 'stop'):

		if flag2 == 0:

			print (' Car Stopped ...')

			flag2 = 1

			flag = 0

		else:

			print ('Car Already Stopped')

	elif (command == 'help'):

		print (''' start - Car Start 

 stop - Car Stop

 quit  - Game End ''')

	elif (command == 'quit'):

		break

	else:

		print (" I don't understand ... ")
