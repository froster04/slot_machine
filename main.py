MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

def deposit():
	while True:
		amount = input("Enter deposit amount: $")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				break
			else:
				print("The amount must be greater than 0.")
		else:
			print("[Invalid Input]")
	return amount

def get_number_of_lines():
	while True:
		lines = input("Enter number of lines to bet: (1-"+ str(MAX_LINES)+"): ")
		if lines.isdigit():
			lines = int(lines)
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("Enter valid number of lines.")
		else:
			print("[Invalid Input]")
	return lines

def get_bet():
	while True:
		bet = input("Enter your bet amount: $")
		if bet.isdigit():
			bet = int(bet)
			if MIN_BET <= bet <= MAX_BET:
				break
			else:
				print(f"The amount must be between ${MIN_BET} - ${MAX_BET}.")
		else:
			print("[Invalid Input]")
	return bet

def main():
	balance = deposit()
	lines = get_number_of_lines()
	bet = get_bet()
	total_bet = bet * lines
	print(f"*** YOU ARE BETTING ${bet} on {lines} lines and Total bet is => ${total_bet} ***")
	# print (balance,lines,bet)

main()