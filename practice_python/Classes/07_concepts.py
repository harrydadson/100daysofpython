class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    def bark(self):
        return "arf arf!"

class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "arruff!"

class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def shedding_amt(self):
        return 0

class GoldenRetrieve(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fetch_able(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7

class GoldenDoodle(Poodle, GoldenRetrieve):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "aroooo!"

sammy = Samoyed("Sammy", 2, 10)
goldie = GoldenDoodle("Goldie", 1, 10)
generic_dogo = Dog("Gene", 10, 10)
print(goldie.shedding_amt())
print(goldie.fetch_able())
print(sammy.bark())
print(goldie.bark())
print(generic_dogo.bark())

