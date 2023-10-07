import random
computer_choice=int(random.randint(1,3))
human_choice =int(input("do you choice rock 1 or paper 2 or scissors"))

if human_choice >3 :
    print("this is not a true number")

else:

    if human_choice == computer_choice:
        print(f"computer choice was {computer_choice} draw")
    elif human_choice == 1 and computer_choice == 2 :
        print(f"computer choice was {computer_choice} you lose")

    elif human_choice == 1 and computer_choice == 3 :
        print(f"computer choice was {computer_choice} you win")


    elif human_choice == 2 and computer_choice == 1 :
        print(f"computer choice was {computer_choice} you win")


    elif human_choice == 2 and computer_choice == 3 :
        print(f"computer choice was {computer_choice} you lose")

    elif human_choice == 3 and computer_choice == 1 :
        print(f"computer choice was {computer_choice} you lose")

    elif human_choice == 3 and computer_choice == 2 :
        print(f"computer choice was {computer_choice} you win")

    else:
        print(computer_choice)