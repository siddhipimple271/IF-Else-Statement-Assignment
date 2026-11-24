
class vehicle:
      def start(self):
            print("vehicle is starting")


class Bike(vehicle):
      def ride(self):
            print("Bike is running")

obj =Bike()
obj.start()
obj.ride()   




class mobile:
      def brand(self):
        print("brand: oppo")

class oppo(mobile):
      def price(self):
        print("price: 1200")


obj =oppo()
obj.brand()
obj.price()


class employee:
    def emp_detalis(self):
        self.name ="rahul"
        self.salary =24000

class manager(employee):
    def manager_details(self):
                self.department ="IT"

    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)

obj=manager()
obj.emp_detalis()
obj.manager_details()
obj.display()


class app:
     def name(self): 
       print("send msg: wp")
class whatsapp(app):
      def sendmsg(self):
           print("send msg: insta")
a=whatsapp()
a.sendmsg()
a.name()


#multilevel 


class app:
     def app_name(self):
          print("instual app")
class googel (app):
     def googel (self):
          print("email_id")
class gmail(googel):
     def gmail(self):
          print("send_mail")

d=gmail()
d.googel()
d.gmail()        

class name:
     def name(self):
          print("stud_name")
class roll_no(name):
     def roll_no(self):
         print("stud_no")
class age(roll_no):
     def age(self):
          print("stud_age") 
k=age()
k.name()
k.roll_no
k.age()


class college:
     def college(self):
          self.name ="mgm college"
class department(college):
     def department(self):
          self.department = "Bsc"
class student(department):
      def student(self):
           self.studentname="siddhi"
           self.rollno=101
      def display(self):
           print("collage name:",self.name)
           print("department:",self.department)
           print("student:",self.studentname)
           print("roll number:",self.rollno)

obj=student()
obj.college()
obj.department()
obj.student()
obj.display() 


class company:
     def name(self):
       print("company_name")
class employee(company):
     def employee(self):
          print("employee_salary")
class manager(employee):
     def manager(self):
          print("employee_dep")

A=manager() 
A.name()
A.employee()
A.manager() 
    


#multiple

class frontend:
     def frontend(self):
          print("html")
class backend:
     def backend(self):
          print("python")
class pythonDeveloper(frontend,backend):
     def display(self):
      print("pythonDeveloper")   

obj=pythonDeveloper()
obj.frontend()
obj.backend()
obj.display()


class breakfast:
     def breakfast(self):
          print("breakfast is tasty")
class lunch:
     def lunch(self):
          print("lunch is tasty")
class food(breakfast,lunch):
     def food(self):
          print("food are healthy")
f=food()
f.lunch()
f.breakfast()  
f.food()       

class bank():
     def bank_details(self):
          print("bank name:sbi")
class atm():
     def atm_details(self):
          print("atm: balance check")
class customer (bank,atm):
     def customer_details (self):
          print("customer")
obj=customer()
obj.bank_details()
obj.atm_details()          
obj.customer_details()


class singer():
     def singer(self):
          print("singing a song:")
class dancer():
     def dancer(self):
      print ("great dancer")         
class artist(singer,dancer):
     def display(self):
          print("artist details")
obj1=artist()
obj1.singer()
obj1.dancer()
obj1.display()          

#Hierarchical
class mobile():
     def mobile(self):
          print("use mobile")
class iphone(mobile):
     def iphone(self):
          print("iphone")
class oneplus(mobile):
     def oneplus(self):
          print("one pluse")
t=oneplus()
t.oneplus()
t.mobile()

class employee():
     def employee_details(self):
      print("employee of company")
class manager(employee):
     def manager_details(self):
          print("manager manages team ")
class developer(employee):
     def developer_details(self):
          print("developer writes code")                    

class accountant(employee):
     def accountant_details(self):
          print(" accountant ")

m=manager()
m.manager_details()
m.employee_details()
d=developer()
d.developer_details()  
d.employee_details()
a=accountant()
a.accountant_details()
a.employee_details()