# important Object Oriented Programming Words
# Abstraction -- turn code into an object factory
from crypt import methods


def make_cup():
  # Encapsulation -- grouping data and methods that manipulate the data together  
  this = {}
  this['capacity'] = 10
  this['amount'] = 0

  def drink(this):
    this['amount'] = this['amount'] - 1

  this['drink'] = drink

  return this

# abstraction allows us to make many coffee cups
# red_cup = make_cup()
# print(red_cup)
# blue_cup = make_cup()
def tea_cup():
  # inheritance -- props and methods from parent
  this = make_cup()
  this['tea_type'] = 'green'
  # ...tea methods

my_tea = tea_cup()

# Polymorphism is drinking with the parents method to drink
my_tea['drink']()


# Inheritance -- all the props and methods of a class can be given to a child class
# Polymorphism -- all of the parents properties and methods will work perfectly with the child class

# Our digital coffee cup

# this is the constructor since it is the data
# capacirty -- how much the cup can hold
# amount -- current amount of coffee

capacity = 10
amount = 0

# these are the class methods 'instance methods' 'dot methds'
# we will be ab le to flle the cup with coffee
# drink from the cup
# empty the cup to dump out the coffee

def drink():
  amount - 2

# ...

# class Test:
#   pass

# print(Test.__init__)

# create a class with the class keyword -- PascalCase the name
class CoffeeCup():
  # class constructor
  # method override on the __init__(ref to instance (self), ...props) method
  def __init__(self, capacity):
    self.capacity = capacity
    self.amount = 0

  # method override string representation
  def __str__(self):
    # what ever string we return will be shown when an instance is printed
    return f'capacity: {self.capacity} amount: {self.amount}'

  # instance methods
  def fill(self):
    # cup is always filled to the brim
    self.amount = self.capacity
  
  def drink(self, drink_size):
    # remove size of drink from amount in cup
    self.amount -= drink_size
    # if self.amount < 0:
    #   self.amount = 0
    # [value is true] if [condition] else [value if false]
    self.amount = 0 if self.amount < 0 else self.amount 

# making an instance of the class
# props defined in the __init__ params are passed
jasons_cup = CoffeeCup(15)
westons_cup = CoffeeCup(10)

jasons_cup.fill()
jasons_cup.drink(10)
jasons_cup.drink(10)
print(jasons_cup)