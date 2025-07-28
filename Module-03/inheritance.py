#dad  mr.object
#daughter   multi clever
#mother       mrs. classy
#son   naughty eno


#single inheritance
class Father:
    def skills(self):
        
        print("I can code in cpp")
        
class Son(Father):
    pass

inno=Son()
inno.skills()

#heirarchical inrehitance
class Mom:
    def cooking(self):
        print("I can cook delicious Biriyani")
        
        
class Inno(Mom):
    pass
class Multi(Mom):
    pass


inno=Inno()
multi=Multi()

inno.cooking()
multi.cooking()

# multilevel inheritance
class Grandpa:
    def advice(self):
        print("Never ignore bugs")
        
        
class Father(Grandpa):
    def tech(self):
        print("Practice cpp will make you more logical")
        
        
class Son(Father):
    pass

multi=Son()
multi.advice()
multi.tech()

# multiple inheritance
class Mother():
    def descipline(self):
        print("Go to bed at 10 pm")
        
class Unclelogic():
    def math(self):
        print("solving equation")
        
        
class Daughter(Mother,Unclelogic):
    pass

multi=Daughter()
multi.descipline()
multi.math()


# method overloading(we can pass single value or multiple value)
class ReportCard:
    def marks(self,math=None,english=None):
        if math is not None and english is not None:
            print(f"Math: {math},English: {english}")
        elif math is not None:
            print(f"Math :{math}")
        else:
            print("No mark given")
            
inno_report=ReportCard()
inno_report.marks()
inno_report.marks(90)
inno_report.marks(98,99)


# overriding

class Parent:
    def role(self):
        print("I am the boss")
        
class Child(Parent):
    def role(self):
        print("I run the show now")

multi=Child()
multi.role()

parent_obj1=Parent()
parent_obj1.role()


# encapsulation

class Family:
    def __init__(self):
        self.__secret_fund=500   #private
        
    def get_fund(self):
        return self.__secret_fund
    
    
dad=Family()
print(dad.get_fund())

# polimorphism

class Role:
    def act(self):
        pass
    
class Cook(Role):
    def act(self):
        print("cooking dinner")
        
class Doctor(Role):
    def act(self):
        print("Prescribing Medicine")
        
        
def daily_roles(role):
    role.act()
    
    
daily_roles(Cook())
daily_roles(Doctor())
    
