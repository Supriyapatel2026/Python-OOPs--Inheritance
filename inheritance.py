# #1.Student Management System (Single Inheritance)

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Student(Person):
#     def __init__(self,name, age, roll_no, course):
#         super().__init__(name,age)
#         self.roll_no= roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)

# s1 = Student("Supriya", 17, 101, "AIPA")
# s1.display_student()



# #2.Bank Account System (Single Inheritance)

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate/100
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", interest)

# b1 = SavingAccount(12345, 10000, 5)
# b1.deposit(2000)
# b1.calculate_interest()


# #3.Family Assets (Multilevel Inheritance)

# class Grandfather:
#     def house(self):
#         print("Grandfather has a House")

# class Father(Grandfather):
#     def bike(self):
#         print("Father has a Bike")

# class Son(Father):
#     def phone(self):
#         print("Son has a Phone")


# s1 = Son()
# s1.house()
# s1.bike()
# s1.phone()



# #4.Employee Hierarchy (Multilevel Inheritance)

# class Person():
#     def get_name(self):
#         self.name = "Ankit"
#         print("Name:", self.name)

# class Employee(Person):
#     def salary(self):
#         self.sal = 25000
#         print("Salary:", self.sal)

# class Manager(Employee):
#     def team_size(self):
#         self.size = 10
#         print("Team Size:", self.size)

# m = Manager()
# m.get_name()
# m.salary()
# m.team_size()

            
# #5.College Management System (Hierarchical Inheritance)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def show_student(self):
#         self.display()
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def show_teacher(self):
#         self.display()
#         print("Subject:", self.subject)


# s = Student("Mushkan",20,85)
# t = Teacher("Amit", 35, "Python")

# print("Student Details")
# s.show_student()

# print("\nTeacher Details")
# t.show_teacher()



# # 6.Vehicle Management System (Hierarchical Inheritance)

# class Vehicle:
#     def start(self):
#         print("Vehicle is Starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has AC")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is Required")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Bus Capacity: 50 Passengers")


# c = Car()
# b = Bike()
# bs = Bus()

# print("Car Details")
# c.start()
# c.air_condition()

# print("\nBike Details")
# b.start()
# b.helmet_required()

# print("\nBus Details")
# bs.start()
# bs.passenger_capacity()


            

                        
