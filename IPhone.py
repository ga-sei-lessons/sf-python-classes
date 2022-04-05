# python imports
# from file import funciton/class/thing
# from file import *
# from folder.file import Class
# file.thing 
from Phone import Phone

# inheritance in python
class IPhone(Phone): # like the extends keyword
  def __init__(self, phone_number, gen, color):
    # Polymorphim in python
    super().__init__(phone_number)
    self.gen = gen
    self.color = color

  def __str__(self):
    return f'number: {self.phone_number} gen: {self.gen} color: {self.color}'
  
  # this is only in IPhones
  def upgrade(self, new_gen):
    """
      takes phone apple store and gets the next gen
    """
    self.gen = new_gen
  

my_iphone = IPhone('666-666-6666', '6', 'gold')
print(my_iphone)
jasons_phone = Phone('333-333-3333')
# Polymorphism in action
my_iphone.text(jasons_phone.phone_number, 'how are you liking the new jitterbug?')
my_iphone.upgrade('7')
print(my_iphone)

