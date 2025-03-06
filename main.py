class Person():
    moods=['Happy','Lazy','tired']
    healthRates=[100,75,50]
    def __init__(self,name, money):
        self.name=name
        self.money=money
        self.__mood=self.moods[0]
        self.__healthRate=self.healthRates[0]

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, new_mood):
        if new_mood in self.moods:
            self.__mood = new_mood
        else:
            print("Invalid mood! Choose from:", self.moods)

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, new_health):
        if new_health in self.healthRates:
            self.__healthRate = new_health
        else:
            print("Invalid health rate! Choose from:", self.healthRates)
    def sleep(self,hours):
        if hours>7:
            self.__mood=Person.moods[1]
        elif hours<7:
            self.__mood=Person.moods[2]
        else:
            self.__mood=Person.moods[0]
        return self.__mood

    def eat(self,meals):
        if meals ==1:
            self.__healthRate = Person.healthRates[2]
        elif meals ==2:
            self.__healthRate = Person.healthRates[1]
        else:
            self.__healthRate = Person.healthRates[0]
        return self.__healthRate
    def buy(self,items):
        if items==1:
            self.money=self.money-10
        return self.money

###################
person1 = Person("Ali", 100)
print(person1.sleep(8))
print(person1.eat(2))
print(person1.buy(3))
person1.mood = "Excited"
person1.healthRate = 200
person1.mood = "Happy"
print(f"New mood: {person1.mood}")

#######################################################################
class Employee(Person):

    def __init__(self,id ,name,money, car, salary, distanceToWork):
        super().__init__(name,money)
        self.id=id
        self.car=car
        self.__salary=salary
        self.distanceToWork=distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary  >= 1000:
            self.__salary=new_salary
        else:
            print("salary should be greater than 1000")
    def work(self,hours):
        if hours > 8:
            self.mood = self.moods[1]
        elif hours < 8:
            self.mood = self.moods[3]
        else:
            self.mood = self.moods[0]
        return self.mood

    def drive(self, distance):
        if self.car:
            return self.car.run(60, distance)
        else:
            return "No car assigned!"
    def refuel(self, gasAmount=100):
        if self.car:
            return self.car.refuel(gasAmount)
        else:
            return "No car assigned!"


emp1 = Employee('ali',101,300, None, 5000, 20)

print(emp1.work(9))
print(emp1.refuel(50))
##################################################################
class Car:
    def __init__(self, brand, model, fuelRate, velocity):
        self.brand = brand
        self.model = model
        self.__fuelRate = fuelRate
        self.__velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self.__fuelRate = value
        else:
            print("Fuel rate must be between 0 and 100.")

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self.__velocity = value
        else:
            print("Velocity must be between 0 and 200.")

    def run(self, velocity, distance):
        if self.fuelRate <= 0:
            return "Can't start! No fuel."

        self.velocity = velocity
        print(f"Car started moving at {self.velocity} ")

        fuel_needed = distance * 0.2
        if fuel_needed > self.fuelRate:
            remaining_distance = (self.fuelRate / 0.2)
            self.fuelRate = 0
            return self.stop(remaining_distance)

        self.fuelRate -= fuel_needed
        return self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            return f"Car stopped! Need refuel. {remaining_distance:.2f} km left to destination."
        return "Car stopped! You have arrived at your destination."

    def refuel(self, gasAmount):
        if self.fuelRate + gasAmount > 100:
            self.fuelRate = 100
        else:
            self.fuelRate += gasAmount
        return f"Fuel refilled! Current fuel: {self.fuelRate}%."

car1 = Car("Toyota", "Corolla", 50, 0)

print(car1.run(80, 100))
print(car1.refuel(30))
print(car1.run(60, 50))
###################################################################
class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.currentEmployees = []

    def get_all_employees(self):
        return self.currentEmployees

    def get_employee(self, empId):
        for emp in self.currentEmployees:
            if emp.id == empId:
                return emp
        return "Employee not found!"

    def hire(self, employee):
        self.currentEmployees.append(employee)
        Office.employeesNum += 1
        return f"Employee {employee.name} hired successfully!"

    def fire(self, empId):
        for emp in self.currentEmployees:
            if emp.id == empId:
                self.currentEmployees.remove(emp)
                Office.employeesNum -= 1
                return f"Employee {emp.name} has been fired."
        return "Employee not found!"

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if isinstance(emp, Employee):
            emp.salary -= deduction
            return f"{deduction} deducted from {emp.name} salary."
        return emp

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if isinstance(emp, Employee):
            emp.salary += reward
            return f"{reward} added to {emp.name} salary."
        return emp

    def check_lateness(self, empId, moveHour, targetHour=9):
        emp = self.get_employee(empId)
        if isinstance(emp, Employee):
            if Office.calculate_lateness(targetHour, moveHour, emp.distanceToWork,emp.car.velocity):
                return self.deduct(empId, 10)
            return self.reward(empId, 10)
        return emp

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):

        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
        return f"Employees number updated to {cls.employeesNum}."



car1 = Car("Toyota", "Corolla", 50, 100)
emp1 = Employee(1, "Ahmed",200, 5000, car1, 30)
emp2 = Employee(2, "Sara",200, 6000, car1, 20)

office = Office("TechCorp")

print(office.hire(emp1))
print(office.hire(emp2))
print(office.get_all_employees())
# print(office.check_lateness(1, 7))
# print(office.check_lateness(2, 8))
print(office.fire(1))
print(office.get_all_employees())

#######################################################################

