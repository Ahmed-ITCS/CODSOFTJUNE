import requests
import os

choice =[]
score = 0
play = "y"
while(play=="y"):
    os.system("clear")
    score=0
    choice =[]
    print("Welcome to the QUIZ TRIVIA\nyou get 1 score for correct answer and get 1 deducted for wrong answer\n\n\n")
    data = requests.get("https://opentdb.com/api.php?amount=5&category=18")
    data = data.json()
    for i in range(5):
        print("your score is : ",score)
        print(data['results'][i]['question'])
        choice.append(data['results'][i]['correct_answer'])
        for incorrect_answer in data['results'][i]['incorrect_answers']:
            choice.append(incorrect_answer)
        k = 1
        for j in choice:
            print(k,end=" : ")
            print(j)
            k+=1
        answer =input("please enter correct choice :")
        if choice[int(answer)-1] == data['results'][i]['correct_answer']:
            print('Correct Answer')
            score+=1
        else:
            score-=1
            print('\n\nWrong Answer')
            print("the correct answer was ",data['results'][i]['correct_answer'])
        choice=[]
        print("----------------------------------------------\n")
    print("\n your total score is ",score)
    play = input("play again ?\ny for yess\nn for no")

    
