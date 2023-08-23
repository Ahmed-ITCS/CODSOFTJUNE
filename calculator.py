import os
os.system("clear")
while(1):
    number1 = input("enter number 1 : ")
    number2 = input("enter number 2 : ")
    operation = input("enter + for addition\nenter - for subtraction\nenter * for multiplication\nenter / for devision :")
    if(operation =="+"):
        print (number1," + ",number2 ," = ",int(number1) + int(number2))
    elif(operation =="-"):
        print (number1," - ",number2 ," = ",int(number1) - int(number2))
    elif(operation =="*"):
        print (number1," * ",number2 ," = ",int(number1) * int(number2))
    elif(operation =="/"):
        print (number1," / ",number2 ," = ",int(number1) / int(number2))