name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten  by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water an lost the game.")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (Cross/Back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the brige and meet a stranger. Do you talk to him (Yes/No)? ").lower()

        if answer == "yes":
            print("You talk to a stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")

    else:
        print("Not a valid option. You lose.")

else: 
    print("Not a valid option. You lose.")

print("Thank you for trying,", name + "!")