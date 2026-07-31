
# 1. Simple class with a method and a property
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"Playing {self.title} by {self.artist}")

track = Song('Ocean', 'Mia')
track.play()  # create an object and call a method

# 2. Inheritance with a child class
class Animal:
    def speak(self):
        return 'sound'

class Dog(Animal):
    def speak(self):
        return 'bark'

pet = Dog()
print(pet.speak())  # Dog reuses Animal and changes speak behavior

# 3. Class with a class method
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def total(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print(Counter.total())  # class state shared across instances

# 4. Using properties to control access
class BankAccount:
    def __init__(self, owner, amount):
        self.owner = owner
        self._balance = amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

account = BankAccount('Dana', 100)
account.balance = 120
print(account.balance)  # property uses getter and setter


