# #class
# class Avanger:
#     def fight(self):
#         print("Avangers start fighting")

#  #object
# ironman=Avanger() 
# hulk=Avanger()

# ironman.fight()
# hulk.fight()

#introdusing method
#class
# class Avanger:
#     def introduce(self,name):
#         print(f"I am {name} and i protect the world")

#  #object
# ironman=Avanger()
# thor=Avanger()
# ironman.introduce("Tony")
# thor.introduce("Thor")



#default constructor
# class Averger:
#     def __init__(this):
#         print("A new avenger join in this team")
# captain=Averger()


#parameterized constructor
class Avanger:
    def __init__(self,name,power):
         self.name=name
         self.power=power
    
    def show(self):
        print(f"{self.name} has power: {self.power}")
spiderman=Avanger("spiderman","web-sliging")
spiderman.show()