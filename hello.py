from ast import operator
from distutils.command.build_scripts import first_line_re
import os
import namer_module
os.system('cls')

# first_name = ["John", "bob", "tina"]

# fav_pizza = {
#     "john": "pepperoni",
#     "bob": "cheese"
# }

# # print (first_name[0])
# print (fav_pizza["bob"])

# talking = "my mom yelled \n'clean your room'"
# print (talking)

my_name = "dallin johnson is my name"

# print (my_name.swapcase())
# print (my_name[1])
# print (my_name.split(' '))
# print (my_name.split(' ')[3].upper())
# print (2%3)
# z = 1
# v = 2
# print (z+v)


# z = 10.1
# v = 3
# print (round(z / 3))

# assignment operators

# num = 41

# num+=1
# num = num+1

# print (num)



# lists

# num = [1,2,3,4,5]

# first_names = ['john', "bob"]
# first_names[0] = 'tina'
# # print (first_names[0][1])
# # print (first_names[len(first_names)-1])  #last in the list

# tup = ('john', 'bob', 'mary')
# tup2 = ('tina', )
# # tup3 = tup + tup2
# tup3 = tup[0:2] + tup2

# # print (tup3[0:3])
# print (tup3[0:3])


# objects

# fav = {
#     'john': 'peperoni',
#     'bob': "mushroom",
#     "tina": "sup"
# }

# fav.update({'tim': "green peppers"})

# print (fav)


# compairisons 

# first_name = "john"

# # print (9 != 10)
# print (first_name = "john")


# conditionals 

# num = 3
# if (num > 10):
#     print ("your number is greater than 10")
# elif (num == 3):
#     print('your number is 3')
# else:
#     print ("your number is not greater than 10")

# multiple conditionals 

# num = 3
# if (num > 10) or (num < 100):
#     print ("your number is greater than 10 and less than 100")

# # while loops

# counter = 0

# while (counter < 10):
#     print ("the count is : %s" % counter)
#     counter += 1


# # for loop

# name = ["john", "bob", "tina"]

# fav = {
#     "john": "pep",
#     "bob": "mushroom",
#     "tina": 'sup'
# }

# for x in name:
#     print(x)


# # fizzbuzz

# i = 1

# while (i <= 100):
#     if(i % 15 == 0):
#         print ("fizzbuzz")
#     elif(i % 5 == 0):
#         print ('fizz')
#     elif(i % 3 == 0):
#         print ('buzz')
#     else:
#         print(i)
#     i += 1


# # functions 

# def theFunc(num1, num2):
#     print (num1 + num2)

# theFunc(4, 5)

# # functuons 2

# def namer(name):
#     return ("hello %s" % name)

# my_name = namer('john')
# for letter in my_name: 
#     print(letter)

# # importing

# print(namer_module.namer('bob').upper())


# # classes


# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         area = self.side_length * self.side_length
#         return ("area: %s" % area)
#     def perimeter(self):
#         perimeter = self.side_length * 4
#         return "the perimeter is %s" % perimeter
#     def report(self):
#         print ("side length: %s" % self.side_length)
#         print ("area: %s" % self.area())
#         print ("perimeter: %s" % self.perimeter())


# my_square = Square(10)
# print(my_square.side_length)
# print(my_square.area())
# print(my_square.perimeter())
# my_square.report()


person