class Employee:
    emp_id=input("emp_id:")
    emp_name=input("emp_name:")
    emp_salary=float(input("emp_salary"))
    emp_department=input("emp_department:")
    def calculate_emp_salary(self,emp_salary,hours_worked):
        self.hours_worked=int(input())
        if(self.hours_worked>50):
            self.overtime=self.hours_worked-50
            self.overtime_amount=overtime*(emp_salary/50)
            print("overtime amount is",overtime_amount)
    def emp_details(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_salary)
        print(self.emp_department)
obj=Employee()
obj.emp_details()
obj.calculate_emp_salary(emp_salary,hours_worked)