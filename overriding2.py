class cafe:
    def food_order(self):
        print("cafe is taking food orders")
class pizza(cafe):
    def food_order(self):
        print("pizza ordered successfully")
class burger(cafe):
    def food_order(self):
        print("burger ordered successfully")
obj=pizza()
obj.food_order()

obj1=burger()
obj1.food_order()


class functionHall:
    def program(self):
        print("function hall is booked")
class wedding(functionHall):
    def program(self):
        print("wedding program is running")
class birthday(functionHall):
    def program(self):
        print("birthday program is running")

obj1=wedding()
obj1.program()

obj2=birthday()
obj2.program()


class mobile:
    def call(self):
        print("normal calling")
class samsung(mobile):
    def call(self):
        print("samsung video calling")
obj=samsung()
obj.call() 


class shopping:
    def payment(self):
        print("shopping...!offline payment")

class onlineshopping(shopping):
    def payment(self):
        print("shopping...!online payment")
show=onlineshopping()
show1=shopping()
show.payment()
show1.payment()


class english():
    def book(self):
        print("read english book")
class marathi():
    def book(self):
        print("read marathi book")
d=marathi() 
d.book()

class school():
    def teaching (self):
        print("general teaching")
class computer(school):
    def teaching(self):
        print("computer teaching")
obj=computer()
obj.teaching()


class banana ():
    def tree(self):
        print("banana tree")
class apple (banana):
    def tree(self):
        print("apple tree")
s=apple()
s.tree()               


class googlepay():
    def app(self):
        print("onlinepay = googlepay")
class phonepay(googlepay):
    def app(self):
        print("onlinepay = phonepay")
obj=phonepay()
obj.app()     


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog bark")

obj = Dog()
obj.sound()


class regular_customer ():
    def shopping(self):
        print("20% off")
class premium_customer(regular_customer):
    def shopping(self):
        print("20% off")   
you=premium_customer()
you.shopping()

class fan():
    def speed(self):
        print("fan is starting")
class smartfan(fan):
    def speed(self):        
       print("rotating a table fan")
t=smartfan()
t.speed()

class perfume():
    def smell(self):
        print("perfume is nice fragrance")
class roseperfume(perfume):
    def smell(self):
        print("roseperfume is nice fragrance")
r=roseperfume()
r1=perfume()
r1.smell()
r.smell()

class hospital():
    def treatment(self):
        print("hospital  treatment")
class childhospital():
    def treatment(self): 
        print("child treatment")
h=childhospital()
h.treatment() 


class manager():
    def salary(self):
        print("manager")
class employee(manager):
    def salary(self):
        print("employee")
caul=employee()
caul.salary()


class transport():
    def travel (self):
        print("son is traveling")
class bus( transport):
    def travel(self):
        print("daughert is travelling")

t=bus()
t.travel()
t1=transport()
t1.travel()


class dress():
    def wear(self):
        print("wear a differnt types of  dresses")
class saree(dress):
    def wear(self):
        print("wear saree is traditional style")

a=saree()
a.wear()

class game():
    def play (self):
        print("play a game")
class cricket(game):
    def play(self):
        print("play a cricket")
obj = cricket()
obj.play() 


class camera():
    def capture(self):
        print("click photo")
class mobilecamera(camera):
    def capture(self):
        print("click a video")
c = mobilecamera()
c.capture()