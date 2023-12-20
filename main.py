# import another_module
# print(another_module.another_variable)
#


# from turtle import Turtle, Screen
# sammy = Turtle()
# print(sammy)
# sammy.shape("turtle")
# sammy.color("cyan4")
# sammy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.align = "r"
print(table)
