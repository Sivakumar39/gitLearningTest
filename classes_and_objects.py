class Employee():
    def __init__(self, name:str='Sivakumar', age:int=27, gender:str="M", department:str="Data Engineering", 
    salary:int=90000, yoe:float=2.2):
        self.name = name
        self.age = age
        self.gender = gender
        self.department =  department
        self.salary =  salary
        self.yearsOfExperience = yoe

emp_Sivakumar =  Employee()

print(emp_Sivakumar.name)