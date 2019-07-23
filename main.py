import random

aicounter = 0
playercounter = 0

def play():
    playersymbol = input("rock, paper o scissors?: ")
    ainumber = random.randint(0,91)

    if ainumber <= 30:
        aisymbol = "rock"
    elif ainumber > 30 and ainumber <= 60:
        aisymbol = "paper"
    else: aisymbol = "scissors"

    winner(aisymbol, playersymbol)

def winner(aisymbol, playersymbol):
    global playercounter
    global aicounter

    if aisymbol == playersymbol:
        print("DRAW")
    elif aisymbol == "rock" and playersymbol == "scissors":
        aiwin()
        print(f"The A.I bring {aisymbol}, you lose")
    elif aisymbol == "rock" and playersymbol == "paper":
        playerwin()
        print(f"The A.I bring {aisymbol}, you win")
    elif aisymbol == "paper" and playersymbol == "scissors":
        playerwin()
        print(f"The A.I bring {aisymbol}, you win")
    elif aisymbol == "paper" and playersymbol == "rock":
        aiwin()
        print(f"The A.I bring {aisymbol}, you lose")
    elif aisymbol == "scissors" and playersymbol == "rock":
        playerwin()
        print(f"The A.I bring {aisymbol}, you win")
    elif aisymbol == "scissors" and playersymbol == "paper":
        aiwin()
        print(f"The A.I bring {aisymbol}, you lose")
    else:
        if playersymbol == "score":
            print(f"The A.I have {aicounter} and you have {playercounter}")
        else: print("introduce a valid string")

def playerwin():
    global playercounter
    playercounter += 1

def aiwin():
    global aicounter
    aicounter += 1

while playercounter < 3 or aicounter < 3:
    play()
    if playercounter == 3 or aicounter == 3:
        if playercounter == 3:
            print("YOU WIN")
        else:
            print("YOU LOSE")
        break

