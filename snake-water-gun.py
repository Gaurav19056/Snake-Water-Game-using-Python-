import random
#0--> snake.....1-->water......2-->gun
print("---")
print("Welcome to Snake, Water, Gun!")
print("Rules: Snake drinks Water, Water douses Gun, Gun kills Snake.")
print("---")
computer=random.choice([0,1,2])
your_choice=int(input("0 for snake,1 for water,2 for gun: "))
if(your_choice==computer):
    print("\n---")
    print("  🤝🤝🤝")
    print("DRAW!!")
    print("  🤝🤝🤝")
    print("\n---")
else:
    if(your_choice==0 and computer==1):
        print("\n---")
        print("  🎉🎉🎉")
        print("you win!!")
    elif( your_choice==0 and computer==2):
        print("you lose!!")
    elif(your_choice==1 and computer==0):
        print("you lose!!")
    elif(your_choice==1 and computer==2):
        print("\n---")
        print("  🎉🎉🎉")
        print("you win!!")
    elif(your_choice==2 and computer==0):
        print("\n---")
        print("  🎉🎉🎉")
        print("you win!!")
    elif(your_choice==2 and computer==1):
        print("you lose!!")
    else:
        print("invalid input")
print("thank you for playing!! ;)")
