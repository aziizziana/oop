class Pet(object):
 def __init__(self, name, age):
     self.name = name
     self.age = age

dog = Pet("Tom", 6)
print(dog.name + " is " + str(dog.age))

dog1 = Pet("Fletcher", 7)
print(dog1.name + " is " + str(dog1.age))

dog2 = Pet("Larry", 9)
print(dog2.name + " is " + str(dog2.age))
print("And they're all mammals ofcourse")

  