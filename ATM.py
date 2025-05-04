banners = "-------------------------------------"
print(banners)
heading = "welcome to the ATM services"
print(heading.upper())
print(banners)

account= {
	'name': 'uthman',
	'PIN':1234,
	'balance':00,
	'transaction': []
}

Tries = 0
while Tries < 3:
	in_pin = int(input ("Please enter the PIN for your account!\n"))
	if in_pin == account['PIN']:
		print(f"welcome {account['name']}!\n")
		break
	else:
		Tries += 1
		print("Wrong PIN! Please try again!\n")

if Tries == 3:
	print("Exceeded the trial limit! \nExiting.....")
	exit()

running = True 
while running:
	print("Please select your choice!")
	choice = int (input (f"1. Withdraw\n2. Deposit\n3. Check balance\n4. Quit\n{banners}\n"))
	#print(banners)

	if choice == 1:
		with_amount = int (input ("please enter the amount u want to withdraw\n"))
		if int(with_amount) > int(account['balance']):
			print("Insufficient funds. Please try again")
		else:
			new_balance = account['balance'] - with_amount
			account['balance'] = new_balance
			print (f"The amount {with_amount} was successfully withdrawn. New balanace is {account['balance']}")
	elif choice == 2:
		dep_amount = int(input("Please enter the amount you are depositig\n"))
		account['balance'] += dep_amount

		print (f"Transaction successful. Your new balance is {account['balance']}")
	elif choice == 3:
		print(f"Your balance is {account['balance']}")
	elif choice == 4:
		print (f"Thank you!")
		running = False 
