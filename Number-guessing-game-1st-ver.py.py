import random

max_number=10
number = random.randint(1,max_number)
print("Hello user welcome to my number guessing game.\n\n")

while True:
    
    try:
        b=int(input("guess a number from 0 to 10\n\n"))

        if b==number:
            print("good job it was indeed", number )
            conditionn=input("good job in correct answer, wanna go next level?\n Yes \t No \n\n")

            while True:
                if conditionn.lower()=="yes":
                    max_number=max_number+10
                    number=random.randint(1,max_number)
                    b=int(input(f"guess a number from 0 to {max_number}\n"))

                    if b==number:
                        print("good job it was indeed\n\n number=", number,"\n")

                    else:
                        print("sorry you were wrong, it was",number,"Try from beginning\n\n")
                        quit()
                        break

                else:
                    print("Thank you for playing\n")
                    break

    
        else:
            print("wrong! it was", number)
    except ValueError:
        print("Hello I asked for number")

    z=input("do you want to play again?\n\n")

    if z.lower()=="yes":
        print("alright")
    elif z.lower()=="no":
        break
    else:
        print("fool, try again\n\n")
        break
     
    
