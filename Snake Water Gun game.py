import random
print("""Hello friends, welcome to Saacket's Snake Water Gun game.
So let's start the game\n""")
try:
    r = 0
    ys = 0.0
    cs = 0.0

    while r < 10:
        r += 1
        print(f"Round {r} Started...")
        print("Enter your choice: ")
        print("s for snake, w for water and g for gun")
        yc = input().lower()
        rand = random.randint(1,3)
        if rand == 1:
            cc = 's'
            print("Computer choose snake\n")
        elif rand == 2:
            cc = 'w'
            print("Computer choose water\n")
        else:
            cc = 'g'
            print("Computer choose gun\n")

        if (yc=='s' and cc=='s') or (yc=='w' and cc=='w') or (yc=='g' and cc=='g'):
            print(f"Round {r} tied")
            ys = ys + 0.5
            cs = cs + 0.5
            print(f"Your score is {ys}")
            print(f"Computer's score is {cs}\n")

        elif (yc=='s' and cc=='w') or (yc=='w' and cc=='g') or (yc=='g' and cc=='s'):
            ys = ys + 1
            print(f"You won Round {r}!")
            print(f"Your score is {ys}")
            print(f"Computer's score is {cs}\n")

        elif (yc=='w' and cc=='s') or (yc=='g' and cc=='w') or (yc=='s' and cc=='g'):
            cs = cs + 1
            print(f"You lost Round {r}")
            print(f"Your score is {ys}")
            print(f"Computer's score is {cs}\n")

    if ys>cs:
        print("You won this game!")
        input()
    elif ys<cs:
        print("You lost this game")
        input()
    elif ys==cs:
        print("This game tied")
        input()
    else:
        print("Unexpected Error! Try Again.")
        input()

except:
    print("Unexpected Error! Try Again.")
    input()