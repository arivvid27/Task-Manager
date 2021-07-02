import os
from replit import db
from time import sleep

Admin_user = os.environ['Admin_user']
Admin_password = os.environ['Admin_password']

username = input('Account Username? > ')
if username == Admin_user:
	pass_check = input('What is the password? > ')
	if pass_check == Admin_password:
		print("Access Granted")
		option = input('Would you like to delete or add? > ')
		if option == 'delete':
			print('Ok!')
			print('Here are all the usernames and passwords to delete:')
			value = db.values()
			print(value)
elif username not in db:
	new_account = input(f'This account name does not exist, would you like to make an account using the name, {username}? > ')
	if new_account == 'yes':
		print('Ok!')
		db["username"] = username
		new_password = input('What would you like your password to be? > ')
		db['password'] = new_password
		sleep(2)
		print('Your Account is now set!')
		print('Restart to login to your account.')
		exit(120)
	elif new_account == 'no':
		print('Ok!')
		print('Quitting...')
		sleep(2)
		exit(120)
elif username == db:
	password = input('Account Password? > ')
	if password != db:
		password_nomatch = input('This password is incorrect, would you like to reset your password? > ')
		if password_nomatch == 'yes':
			del db["password"]
			print('Ok!')
			password_reset = input("What would you like your password to be? > ")
			db["password"] = password_reset
			print('Your password is now reset.')
			print('Restart to login to your account.')
			exit(120)
		elif password_nomatch == 'no':
			print('Ok!')
			print('Restart the program to get another try at logging in.')
			exit(120)
