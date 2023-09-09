class Person:
    def __init__(self , name , age):
    
        self.name = name
        self.age  = age 

    def is_adult(self):
        if self.age >18:
            print("You have too much responsibilities")
         
        else:
            print("Lucky you")
         
    

first_person=Person("manal" , 22)
print(first_person.name)
print(first_person.age)
first_person.is_adult()    

class Person2:
    def __init__ (self,name,age):
        self.name = name
        self.age = age  
    def __str__(self):
        return f"my name is{self.name}, and i am {self.age} years old"
    
#secondperson =Person2(name, age)

