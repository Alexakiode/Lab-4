#Creating the Superclass Person
class Person:
    #Defining the initialisation attributes
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
#Defining the profile information and giving it a return statement
    def get_profile_info(self):
        return "Name: %s, Phone number: %s" %(self.name, self.phone_number)

#Creating the subclass Student and passing the Superclass Person
#To be able to use the attributes
class Student(Person):
    #Defining the init function with Student attribute, args and kwargs attributes
    def __init__(self, course, *args, **kwargs):
        self.course = course
        self.classes = []
        #Import method to import attributes from Superclass using super().__init__
        super().__init__(*args, **kwargs)
        
#Defining the enrol function
    def enrol(self, module):
        self.classes.append(module)

#Creating the Staff member subclass with the Superclass Person
#To be able to use the attributes
class StaffMember(Person):

    #Defining the init attributes for Staff member and the attributes
    def __init__(self, *args, **kwargs ):
        self.courses = []
        super().__init__(*args, **kwargs)

#Defining the Staff admin portfolio and the attributes
    def administrator_for(self, module):
        self.module = module
        self.courses.append(course)
        
#Defining the salary and the attribute
    def get_salary(self):
        return self.salary
    
    #Creating the class Lecturer with Superclass person 
class Lecturer(Person):
    #Defining the init method, including the 
    #title and salary attributes as required
    def __init__(self, title, salary, *args, **kwargs):
       self.title = title
       self.salary = salary
       #Using the superclass init function to acquire 
       #information from Person 
       
       super().__init__(*args, **kwargs)
       
       #Defining the title and salary functions       
    def academic_title(self,title):
        self.title = title
        
    def get_salary(self, salary):
        self.salary = salary
 
#Creating an instance of the subclass Lecturer
#lecturer1 = Lecturer("Shagy", "0744", "Dr", "60000")

#Creating an instance of the subclass Lecturer interpolating it
lecturer1 = Lecturer("Dr", "60000", "Shagy", "0744")

#Calling the result with a print function
print(lecturer1.name,lecturer1.phone_number,lecturer1.title, lecturer1.salary)
