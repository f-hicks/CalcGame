import time
from colorama import init, Fore, Style
init()
import os  
clearconsole = lambda: os.system("cls")
print(Fore.RED + "Hard maintainability: if someone takes your spot from the leaderboard,")
print("then you will erased from the leaderboard entirely! ")
print()
time.sleep(0.8)
print(Fore.MAGENTA + "High Scores:")
time.sleep(0.1)
readScore1st = open("challengerScore1st.txt", "r")
readName1st = open("challengerName1st.txt", "r")
readScoreVari1st = readScore1st.read()
readNameVari1st = readName1st.read()
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
print(Fore.YELLOW + "Rank no.1" + Fore.WHITE + "│", Fore.YELLOW + readScoreVari1st, "point(s) by", readNameVari1st,"- Difficulty: challenger")
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore1st.close()
readName1st.close()


#prints the next highest score
readScore2nd = open("challengerScore2nd.txt", "r")
readName2nd = open("challengerName2nd.txt", "r")
readScoreVari2nd = readScore2nd.read()
readNameVari2nd = readName2nd.read()
print(Style.BRIGHT  + Fore.RED +  "Rank no.2" + Fore.WHITE + "│", Fore.RED + readScoreVari2nd, "point(s) by", readNameVari2nd, "- Difficulty: challenger")
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore2nd.close()
readName2nd.close()


#prints the next highest score
readScore3rd = open("challengerScore3rd.txt", "r")
readName3rd = open("challengerName3rd.txt", "r")
readScoreVari3rd = readScore3rd.read()
readNameVari3rd = readName3rd.read()
print(Fore.CYAN + "Rank no.3" + Fore.WHITE + "│",Fore.CYAN + readScoreVari3rd, "point(s) by", readNameVari3rd,"- Difficulty: challenger")
print(Fore.WHITE + Style.NORMAL + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore3rd.close()
readName3rd.close()


#prints the next highest score
readScore4th = open("challengerScore4th.txt", "r")
readName4th = open("challengerName4th.txt", "r")
readScoreVari4th = readScore4th.read()
readNameVari4th = readName4th.read()
print("Rank no.4" + Fore.WHITE + "│", readScoreVari4th, "point(s) by", readNameVari4th,"- Difficulty: challenger")
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.05)
readScore4th.close()
readName4th.close()


#prints the next highest score
readScore5th = open("challengerScore5th.txt", "r")
readName5th = open("challengerName5th.txt", "r")
readScoreVari5th = readScore5th.read()
readNameVari5th = readName5th.read()
print("Rank no.5│", readScoreVari5th, "point(s) by", readNameVari5th,"- Difficulty: challenger")
print(Fore.WHITE + "─────────│─────────────────────────────────────────────────────────────────│")
time.sleep(0.1)
print()
readScore5th.close()
readName5th.close()

  
enter = input("Press enter to continue: ")
clearconsole()
