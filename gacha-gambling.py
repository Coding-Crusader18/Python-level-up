import random #imports random built in function
counter=0
weapons=["Wooden Sword","Iron Dagger","Bronze Spear", "Basic Bow","Short Sword","Rusty Axe", "Stone Hammer","Iron Mace","Steel Knife","Wooden Staff","Minigun"]#created a list called weapons

def rools(rolls):#initializing a function
    i=0
    print("these are things you won: ")
    global counter#using global to to upadte the counter variable outside of function

    counter=counter+rolls

    rolls=rolls
    for i in range(1,rolls+1):#using for loop to Iterating 
        random_weapons=random.choice(weapons)
        print(f"{i}.",random_weapons)


soka=input("do you want to wish? \tYES? OR NO?\n")

if soka.lower()=="yes":
    while True:#using while loop to continous looping
        gacha=input("\nhow many wishes do you want to wish? or Q\n")
        if gacha.lower()=="q":
            print("thanks for playing")
            break

        elif gacha:
            try:#making sure the gacha is always in int form
                gacha=int(gacha)#making sure the gacha is always in int form
                rools(gacha)#function calling

            except ValueError:#making sure the gacha is always in int form
                print("only numbers no decimal or words except Q is ok not ok")
                break

            counter=counter
            print(f"\n\n Your total gacha counts is:",counter)#checking if global is working properly
            if counter>=90:#win legenday weapon
                print("you have just got the legendary rocket congrats")


elif soka.lower()=="no":
    print("thank you for playing")

else:
    print("only Yes or NO")



                


        










