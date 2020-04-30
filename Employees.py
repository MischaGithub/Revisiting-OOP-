
class Employee:
    emp_Count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_Count += 1

    def display_Count(self):
        print("Total Employee %d" % Employee.emp_Count)

    def display_Employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
employee_1 = Employee("Zara", 2000)
"This would create second object of Employee class"
employee_2 = Employee("Manni", 5000)


employee_1.display_Employee()
employee_2.display_Employee()
print("Total Employee %d" % Employee.emp_Count)