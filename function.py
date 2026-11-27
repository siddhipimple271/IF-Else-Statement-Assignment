def student_info(name, age, city):
          print("name",name)
          print("age",age)
          print("city",city)

student_info(name="siddhi",age= 34,city ="pune")


def calculator(a,b):
        add =a+b
        sub =a-b
        mul =a*b
        div =a/b
        return add,sub,mul,div

print(calculator(12,3))



def hello():
        print("hello world....!")
hello()
hello()


print("program started")
def display():
     print("inside program..!")
     print ("out side progeram")
def display():
        print("good morning")
display()



print("program started")
def display():
        print("inside program")
print("before calling")  

display()
print("ended....!")


def addition(a,b):
        print(a+b)
addition(2,4)
addition(1,9)
print("two num addition")

print("hello")
def display():
        print("before ")
display()


#no args without return type
  
def add():
     a =5;
     b=6;
     print(a+b)
add()      

     
#args without return type

def mul (a,b):
     print(a*b)
mul(10,11)   

#no args with return type
def add():
     a = 7
     b = 6
     return a+b
print(add())


def sub():
    a =5
    b =6
    print(a-b)
    sub()


def add():
  a = 11
  b = 12
  c = a+b
print("addition is: ")

add()

def outer():
    print("hi")
    def inner():
     print("hello")
outer()     