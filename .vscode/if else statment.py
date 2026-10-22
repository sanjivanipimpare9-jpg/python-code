# username = input("Enter user name")
# if username == "correct_username":
#     password = input("Enter password:")
#     if password == correct_password:
#         print("logine succesful")
#     else:
#         print("incorrect password")
# else:
#      print("incorrect password")   



# Age = int(input("Enter your age"))
# if Age >= 18:
#    registed = input("Are you register for vote:")
#    if registed == "yes":
#       print("register for vote")
#    else:
#        print("not register")
# else:
#     print("your age is not eligible for register voting")



# marks = float(input("Enter ur marks"))
# if marks >= 35:
#     if marks>= 75:
#         print("your pass with distincation") 
#     else:
#         print("you are pass")
# else:
#     print("you are fali")   

                   #1
# Gread = "C"
# match Gread :
#     case "A" :
#         print( "ur gread A exclent....!")
#     case "B" :
#         print("ur gread B nice....!")
#     case "C":
#         print("ur gread C good...!")
#     case _ :
#         print("better luck next time")

                    #2
# Quarter = "Q3"
# match Quarter :
#     case "Q1" :
#         print("january - march")
#     case "Q2" :
#         print("April - June")
#     case "Q3" :
#         print("July - September")
#     case "Q4" :
#         print("October - December") 
#     case "Q5":
#         print("invalid input")    

                   #3
# num1 = 34
# num2 = 6
# operator = "+" 
# match operator :
#     case "*":
#         result = num1 * num2
#         print(f"result : {num1} * {num2} = {result}")
#     case "+":
#         result = num1 + num2 
#         print(f"result : {num1} + {num2} = {result}") 
#     case "-" :
#         result = num1 - num2
#         print(f"result : {num1} - {num2} = {result}")
#     case "%" :
#         result = num1 % num 
#         print(f"result : {num1} % {num2} = {result}")
#     case _ :
#         print("invalid operator...!")        


                       #4
number = 7
match number %2 :
    case 0:
        print (f"{number} is an evan number")
    case 1:
        print(f"{number} is an odd number")


                        #5
clr = "green"
match clr :
    case 'red':
        print("Stop!")
    case "yellow":
        print("ready for race !")
    case " green":
        print("go!")        
    case _ :
        print("invalid clr....?")


                         #6
Weekend = "saturday"
match Weekend :
    case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
        print("weekday...!")
    case "saturday"|"sunday":
        print("weekend day...!")


                          #7
age = 21
match age :
    case age if age > 18: 
         print("you are adult")
    case age if age < 18:
        print("you are child")


                          #8
order = "order sucessful"
match order:
    case "Order Placed":
        print("your order confirm ")
    case "Out shipped":
        print("shipped your order")
    case "Delivered":
        print("your order tody deliver")
    case "Cancelled":
        print("Your order was cancelled")
    case _:
        print(" Please contact customer support")


                       #9
Numbers= int(input("Enter a number: "))
match Numbers % 2 == 0:
    case True:
        print("Even number")
    case False:
        print("Odd number")


                       #10
weather = "winter"
match weather:
    case "rainy":
      print("don't go out")
    case "winter":
      print("it's very cold outside")
    case "Summer":
      print("Wear sunglasses")
    case _:
      print(" Weather looks nice")



                        





