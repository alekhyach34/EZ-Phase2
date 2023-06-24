class Employee:
    def __init__(self):
        self.emp_id=input("emp_id:")
        self.emp_name=input("emp_name:")
        self.emp_salary=float(input("emp_salary"))
        self.emp_department=input("emp_department:")
    def calculate_emp_salary(self):
        hours_worked=int(input())
        if(hours_worked>50):
            overtime=hours_worked-50
            overtime_amount=overtime*(self.emp_salary//50)
            self.emp_salary+=overtime_amount
            print(self.emp_salary)
        else:
            print(self.emp_salary)
    def emp_details(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_salary)
        print(self.emp_department)
obj=Employee()
obj.calculate_emp_salary()
obj.emp_details()