import os
os.system("clear")
tasks = []
completed_tasks = []
while(1):
    user_choice = input("\nenter 1 to log task in todo list\nenter 2 delete task\nenter 3 to mark task completed\nenter 4 to see completed task\nenter 5 to see all task\nenter q to quit")
    if(user_choice == "1"):
        task = input("enter task : ")
        tasks.append(task)
        n = 1
        for i in tasks:
            print(n , end=" : ")
            print(i)
            n+=1
            os.system("clear")
    elif(user_choice =="2"):
        n = 1
        for i in tasks:
            print(n , end=" : ")
            print(i)
            n+=1
        task = input("enter task no# you want to delete : ")
        tasks.remove(tasks[int(task)-1])
        os.system("clear")
    elif(user_choice =="3"):
        n = 1
        for i in tasks:
            print(n , end=" : ")
            print(i)
            n+=1
        task = input("enter task no# you want to mark complete : ")
        completed_tasks.append(tasks[int(task)-1])
        tasks.remove(tasks[int(task)-1])
        os.system("clear")
    elif(user_choice =="4"):
        n = 1
        for i in completed_tasks:
            print(n , end=" : ")
            print(i)
            n+=1
    elif(user_choice=="5"):
        n = 1
        for i in tasks:
            print(n , end=" : ")
            print(i)
            n+=1
    elif(user_choice=="q"):
        os.system("clear")
        exit()
    else:
        print('\ninvalid choice\nenter again\n')