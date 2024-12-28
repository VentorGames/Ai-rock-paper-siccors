import random

speler = None
ai = None
zetten = ("rock", "paper", "scissors", "rock", "paper", "scissors", "rock", "paper", "scissors")
gedaan = 0
speler_punt = 0
ai_punt = 0

# main loop
naam = input("What is your name: ")
hoeveelkeer = int(input("How many times do you want to play: "))

while True:
    speler = input("rock paper scissors: ")
    
    ai = random.choice(zetten)
    
    if speler == "rock" and ai == "scissors":
        speler_punt += 1
        print("You get a point")
    elif speler == "scissors" and ai == "rock":
        ai_punt += 1
        print("AI gets a point")
    elif speler == "paper" and ai == "rock":
        speler_punt += 1
        print("You get a point")
    elif speler == "rock" and ai == "paper":
        ai_punt += 1
        print("AI gets a point")
    elif speler == "scissors" and ai == "paper":
        speler_punt += 1
        print("You get a point")
    elif speler == "paper" and ai == "scissors":
        ai_punt += 1
        print("AI gets a point")
        
    print(f"AI chose {ai}")
        
    gedaan += 1
    
    if gedaan == hoeveelkeer:
        if speler_punt > ai_punt:
            print(f"{naam} has won!!")
        elif speler_punt == ai_punt:
            print("TIE")
        else:
            print("AI has won!!")
            
        break
