# Main file
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, empid, name, dept):
        print("__init__ of Employee")
        self.__empid = empid
        self.__name = name
        self.__dept = dept
    @abstractmethod
    def calculate_salary(self):
        pass
    def get_details(self):
        return {
            "Employee ID": self.__empid,
            "Name": self.__name,
            "Department": self.__dept
            }
      
class PermanentEmployee(Employee):
    def __init__(self, empid, name, dept, basic_salary, bonus):
        super().__init__(empid, name, dept)
        self.__basic_salary = basic_salary
        self.__bonus = bonus
        print("__init__ of PermanentEmployee")

    def calculate_salary(self):
        return self.__basic_salary + self.__bonus

    def display_details(self):
        print(self.get_details())
        print(f"Basic Salary of Permanent Employee: ${self.__basic_salary}")
        print(f"Bonus Of Permanent Employee : ${self.__bonus:.2f}")
        print(f"Total Salary of Permanent Employee: ${self.calculate_salary()}\n")
        
class ContractEmployee(Employee):
    def __init__(self, empid, name, dept, hour_rate, working_hours):
        super().__init__(empid, name, dept)
        self.__hour_rate = hour_rate
        self.__working_hours = working_hours
        print("__init__ of ContractEmployee")

    def calculate_salary(self):
        return self.__hour_rate * self.__working_hours

    def display_details(self):
        print(self.get_details())
        print(f"Hourly Rate for Contract Employee is : ${self.__hour_rate:.2f}")
        print(f"The Contract employee working Hours is  : {self.__working_hours}")
        print(f"Total Salary of Contract Employee is  ${self.calculate_salary():.2f}\n")
        
class Intern(Employee):
    def __init__(self, empid, name, dept, stipend):
        super().__init__(empid, name, dept)
        self.__stipend = stipend
        print("__init__ of Intern")

    def calculate_salary(self):
        return self.__stipend

    def display_details(self):
        print(self.get_details())
        print(f"Stipend of intern is: ${self.__stipend:.2f}")
        print(f"Total Salary is of intern is: ${self.calculate_salary():.2f}\n") 
        
per_emp = PermanentEmployee("101", "Amruta Bhosale", "IT", 50000, 4000)
per_emp.display_details()

cont_emp = ContractEmployee("181", "Aniket Kalamkar", "Finance", 60, 180)
cont_emp.display_details()

intern = Intern("208", "Prathamesh Patil", "Sales", 2000)  
intern.display_details()

