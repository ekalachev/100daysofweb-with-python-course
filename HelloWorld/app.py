import utils

numbers = [1, 2, 4, 5, 2, 10, 2, 2, 6, 7, 2, 7]

# numbers_set = set()
#
# for number in numbers:
#     numbers_set.add(number)
#
# print(numbers_set)

# --------------------------

# numbers_dict = dict()
#
# for number in numbers:
#     if number in numbers_dict:
#         count = numbers_dict.get(number) + 1
#         numbers_dict[number] = count
#     else:
#         numbers_dict[number] = 1
#
# print(numbers_dict)

# --------------------------


# class Array:
#     @staticmethod
#     def remove_duplicates(numbers_in):
#         numbers_set = set()
#         for number in numbers_in:
#             numbers_set.add(number)
#
#         return numbers_set
#
#
# array = Array()
# print(array.remove_duplicates(numbers))

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hello! My name is {self.name}")
#
#
# person = Person("David")
# person.talk()

# -----------------------

maximum = utils.find_max(numbers)
print(maximum)
