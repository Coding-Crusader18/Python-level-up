Tasks=[]
print("welcome User! This is the first task manager created by DFOCMARU\n")
print("lets get started shall we\n")

try:
    while True:
        add=input("Add a task? Yes or NO?\n")

        if add.lower()=="yes":
            while True:
                takes=input("Enter the task or is it E(enough)\n")
                if takes.lower()=="e":
                    print("great")
                    break
                else:
                    Tasks.append(takes)
                    print("your task has been sucessfully added")



        elif add.lower()=="no":
            print("alright see you next time user")
            break

        else:
            print("sorry! user but our current system only works on Yes and No")


        print("hello user it appears You have some tasks to check")
        
        i=0
        for tasks in Tasks:
            i=i+1
            print(f"{i}.",tasks)

        print("if your task is done you can remove the done tasks")

        while True:
            sub=input("remove a task? yes,no or C (which means completed)?\n")

            if sub.lower()=="c":

                if not Tasks:
                    print("Congrats you did great today")

                    quit()

                else:
                    print("You need to complete these tasks")

                i=0
                for task in Tasks:
                    i=i+1
                    print(f"{i}.", task)

              



        
            elif sub.lower()=="yes":
                takes=input("Enter the task\n")
                Tasks.remove(takes)
                print("your task has been sucessfully removed")

                i=0
                print("Now you have these task's to complete: ")
                for task in Tasks:
                    i=i+1
                    print(f"\n{i}." ,task)



            elif add.lower()=="no":
                print("You need to complete these tasks")

                for task in Tasks:
                    i=i+1
                    print(f"{i}.", task)
            

            else:
                print("sorry! user but our current system only works on Yes,No and C system")



except ValueError:
    print("how are you writng tasks in numbers and decimal?")

