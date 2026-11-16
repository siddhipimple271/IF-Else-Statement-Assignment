username = input ("enter user name:")
if username== "correct_username":
  password = input("enter password:")
if password == "correct_password":
       print("login successful")
else:
   print ("Icorrect password")    





num = int(input("enter a number:"))
if num >0:
    print("The number is positive")          


num =int( input("enter a number:"))
if num % 2 ==0:
    print("The number is even")
else:
   print("The number is odd")


   
age = int(input("Enter your age: "))

if age >= 18:
     print("Eligible to vote")
else:
     print("Not eligible to vote")

    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
     print("First number is greater")
else:
     print("Second number is greater")

   



ch = "E"

if ch in "aeiouAEIOU":
     print("Character is a vowel")
else:
     print("Character is a consonant")
        
        

marks = int(input("Enter your marks: "))
if marks >= 90:
     print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
     print("Grade: C")
elif marks >= 40:
     print("Grade: D")
else:
    print("Grade: Fail")


    

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
     discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount
print("Discount:", discount)
print("Final amount:", final_amount)


Grade = "d"
match Grade:
      case "a":
        print ("first grade")
      case "b":
         print(" second grade")
      case "c":
         print("third grade")
      case _:
         print("fail")


Quater = "Q4"
match Quater:
    case "Q1":
       print("janary - march")
    case "Q2":
       print("April - juan")
    case "Q3":
       print("jualy- sep")
    case "Q4":
        print("oct-dec")
    case _:
       print("invalide input")


day = 7
match day:
    case 1|2|3|4|5:
       print("weekday")
    case 6|7:
       print("weekend")
    case _:
       print("invalid input")     

 
number = "20 40"

match number:
     case "20 40":
        print("addition")
     case "40 30":
        print("subtration")
     case "20 10":
      print("multiplcation")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

number="subtraction"
match number:
   case"addition":
      print("addition=",num1+num2)  
   case "multiplication":
      print("multiplication=",num1*num2)
   case "subtraction":
      print("subtraction=",num1-num2) 
   case _:
       print("invalide") 
       

activite = 0
match activite:
  case 1:
     print("activite")
  case 0:   
      print("unactivity") 
  case _:
     print("invalid")  


       
battery = 100
match battery:
   case 100:   
     print("battery full")
   case 50:
      print("battery half") 
   case 25:        
      print("battery low")
   case 0:   
      print("battery off")
   case _:
       print("invalid")


atm= 1
match atm: 
   case 1:
      print("check money")
   case 2:
      print("withdraw money")  
   case 3:   
      print("deposit money")
   case 4:   
      print("exit")
   case _:   
      print("invalid")


clr = "red"

match clr:
   case "red":
      print("stop")
   case "yellow":
      print("reday to go")
   case "green":
      print("go")


choise=1

match choise:
   case 1:
      print(10+20)
   case 2:
      print(10-5)
   case 3:
      print(10*5)
   case _:
      print("invalid choice")   


month =7
match month:
   case 1|3:
      print("jan-mar")
   case 4|6 :
      print("april-jun")  
   case 7|9:   
      print("jul-sep")
   case 10|12:
      print("aug-dec")     
   case _:
      print("invalid month")  

age =5
match age:
   case 1|5:
      print("littel child")
   case 6|10:
      print("child")
   case 12|15:
      print("teenager")
   case 20|28:
      print("young")
   case _:
       print("other age")    

sub =50
match sub:
   case 20 |30:
     print("marathi","english")
   case 50:
       print("history","math")  
   case _:
      print("fail")    


      
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


match a,b:
    case "+":
        print("Addition =", a + b)

    case "-":
        print("Subtraction =", a - b)

    case "*":
        print("Multiplication =", a * b)

    case "/":
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")






