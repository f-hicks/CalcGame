import random
import os
import time  
from colorama import init, Fore, Style
import platform
init()

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

oS = platform.system()

if oS == 'Windows':
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')
	
def getSum(num1, num2):
	return(num1 + num2)

def getDifference(num1, num2):
	return(num1 - num2)
	
def getProduct(num1, num2):
	return(num1 * num2)

def getQuotient(num1, num2):
	return(num1 / num2)

answer = "0"

print(Fore.GREEN + "1 = Easy")
time.sleep(0.2)
print(Fore.YELLOW + Style.DIM + "2 = Medium")
time.sleep(0.2)
print(Fore.RED + Style.NORMAL + "3 = Hard",Fore.GREEN + "")
time.sleep(0.2)

#asks for a difficulty to be selected with checks in place
while True:
	try:
		flush_input()
		difficulty = int(input("Choose a difficultly level to practice in (can be changed later): "))
		if difficulty > 3 or difficulty < 1:
			difficulty = int("f")
		break
	except ValueError:
		print(Fore.RED + "")
		print("Invalid, try again")
		 

while answer != "end":
	operationFinal = random.randint(0, 3)
	if difficulty == 1:
		num1 = random.randint(25,100) 
		num2 = random.randint(1,25) 

	elif difficulty == 2:
		num1 = random.randint(25, 150) 
		num2 = random.randint(-25, 25)

	elif difficulty == 3:
		num1 = random.randint(-50, 150) 
		num2 = random.randint(-100, -50)
	
	if operationFinal == 0:
		corAns = "addition"
		answer = getSum(num1, num2)
	elif operationFinal == 1:
		corAns = "subtraction"
		answer = getDifference(num1, num2)
	elif operationFinal == 2:
		corAns = "multiplication"
		answer = getProduct(num1, num2)
	elif operationFinal == 3:
		corAns = "division"
		answer = getQuotient(num1, num2)
			
	answer = round(answer)


	clear()
	print(Fore.YELLOW + "Type 'end' to finish")
	print("Press enter to skip a question")
	print(Fore.MAGENTA + "")
	print("Type 'd' to change the difficulty")
	if difficulty == 1:
		print("You are playing on",Fore.GREEN + "'easy'",Fore.MAGENTA + "difficulty")
	elif difficulty == 2:
		print("You are playing on",Fore.YELLOW +  "'medium'",Fore.MAGENTA +  "difficulty")
	else:
		print("You are playing on",Fore.RED + "'hard'",Fore.MAGENTA + "difficulty")
	print(Fore.CYAN + "------------------------------------------------------------------") 
	print(Fore.YELLOW + "The numbers",num1, "and",  num2, "turn into the number", answer)
	print()
	print(Fore.CYAN  + "1 = addition")
	print("2 = subtraction")
	print("3 = multiplication")
	print("4 = division (to nearest integer)")

	flush_input()
	choice = input(Fore.MAGENTA + "What operation has happened here: ")

	if choice == "1":
		choice = int(choice)
		choice = choice - 1
		if choice == operationFinal:
				clear()
				print(Fore.GREEN + " Correct!")
				 
				print()
				time.sleep(1.25)

		else:
			clear()
			print(Fore.RED + " Incorrect")
			 
			print()
			print(Fore.GREEN + "Correct answer:", corAns)
			time.sleep(1.7)


	elif choice == "2":
		choice = int(choice)
		choice = choice - 1
		if choice == operationFinal:
			clear()
			print(Fore.GREEN + " Correct!")
			 
			print()
			time.sleep(1.25)

		else:
			clear()
			print(Fore.RED + " Incorrect")
			 
			print()
			print(Fore.GREEN + "Correct answer:", corAns)
			time.sleep(1.7)

		
	elif choice == "3":
		choice = int(choice)
		choice = choice - 1
		if choice == operationFinal:
			clear()
			print(Fore.GREEN +" Correct!")
			 
			time.sleep(1.25)

		else:
			clear()
			print(Fore.RED + " Incorrect")
			 
			print()
			print(Fore.GREEN + "Correct answer:", corAns)
			time.sleep(1.7)

		
	elif choice == "4":
		choice = int(choice)
		choice = choice - 1
		if choice == operationFinal:
			clear()
			print(Fore.GREEN + " Correct!")
			 
			time.sleep(1.25)
		else:
			clear()
			print(Fore.RED + " Incorrect")
			 
			print()
			print(Fore.GREEN + "Correct answer:", corAns)
			time.sleep(1.7)
	
	elif choice == "":
		print()

	elif choice == "end":
		break
		clear()

	elif choice == "d":
		clear()
		print(Fore.GREEN + "1 = Easy")
		time.sleep(0.2)
		print(Fore.YELLOW + Style.DIM + "2 = Medium")
		time.sleep(0.2)
		print(Fore.RED + Style.NORMAL + "3 = Hard",Fore.GREEN + "")
		time.sleep(0.2)

		#asks for a difficulty to be selected with checks in place
		while True:
			try:
				flush_input()
				  
				difficulty = int(input("Choose a difficultly level to practice in (can be changed later): ")) 
				if difficulty > 3 or difficulty < 1:
					difficulty = int("f")
				break
			except ValueError:
				print(Fore.RED + "")
				print("Invalid, try again")
				 
	
	else:
		clear()
		print(Fore.RED + " Invalid")
		 
		print()
		print(Fore.GREEN + "Correct answer:", corAns)
		time.sleep(1.7)

		
