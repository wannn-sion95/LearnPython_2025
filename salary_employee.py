from abc import ABC, abstractmethod

class employee(ABC):
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

        @abstractmethod
        def calculate_salary(self):
            pass

class secretary(employee):
    def __init__(self, name, salary):
        super().__init__(name)
    

    def calculate_salary(self):
        return self.salary


emp1 = employee("Ridwan", "25.000.000")
emp2 = employee("Rayna", "15.000.000")

print(f"Salary of a HRD:\n\nName  : {emp1.name}\nSalary: Rp.{emp1.salary}\n\n")
print(f"Salary of a Secretary:\n\nName  : {emp2.name}\nSalary: Rp.{emp2.salary}")
