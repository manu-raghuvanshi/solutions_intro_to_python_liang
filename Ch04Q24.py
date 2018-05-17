import random

num = random.randint(1,13) #number of the card
sym = random.randint(1,4) #symbol of the card

if num == 1:
    print("The card you picked is the Ace of",end=" ")
elif num == 2:
    print("The card you picked is the Two of",end=" ")
elif num == 3:
    print("The card you picked is the Three of",end=" ")
elif num == 4:
    print("The card you picked is the Four of",end=" ")
elif num == 5:
    print("The card you picked is the Five of",end=" ")
elif num == 6:
    print("The card you picked is the Six of",end=" ")
elif num == 7:
    print("The card you picked is the Seven of",end=" ")
elif num == 8:
    print("The card you picked is the Eight of",end=" ")
elif num == 9:
    print("The card you picked is the Nine of",end=" ")
elif num == 10:
    print("The card you picked is the Ten of",end=" ")
elif num == 11:
    print("The card you picked is the Jack of",end=" ")
elif num == 12:
    print("The card you picked is the Queen of",end=" ")
elif num == 13:
    print("The card you picked is the King of",end=" ")

if sym == 1:
    print("Clubs")
elif sym == 2:
    print("Diamonds")
elif sym == 3:
    print("Hearts")
elif sym == 4:
    print("Spades")
