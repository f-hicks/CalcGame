


#Importing libaries
from inputimeout import inputimeout, TimeoutOccurred
import os
import sys
import time
import random
from colorama import init, Fore, Style
from subprocess import call
init()

def flush_input():
	import msvcrt
	while msvcrt.kbhit():
		sys.warnoptionsmsvcrt.getch()


nameCheck = []


#Creating the clearconsole function
clearConsole = lambda: os.system('cls')
#prints the highest score
clearConsole()
print(Fore.YELLOW + "UPDATE(2.7):x2 Streak powers!",Fore.BLUE + "││",Fore.YELLOW + "Current version(2.7.1)")
print()
print(Fore.RED + "Hard maintainability: if someone takes your spot from the leaderboard,")
print("then you will be erased from the leaderboard entirely! ")
print()
time.sleep(0.8)
print(Fore.MAGENTA + "High Scores:")
time.sleep(0.1)
readScore1st = open("1stScore.txt", "r")
readName1st = open("1stName.txt", "r")
readDifficulty1st = open("1stDifficulty.txt", "r")
readDifficultyVari1st = readDifficulty1st.read()
readScoreVari1st = readScore1st.read()
readNameVari1st = readName1st.read()
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
print(Fore.YELLOW + "Rank no.1" + Fore.WHITE + "│", Fore.YELLOW + readScoreVari1st, "point(s) by", readNameVari1st,"- Difficulty:",readDifficultyVari1st)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore1st.close()
readName1st.close()


#prints the next highest score
readScore2nd = open("2ndScore.txt", "r")
readName2nd = open("2ndName.txt", "r")
readDifficulty2nd = open("2ndDifficulty.txt", "r")
readScoreVari2nd = readScore2nd.read()
readNameVari2nd = readName2nd.read()
readDifficultyVari2nd = readDifficulty2nd.read()
print(Style.BRIGHT  + Fore.RED +  "Rank no.2" + Fore.WHITE + "│", Fore.RED + readScoreVari2nd, "point(s) by", readNameVari2nd, "- Difficulty:",readDifficultyVari2nd)
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore2nd.close()
readName2nd.close()
readDifficulty2nd.close()


#prints the next highest score
readScore3rd = open("3rdScore.txt", "r")
readName3rd = open("3rdName.txt", "r")
readDifficulty3rd = open("3rdDifficulty.txt", "r")
readScoreVari3rd = readScore3rd.read()
readNameVari3rd = readName3rd.read()
readDifficultyVari3rd = readDifficulty3rd.read()
print(Fore.CYAN + "Rank no.3" + Fore.WHITE + "│",Fore.CYAN + readScoreVari3rd, "point(s) by", readNameVari3rd,"- Difficulty:",readDifficultyVari3rd)
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore3rd.close()
readName3rd.close()
readDifficulty3rd.close()


#prints the next highest score
readScore4th = open("4thScore.txt", "r")
readName4th = open("4thName.txt", "r")
readDifficulty4th = open("4thDifficulty.txt", "r")
readScoreVari4th = readScore4th.read()
readNameVari4th = readName4th.read()
readDifficultyVari4th = readDifficulty4th.read()
print("Rank no.4" + Fore.WHITE + "│", readScoreVari4th, "point(s) by", readNameVari4th,"- Difficulty:",readDifficultyVari4th)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore4th.close()
readName4th.close()
readDifficulty4th.close()


#prints the next highest score
readScore5th = open("5thScore.txt", "r")
readName5th = open("5thName.txt", "r")
readDifficulty5th = open("5thDifficulty.txt", "r")
readScoreVari5th = readScore5th.read()
readNameVari5th = readName5th.read()
readDifficultyVari5th = readDifficulty5th.read()
print("Rank no.5│", readScoreVari5th, "point(s) by", readNameVari5th,"- Difficulty:",readDifficultyVari5th)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.1)
print()
readScore5th.close()
readName5th.close()
readDifficulty5th.close() 



#prints the instructions of the game with adequete delays.
import time

print(Fore.GREEN + "This is a game where you have to find the correct operation that caused the first two numbers to turn into the last.")
time.sleep(0.3)
print()
print("Getting an answer correct gives you points but getting one incorrect takes points away.")
time.sleep(0.3)
print()
print("If you don't answer a question in time, you will lose points (affected by difficulty).")
time.sleep(0.3)
print()
print("Score as high as you can in 5 rounds. Also changing the difficulty changes how hard each question is. ")
time.sleep(0.3)
print()	
print(Fore.CYAN + "If you answer all the questions correctly in a game, you will gain and lose more points next game (streak multiplier).")
print("And also activate streak powers which helps you in various ways (mostly)")
print()

while True:
	try:
		  
		which = input(Fore.MAGENTA + "View challenger leaderboard (y/n): ").lower()
		if which == "y" or which == "n":
			break
		else:
			which = int("f")
	except:
		print(Fore.RED + "Invalid")
		 

if which == "y":
	clearConsole()
	call(["python", "chalLeader.py"])

turns = "y"
streak = 1
startReady = "p"
while turns == "y":
	tries = 6
	

# creates each operation to be used multiple times. 
	def getSum(num1, num2):
		return(num1 + num2)

	def getDifference(num1, num2):
		return(num1 - num2)
	
	def getProduct(num1, num2):
		return(num1 * num2)

	def getQuotient(num1, num2):
		return(num1 / num2)
	
	clearConsole()
	if startReady == "p":
		print(Fore. GREEN + "1 = Easy")
		time.sleep(0.2)
		print(Fore.YELLOW + Style.DIM + "2 = Medium")
		time.sleep(0.2)
		print(Fore.RED + Style.NORMAL + "3 = Hard",Fore.GREEN + "")
		time.sleep(0.2)

#asks for a difficulty to be selected with checks in place
	if startReady == "p":
		while True:
			try:
				  
				flush_input()
				difficulty = int(input("Choose a difficultly level: "))
				if difficulty > 3 or difficulty < 1:
					difficulty = int("f")
				break
			except ValueError:
				print(Fore.RED + "")
				print("Invalid, try again", Fore.GREEN + "")
				 
	print()
	clearConsole()

# determines the reduction and gain of points		
	points = 500 * streak 
	reduction = 50 * streak
	gain = 75 * streak


#displays the difficulty
	print(Fore.MAGENTA + "Streak multiplier:",Fore.CYAN + str(streak))
	print()
	if streak == 1:
		print(Fore.MAGENTA + "This is where you gain and lose points based on the number above.")
		print("For example, seeing a 2 will cause your point gain and reduction to double")
		print("This number increases every time you press play again but resets back to 1 if you get an answer incorrect.")
		print("This only applies to normal mode")
		time.sleep(0.2)
	elif streak == 10:
		print("You have reached maxium streak")
		time.sleep(0.2)
	print()
	if difficulty == 1:
		print(Fore.GREEN + "Difficulty 'easy' has been selected;")
		time.sleep(0.2)
		print(Fore.BLUE + "")
		print("Or type 'p' to practice")
		time.sleep(0.2)
	elif difficulty == 2:
		print(Fore.YELLOW + "Difficulty 'medium' has been selected")
		time.sleep(0.2)
		print(Fore.BLUE + "")
		print("Or type 'p' to practice")
		time.sleep(0.2)
	elif difficulty == 3:
		print(Fore.RED + "Difficulty 'hard' has been selected")
		print()
		time.sleep(1)
		print("Type 'c' to play the hardest difficulty (if you dare)")
		print("This contains harder points to gain and a short time to answer")
		print(Fore.BLUE + "")
		time.sleep(0.2)
		print("Or type 'p' to practice")
		time.sleep(0.2)
	else:
		print(Fore.RED + "Difficulty 'challenger' has been selected")
		time.sleep(0.2)
		print(Fore.BLUE + "")
		print("Or type 'p' to practice")
	time.sleep(0.5)

	startingPoints = points
	other1 = 0
	other2 = 0
	correct = 0
	incorrect = 0
	randStreak = 0

#starts countdown sequence when something is typed 
	print()	
	flush_input()
	  
	if startReady == "c":
		difficulty = 4

	startReady = input(Fore.YELLOW + "Press enter to play normally (normal mode) or type in one of the above options: ").lower()
	clearConsole()
	if startReady == "c" and streak == 1:
		difficulty = 4
		clearConsole()
		print("Get ready challenger")
		time.sleep(1.5)
	elif startReady == "p":
		clearConsole()
		print("practice mode enabled")
		print()
		print("Answer as many questions as you want with no time limit")
		time.sleep(1)
	elif startReady == "c"  and difficulty != 4:
		clearConsole()
		print(Fore.RED + "Access denied due to your streak being too high")

	if streak > 1:
		randStreak = random.randint(1, 20) #0, 20
		if randStreak > 0 and randStreak < 7:
			print(Fore.GREEN + "You found a common streak power!")
			print()
			randC = random.randint(1,2)
			if randC == 1:
				print("+ 50 points per each correct answer") #10
				gain += 50
			elif randC == 2:
				print("+ 15% points per each correct answer") #5%
				gain += (gain / 100) * 15

		elif randStreak > 6 and randStreak < 10:
			print(Fore.BLUE + "You found a rare streak power!")
			print()
			randR = random.randint(1,2)
			if randR == 1:
				print("Your streak is increased by one")
				streak += 1
			elif randR == 2:
				print("Timeout length is increased by 3 seconds") #2

		elif randStreak == 10 or randStreak == 11:
			print(Fore.MAGENTA + "You found an epic streak power!")
			print()
			randE = random.randint(1,2)
			if randE == 1:
				print("Your streak is protected even if you get an answer incorrect")
				incorrect = -5
			elif randE == 2:
				print("+ 500 points per correct answer")
				gain += 100

		elif randStreak == 12:
			print(Fore.YELLOW + "You found a legendary streak power!!")
			print()
			randL = random.randint(1,2)
			if randL == 1:
				print("There is no timer for this round!")
				time.sleep(0.75)
				print("And start with double the amount of points!")
				points *= 2
			elif randL == 2:
				print("All questions in one!")
				time.sleep(0.75)
				print("And gain a bonus 30% of your points gained")
				gain += (gain / 100) * 30
				gain *= 5
				tries = 2
		else:
			print(Fore.RED + "No streak power found for this round")
		time.sleep(2.5)
		print()
	else:
		print(Fore.CYAN + "Gain a streak above 1 to have a chance to get a streak power")
		print()
		time.sleep(2.5)

		
	print(Fore.YELLOW + "3")
	 
	print()
	time.sleep(0.4)
	print("2")
	 
	print()
	time.sleep(0.4)
	print("1")
	 
	print()
	time.sleep(0.4)
	print("Go!")
	 
	 
	time.sleep(0.7)

	if startReady == "p":
		tries = 0
		points = 0
		clearConsole()
		call(["python", "practice.py"])

	
	

# determines number range based on difficultly
	while tries > 1:
		operationFinal = random.randint(0, 3)
		if difficulty == 1:
			num1 = random.randint(25,100) 
			num2 = random.randint(1,25) 
			timer = 11
		elif difficulty == 2:
			num1 = random.randint(25, 150) 
			num2 = random.randint(-25, 25)
			timer = 8.5 
		elif difficulty == 3:
			num1 = random.randint(-50, 150) 
			num2 = random.randint(-100, -50)
			timer = 6
		else:
			num1 = random.randint(-50, 150) 
			num2 = random.randint(-100, -50)
			timer = 4

		if randStreak > 6 and randStreak < 10 and randR == 2:
			timer += 3
			randStreak = 0

# checks for / by 0 error and changes values of nums if this is true
		if num1 == 0 or num2 == 0:
			while num1 == 0 or num2 == 0:
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
				else:
					num1 = random.randint(-50, 150) 
					num2 = random.randint(-100, -50)
					
	

# creates an answer based on what random operation has been picked		
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
	
	
#outputs all of the nessesery info to the user and also decreases the remaining rounds	
		tries -= 1
		print(Fore.YELLOW)
		clearConsole()
		print(tries,"question(s) remaining")
		print()
		print("Your current amount of points:",points)
		print(Fore.CYAN + "------------------------------------------------------------------") 
		print(Fore.YELLOW + "The numbers",num1, "and",  num2, "turn into the number", answer)
		print()
		print(Fore.CYAN + "1 = addition")
		print("2 = subtraction")
		print("3 = multiplication")
		print("4 = division (to nearest integer)")
		

#asks the user to guess which operation has happened (error handling in place)	
		while True:
			try:
				print()
				  
				flush_input()
				if randStreak == 12:
					choice = int(input(Fore.MAGENTA + "What operation has happened here: "))
				else:
					choice = int(inputimeout(prompt = Fore.MAGENTA + "What operation has happened here: ", timeout = timer))
				if choice > 4 or choice < 1:
					choice = int("f")
				break
			except ValueError: 
				print(Fore.RED + "Invalid")
				time.sleep(0.5)
				choice = 7
				break
			except TimeoutOccurred:
				choice = 6
				print()
				print("timed out")
				time.sleep(0.5)
				break

#checks whether the user is correct		
		if choice == 1:
			choice = choice - 1
			if choice == operationFinal:
				clearConsole()
				print(Fore.GREEN + " Correct!")
				correct += 1
				 
				print()
				print(" +",gain,"points")
				time.sleep(1.25)
				points = points + gain
			else:
				clearConsole()
				print(Fore.RED + " Incorrect")
				incorrect += 1
				 
				print()
				print(" -", reduction,"points")
				time.sleep(0.8)
				print()
				print(Fore.GREEN + "Correct answer:", corAns)
				time.sleep(1.7)
				points = points - reduction

		elif choice == 2:
			choice = choice - 1
			if choice == operationFinal:
				clearConsole()
				print(Fore.GREEN + " Correct!")
				correct += 1
				 
				print()
				print(" +",gain,"points")
				time.sleep(1.25)
				points = points + gain
			else:
				clearConsole()
				print(Fore.RED + " Incorrect")
				incorrect += 1
				 
				print()
				print(" -", reduction,"points")
				time.sleep(0.8)
				print()
				print(Fore.GREEN + "Correct answer:", corAns)
				time.sleep(1.7)
				points = points - reduction
		
		elif choice == 3:
			choice = choice - 1
			if choice == operationFinal:
				clearConsole()
				print(Fore.GREEN +" Correct!")
				correct += 1
				 
				print()
				print(" +",gain,"points")
				time.sleep(1.25)
				points = points + gain
			else:
				clearConsole()
				print(Fore.RED + " Incorrect")
				incorrect += 1
				 
				print()
				print(" -", reduction,"points")
				time.sleep(0.8)
				print()
				print(Fore.GREEN + "Correct answer:", corAns)
				time.sleep(1.7)
				points = points - reduction
		
		elif choice == 4:
			choice = choice - 1
			if choice == operationFinal:
				clearConsole()
				print(Fore.GREEN + " Correct!")
				correct += 1
				 
				print()
				print(" +",gain,"points")
				time.sleep(1.25)
				points = points + gain
			else:
				clearConsole()
				print(Fore.RED + " Incorrect")
				incorrect += 1
				 
				print()
				print(" -", reduction,"points")
				time.sleep(0.8)
				print()
				print(Fore.GREEN + "Correct answer:", corAns)
				time.sleep(1.7)
				points = points - reduction
	

		elif choice == 6:
			clearConsole()
			print(Fore.RED + " Timed out!")
			 
			print()
			print(" - 10 points")
			time.sleep(0.8)
			print()
			print(Fore.GREEN + "Correct answer:", corAns)
			time.sleep(1.7)
			points = points - (10 * streak)
			other1 += 1

		elif choice == 7:
			clearConsole()
			print(Fore.RED + "Invalid")
			 
			print()
			print(" - 5 points")
			time.sleep(1.25)
			points = points - (5 * streak)
			other2 +=1

		
	


#displays the final amount of points and checks if the user is on hard difficlulty for the leaderboard. 			
	clearConsole()
	print(Fore.YELLOW + "You earned",points,"Points! Well done")
	print()
	while True:
		try:
			  
			flush_input()
			viewPoints = input(Fore.MAGENTA + "View how you earned these points (y/n): ").lower()
			if viewPoints == "y" or viewPoints == "n":
				break
			else:
				viewPoints = int("f")
		except:
			 
			print(Fore.RED + "Invalid")
	
	if viewPoints == "y" and startReady != "p":
		clearConsole()
		print(Fore.YELLOW + "Started with:",startingPoints)
		print()
		time.sleep(0.1)
		print(Fore.RED + "But lost",incorrect*reduction,"points to incorrect answers" )
		print()
		time.sleep(0.1)
		print("And also lost",(other1*10)+(other2*5),"points to other sources")
		time.sleep(0.1)
		print()
		print(Fore.GREEN + "But gained",correct*gain,"points")
		time.sleep(0.1)
		print()
		print(Fore.YELLOW + "And so earned a total of",points,"points")
		flush_input()
		enter = input("Press enter to continue: ")
		clearConsole()

	elif viewPoints == "y" and startReady == "p":
		print()
		print(Fore.RED + "To view points, play a game in 'normal' mode by pressing play again")
		time.sleep(4)
		clearConsole()
	clearConsole()
	incorrect = incorrect + other1 + other2
		

#opens all the text files storing the high score details and assigns the content of each to a different variable
	scoreFile5th = open("5thScore.txt", "r")
	potNewScore5th = float(scoreFile5th.readline())

	scoreFile4th = open("4thScore.txt", "r")
	potNewScore4th = float(scoreFile4th.readline())

	scoreFile3rd = open("3rdScore.txt", "r")
	potNewScore3rd = float(scoreFile3rd.readline())

	scoreFile2nd = open("2ndScore.txt", "r")
	potNewScore2nd = float(scoreFile2nd.readline())

	scoreFile1st = open("1stScore.txt", "r")
	potNewScore1st = float(scoreFile1st.readline())

	scoreFileChallenger1st = open("ChallengerScore1st.txt", "r")
	potNewScoreChallenger1st = float(scoreFileChallenger1st.readline())

	scoreFileChallenger2nd = open("ChallengerScore2nd.txt", "r")
	potNewScoreChallenger2nd = float(scoreFileChallenger2nd.readline())

	scoreFileChallenger3rd = open("ChallengerScore3rd.txt", "r")
	potNewScoreChallenger3rd = float(scoreFileChallenger3rd.readline())

	scoreFileChallenger4th = open("ChallengerScore4th.txt", "r")
	potNewScoreChallenger4th = float(scoreFileChallenger4th.readline())

	scoreFileChallenger5th = open("ChallengerScore5th.txt", "r")
	potNewScoreChallenger5th = float(scoreFileChallenger5th.readline())



		

	scoreFile5th.close()
	scoreFile4th.close()
	scoreFile3rd.close()
	scoreFile2nd.close()
	scoreFile1st.close()
	scoreFileChallenger1st.close()
	scoreFileChallenger2nd.close()
	scoreFileChallenger3rd.close()
	scoreFileChallenger4th.close()
	scoreFileChallenger5th.close()

	if difficulty == 1:
		difficulty = "easy"
	elif difficulty == 2:
		difficulty = "medium"
	elif difficulty == 3:
		difficulty = "hard"
	else:
		difficulty = "challenger"


#checks if the amount of points is high enough for each rank on the highscore leaderboard
#also if the above is true, then asks the user to enter their name (error handling in place)
#it is then written to each file, overriding what there was there before.
	if difficulty == "challenger":
		if points > potNewScoreChallenger5th:
			if points > potNewScoreChallenger4th:
				if points > potNewScoreChallenger3rd:
					if points > potNewScoreChallenger2nd:
						if points > potNewScoreChallenger1st:
							points = str(points)
							f = open("ChallengerScore1st.txt", "w")
							f.write(points)
							x = open("ChallengerName1st.txt", "w")
							while True:
								try:
						
									flush_input()
									newName = input(Fore.MAGENTA + "Enter your name for the CHALLENGER leaderboard (must be < 11 char): ")
									
									for letters in newName:
										nameCheck.append(letters)
									if len(nameCheck) >= 11:
										newName = int("f") 
									x.write(newName)
									break
								except:
									print(Fore.RED + "Invalid try again")
									 
									nameCheck.clear()
							x.close()
							f.close()
						else:
							points = str(points)
							f = open("ChallengerScore2nd.txt", "w")
							f.write(points)
							x = open("ChallengerName2nd.txt", "w")
							while True:
								try:
									flush_input()
									newName = input(Fore.MAGENTA + "Enter your name for the CHALLENGER leaderboard (must be < 11 char): ")
									for letters in newName:
										nameCheck.append(letters)
									if len(nameCheck) >= 11:
										newName = int("f") 
									x.write(newName)
									break
								except:
									print(Fore.RED + "Invalid try again")
									 
									nameCheck.clear()
							x.close()
							f.close()
					else:
						points = str(points)
						f = open("ChallengerScore3rd.txt", "w")
						f.write(points)
						x = open("ChallengerName3rd.txt", "w")
						while True:
							try:
								flush_input()
								newName = input(Fore.MAGENTA + "Enter your name for the CHALLENGER leaderboard (must be < 11 char): ")
								for letters in newName:
									nameCheck.append(letters)
								if len(nameCheck) >= 11:
									newName = int("f") 
								x.write(newName)
								break
							except:
								print(Fore.RED + "Invalid try again")
								 
								nameCheck.clear()
						x.close()
						f.close()
				else:
					points = str(points)
					f = open("ChallengerScore4th.txt", "w")
					f.write(points)
					x = open("ChallengerName4th.txt", "w")
					while True:
						try:
							flush_input()
							newName = input(Fore.MAGENTA + "Enter your name for the CHALLENGER leaderboard (must be < 11 char): ")
							for letters in newName:
								nameCheck.append(letters)
							if len(nameCheck) >= 11:
								newName = int("f") 
							x.write(newName)
							break
						except:
							print(Fore.RED + "Invalid try again")
							 
							nameCheck.clear()
					x.close()
					f.close()
			else:
				points = str(points)
				f = open("ChallengerScore5th.txt", "w")
				f.write(points)
				x = open("ChallengerName5th.txt", "w")				
				while True:
					try:
						flush_input()
						newName = input(Fore.MAGENTA + "Enter your name for the CHALLENGER leaderboard (must be < 11 char): ")
						for letters in newName:
							nameCheck.append(letters)
						if len(nameCheck) >= 11:
							newName = int("f") 
						x.write(newName)
						break
					except:
						print(Fore.RED + "Invalid try again")
						 
						nameCheck.clear()
				x.close()
				f.close()


	elif points > potNewScore5th:
		if points > potNewScore4th:
			if points > potNewScore3rd:
				if points > potNewScore2nd:
					if points > potNewScore1st:
						points = str(points)
						f = open("1stScore.txt", "w")
						f.write(points)
						x = open("1stName.txt", "w")
						y = open("1stDifficulty.txt","w")
						y.write(difficulty)
						while True:
							try:
								
								flush_input()
								newName = input(Fore.MAGENTA + "Enter your name for the leaderboard (must be < 11 char): ")
								
								for letters in newName:
									nameCheck.append(letters)
								if len(nameCheck) >= 11:
									newName = int("f") 
								x.write(newName)
								break
							except:
								print(Fore.RED + "Invalid try again")
								 
								nameCheck.clear()
						f.close()
						x.close()
						y.close()
					else:
						points = str(points)
						f = open("2ndScore.txt", "w")
						f.write(points)
						x = open("2ndName.txt", "w")
						y = open("2ndDifficulty.txt","w")
						y.write(difficulty)
						while True:
							try:
								
								flush_input()
								newName = input(Fore.MAGENTA + "Enter your name for the leaderboard (must be < 11 char): ")
								
								for letters in newName:
									nameCheck.append(letters)
								if len(nameCheck) >= 11:
									newName = int("f") 
								x.write(newName)
								break
							except:
								print(Fore.RED + "Invalid try again")
								 
								nameCheck.clear()
						f.close()
						x.close()
						y.close()
				else:
					points = str(points)
					f = open("3rdScore.txt", "w")
					f.write(points)
					x = open("3rdName.txt", "w")
					y = open("3rdDifficulty.txt","w")
					y.write(difficulty)
					while True:
						try:
							
							flush_input()
							newName = input(Fore.MAGENTA + "Enter your name for the leaderboard (must be < 11 char): ")
							
							for letters in newName:
								nameCheck.append(letters)
							if len(nameCheck) >= 11:
								newName = int("f") 
							x.write(newName)
							break
						except:
							print(Fore.RED + "Invalid try again")
							 
							nameCheck.clear()
					f.close()
					x.close()
					y.close()
			else:
				points = str(points)
				f = open("4thScore.txt", "w")
				f.write(points)
				x = open("4thName.txt", "w")
				y = open("4thDifficulty.txt","w")
				y.write(difficulty)
				while True:
					try:
						
						flush_input()
						newName = input(Fore.MAGENTA + "Enter your name for the leaderboard (must be < 11 char): ")
						
						for letters in newName:
							nameCheck.append(letters)
						if len(nameCheck) >= 11:
							newName = int("f") 
						x.write(newName)
						break
					except:
						print(Fore.RED + "Invalid try again")
						 
						nameCheck.clear()
				f.close()
				x.close()
				y.close()
		else:
			points = str(points)
			f = open("5thScore.txt", "w")
			f.write(points)
			x = open("5thName.txt", "w")
			y = open("5thDifficulty.txt","w")
			y.write(difficulty)
			while True:
				try:
					
					flush_input()
					newName = input(Fore.MAGENTA + "Enter your name for the leaderboard (must be < 11 char): ")
					
					for letters in newName:
						nameCheck.append(letters)
					if len(nameCheck) >= 11:
						newName = int("f") 
					x.write(newName)
					break
				except:
					print(Fore.RED + "Invalid try again")
					 
					nameCheck.clear()
			f.close()
			x.close()
			y.close()
			
	while True:
		try:
			flush_input()
			  
			turns = input(Fore.YELLOW + "Go again (y/n): ").lower()
			if turns == "y" or turns == "n":
				break
			else:
				turns = int("f")
		except ValueError:
			print(Fore.RED + "Invalid try again")
			 
	if turns == "y":
		print()
		if incorrect < 1 and startReady != "p":	
			streak += 1
			incorrect = 0
		if incorrect > 0 or startReady == "p":
			streak = 1
		if streak > 10:
			print(Fore.MAGENTA + "Congrats on getting here! Your streak will now reset")
			streak = 1
			time.sleep(3)
			clearConsole()
		print(Fore.BLUE + "NOTE; if you just played in normal mode, you can no longer change your difficulty unless you choose practice mode")
		print()
		time.sleep(0.2)
		print("But in doing so, it removes streak stacks. But after ending your pracice session, you can change your difficulty again")
		print()
		time.sleep(0.2)
		enter = input("Press enter to continue")
		if difficulty == "easy":
			difficulty = 1
		elif difficulty == "medium":
			difficulty = 2
		elif difficulty == "hard":
			difficulty = 3
		else:
			difficulty = 4

	
	#displays the new leaderboard

clearConsole()
#prints the highest score
print(Fore.RED + "Hard maintainability: if someone takes your spot from the leaderboard,")
print("then you will erased be from the leaderboard entirely! ")
print()
time.sleep(0.8)
print(Fore.MAGENTA + "High Scores:")
time.sleep(0.1)
readScore1st = open("1stScore.txt", "r")
readName1st = open("1stName.txt", "r")
readDifficulty1st = open("1stDifficulty.txt", "r")
readDifficultyVari1st = readDifficulty1st.read()
readScoreVari1st = readScore1st.read()
readNameVari1st = readName1st.read()
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
print(Fore.YELLOW + "Rank no.1" + Fore.WHITE + "│", Fore.YELLOW + readScoreVari1st, "point(s) by", readNameVari1st,"- Difficulty:",readDifficultyVari1st)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore1st.close()
readName1st.close()


#prints the next highest score
readScore2nd = open("2ndScore.txt", "r")
readName2nd = open("2ndName.txt", "r")
readDifficulty2nd = open("2ndDifficulty.txt", "r")
readScoreVari2nd = readScore2nd.read()
readNameVari2nd = readName2nd.read()
readDifficultyVari2nd = readDifficulty2nd.read()
print(Style.BRIGHT  + Fore.RED +  "Rank no.2" + Fore.WHITE + "│", Fore.RED + readScoreVari2nd, "point(s) by", readNameVari2nd, "- Difficulty:",readDifficultyVari2nd)
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore2nd.close()
readName2nd.close()
readDifficulty2nd.close()


#prints the next highest score
readScore3rd = open("3rdScore.txt", "r")
readName3rd = open("3rdName.txt", "r")
readDifficulty3rd = open("3rdDifficulty.txt", "r")
readScoreVari3rd = readScore3rd.read()
readNameVari3rd = readName3rd.read()
readDifficultyVari3rd = readDifficulty3rd.read()
print(Fore.CYAN + "Rank no.3" + Fore.WHITE + "│",Fore.CYAN + readScoreVari3rd, "point(s) by", readNameVari3rd,"- Difficulty:",readDifficultyVari3rd)
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore3rd.close()
readName3rd.close()
readDifficulty3rd.close()


#prints the next highest score
readScore4th = open("4thScore.txt", "r")
readName4th = open("4thName.txt", "r")
readDifficulty4th = open("4thDifficulty.txt", "r")
readScoreVari4th = readScore4th.read()
readNameVari4th = readName4th.read()
readDifficultyVari4th = readDifficulty4th.read()
print("Rank no.4" + Fore.WHITE + "│", readScoreVari4th, "point(s) by", readNameVari4th,"- Difficulty:",readDifficultyVari4th)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore4th.close()
readName4th.close()
readDifficulty4th.close()


#prints the next highest score
readScore5th = open("5thScore.txt", "r")
readName5th = open("5thName.txt", "r")
readDifficulty5th = open("5thDifficulty.txt", "r")
readScoreVari5th = readScore5th.read()
readNameVari5th = readName5th.read()
readDifficultyVari5th = readDifficulty5th.read()
print("Rank no.5│", readScoreVari5th, "point(s) by", readNameVari5th,"- Difficulty:",readDifficultyVari5th)
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.1)
print()
readScore5th.close()
readName5th.close()
readDifficulty5th.close() 
time.sleep(1)
print(Fore.YELLOW + "If you scored high enough, you should be able to view your score here")
print()
print()

while True:
	try:
		  
		which = input(Fore.MAGENTA + "View challenger leaderboard (y/n): ").lower()
		if which == "y" or which == "n":
			break
		else:
			which = int("f")
	except:
		 
		print(Fore.RED + "Invalid")

print()
if which == "y":
	clearConsole()
	call(["python", "chalLeader.py"])

while True:
	try:
		flush_input()
		  
		wipe = int(input(Fore.RED + "Do you wish to reset the leaderboard 1=yes 2=no: "))
		if wipe > 2:
			wipe = int("f")
		break
	except ValueError:
		(Fore.RED + "Invalid try again")
		 

# opens and wipes the leaderboard
if wipe == 1:
	readScore5th = open("5thScore.txt", "w")
	readName5th = open("5thName.txt", "w")
	readDifficulty5th = open("5thDifficulty.txt", "w")
	readScore4th = open("4thScore.txt", "w")
	readName4th = open("4thName.txt", "w")
	readDifficulty4th = open("4thDifficulty.txt", "w")
	readScore3rd = open("3rdScore.txt", "w")
	readName3rd = open("3rdName.txt", "w")
	readDifficulty3rd = open("3rdDifficulty.txt", "w")
	readScore2nd = open("2ndScore.txt", "w")
	readName2nd = open("2ndName.txt", "w")
	readDifficulty2nd = open("2ndDifficulty.txt", "w")
	readScore1st = open("1stScore.txt", "w")
	readName1st = open("1stName.txt", "w")
	readDifficulty1st = open("1stDifficulty.txt", "w")
	readScoreChallenger1st = open("challengerScore1st.txt", "w")
	readNameChallenger1st = open("challengerName1st.txt", "w")
	readScoreChallenger2nd = open("challengerScore2nd.txt", "w")
	readNameChallenger2nd = open("challengerName2nd.txt", "w")
	readScoreChallenger3rd = open("challengerScore3rd.txt", "w")
	readNameChallenger3rd = open("challengerName3rd.txt", "w")
	readScoreChallenger4th = open("challengerScore4th.txt", "w")
	readNameChallenger4th = open("challengerName4th.txt", "w")
	readScoreChallenger5th = open("challengerScore5th.txt", "w")
	readNameChallenger5th = open("challengerName5th.txt", "w")
	
	readScore5th.write("0")
	readScore4th.write("0")
	readScore3rd.write("0")
	readScore2nd.write("0")
	readScore1st.write("0")
	readScoreChallenger1st.write("0")
	readScoreChallenger2nd.write("0")
	readScoreChallenger3rd.write("0")
	readScoreChallenger4th.write("0")
	readScoreChallenger5th.write("0")
	
	readName5th.write("")	
	readName4th.write("")
	readName3rd.write("")
	readName2nd.write("")
	readName1st.write("")
	readNameChallenger1st.write("")
	readNameChallenger2nd.write("")
	readNameChallenger3rd.write("")
	readNameChallenger4th.write("")
	readNameChallenger5th.write("")
	
	readDifficulty5th.write("")
	readDifficulty4th.write("")
	readDifficulty3rd.write("")
	readDifficulty2nd.write("")
	readDifficulty1st.write("")
	
	readScore5th.close()
	readName5th.close()
	readDifficulty5th.close()
	readScore4th.close()
	readName4th.close()
	readDifficulty4th.close()
	readScore3rd.close()
	readName3rd.close()	
	readDifficulty3rd.close()
	readScore2nd.close()
	readName2nd.close()
	readDifficulty2nd.close()
	readScore1st.close()
	readName1st.close()
	readDifficulty1st.close()
	readNameChallenger1st.close()
	readScoreChallenger1st.close()
	readNameChallenger2nd.close()
	readScoreChallenger2nd.close()
	readNameChallenger3rd.close()
	readScoreChallenger3rd.close()
	readNameChallenger4th.close()
	readScoreChallenger4th.close()
	readNameChallenger5th.close()
	readScoreChallenger5th.close()
	clearConsole()
	print(Fore.GREEN + "Successfully cleared leaderboard")
	time.sleep(2.5)

clearConsole()
print(Fore.YELLOW + "Ending session")
sys.exit()

	



	

	
	 
