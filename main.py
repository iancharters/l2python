# class DogFood:
#     def __init__(self, food="kibble"):
#         self.food = food

#     def describe_food(self):
#         print(self.food)


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.food = DogFood()

#     def sit(self):
#         print(self.name.title() + " is now sitting.")

#     def roll_over(self):
#         print(self.name.title() + " rolled over!")


# class ShowDog(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def laser_eyes(self):
#         print(self.name.title() + " shoots laser beams out of his eyes.")


# myDog = Dog("Gus", 10)

# print(myDog.__dict__)

# myShowDog = ShowDog("Gary", 1000)

# myShowDog.laser_eyes()
# myShowDog.roll_over()
# myShowDog.food.describe_food()

try:
    print(5 / 0)
except ZeroDivisionError as lol:
    print(lol)
    print("lol")
