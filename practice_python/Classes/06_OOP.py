class Robot:
    def __init__(self,Name, Color, Weight):
        self.Name = Name
        self.Color = Color
        self.Weight = Weight

    def introduce_self(self):
        print(f"My name is {self.Name}")

class Person:
    def __init__(self,n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "Blue", 40)

p1 = Person("Alice", "aggressive", False)
p2 = Person("Bob", "Talkertive", True)

#p1 owns r2, p2 owns r1
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()



