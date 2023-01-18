import random
import os
import sys
import time

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1
ROWS = 3
COLUMNS = 3

# symbols for slot machine
symbols = ['cherry', 'lemon', 'orange', 'plum', 'bell', 'bar', 'seven', 'blank']


def save_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))

def load_balance():
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as f:
            content = f.read()
            if content:
                return int(content)
            else:
                return 0
    else:
        return 0


def add_balance():
    while True:
        amount = input("Enter amount to add to balance: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("[Invalid Input]")

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

import os

def spin_reels():
    symbols = ["cherry", "lemon", "orange", "plum", "bell", "bar", "seven", "blank"]
    reels = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
    for i in range(5):
        for reel in reels:
            reel[0], reel[1], reel[2] = random.choice(symbols), random.choice(symbols), random.choice(symbols)
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            for row in reels:
                print(row)
            time.sleep(0.2)
    return reels



def check_win(reels, lines, bet):
    win = 0
    winning_combinations = {
        "cherry": [[1, 1], [2, 2], [0, 0]],
        "lemon": [[0, 1], [1, 2], [2, 0]],
        "orange": [[0, 2], [1, 0], [2, 1]],
        "plum": [[0, 0], [1, 1], [2, 2]],
        "bell": [[2, 0], [1, 1], [0, 2]],
        "bar": [[0, 1], [1, 0], [2, 2]],
        "seven": [[1, 2], [2, 1], [0, 0]],
        "blank": [[0, 1], [1, 2], [2, 0]],
    }
    for line in range(lines):
        for symbol in winning_combinations:
            if [reels[line][0], reels[line][1], reels[line][2]] in winning_combinations[symbol]:
                win += bet
    return win


def main():
    balance = load_balance()
    if balance == 0:
        balance = deposit()
    else:
        print(f"Welcome back! Your current balance is ${balance}.")

    while True:
        print("1. Play game")
        print("2. Add balance")
        print("3. Exit")
        option = input("Choose an option: ")
        if option == "1":
            lines = get_number_of_lines()
            while True:
                bet = get_bet()
                total_bet = bet * lines

                if total_bet > balance:
                    print(f"You can't afford that :) | Your balance is: ${balance}")
                else:
                    break
            balance -= total_bet  # deduct total bet from balance

            # spin the reels
            reels = spin_reels()
            print("Spinning reels...")
            for row in reels:
                print(row)

            # check if player has won
            win = check_win(reels, lines, bet)
            if win > 0:
                print(f"Congratulations, you won ${win}!")
                balance += win
            else:
                print("Sorry, try again.")

            print(f"Your current balance is ${balance}.")
            save_balance(balance)
        elif option == "2":
            add_amt = add_balance()
            balance += add_amt
            print(f"Your new balance is ${balance}")
            save_balance(balance)
        
        elif option == "3":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid option")
main()
