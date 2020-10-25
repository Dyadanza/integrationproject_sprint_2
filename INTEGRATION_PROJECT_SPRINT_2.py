## Programmer: Derek Yadanza
## The main program is a automated golf caddie that keeps your score, totals it, and reports to you an accuracy percentage
print("*Left-Over numeric operators*")
print("Modulus Operator")
a = int(input("Type any number greater than, but not divisable by 10: "))
mod_op = a % 10

##The mod operator calculates the remainder of a division problem when it is not evenly divisable

print(mod_op)

print("Floor Division")
b = int(input("Type any number greater than but not divisable by 3: "))
floor_div = b // 3

##Floor division "//" will round the answer down to the nearest whole number if the number is not evenly divisable

print(floor_div)

print("Shortcut Operators")
number = 5
number += 2
print(number)
##The above operator "number += 2" is simply a short hand way of writing "number = number + 2"
##This method can be repeated for any of the numeric operators to create a shortcut operator
print("Range")
for num in range(10):
    print(num, end =" ")
print()
## The above lines will print all numbers in range "10" except for "10" itself

print("For")
for x in range(12, 20):
  print(x)
## Here we see "for" being used with "range" to print a single variable that represents all numbers from range 12 - 20

print("While")
num_x = 5
while num_x > 0:
    num_x -= 1
    print(num_x)
## The above loop continues to repeat the process of reducing the value of num_x by 1, WHILE it is greater than 0

print("In")
sports = ["golf", "tennis", "baseball"]
if "golf" in sports:
  print("yes")
else:
    print("No")
## The above lines search for items in a list, and prints a statement whether it is in the list or not


def main():
    while True:
        prompt_user()
def prompt_user():
#The above code wraps my program inside one function, this allows me to loop it based on user input at the end
    input("Press Enter if you would like to play a round of golf")
    print("Welcome to the Coded Caddie program, 3-Hole Edition!\nMy name is Codie, and I am your Coded Caddie!")

    ## \num_x creates a second line for the string of code, and is strictly for formatting purposes

    print("Before we get started, lets recall some of the rules of the golf course before you tee off.")
    print("If you happen to hit your ball into a hazard, that would entail a two stroke penalty.")
    hazard_pen = 2 ** 2

    ##above, we see the exponent operator "**" indicating that we are raising 2 to the second power

    print( "For instance if you hit your second stroke into the water, after taking a drop, you would then be hitting " + str(
        hazard_pen))

    hole_one_par = int(input("Please enter the par for hole one: "))

    ## In the line above "=" is the assignment operator, which is give value to the variable "hole_one_par"
    ## writing "int(input())" rather than just "input()" is specifying that the entry will be read as an integer

    print("For a par " + str(hole_one_par) + ", try to reach the green in " + str(hole_one_par - 2) + " strokes!")

    ## in the line above str() is used to convert the integer variable to a string, that way it can be concatanated using the "+" to another string operator

    strokes_to_green_1 = int(input("How many strokes did it take for you to reach the green?: "))
    if strokes_to_green_1 == hole_one_par:

        ## "==" is not the assignemnt operator, rather it is quite literally "equals"

        print("Not great, but we can save bogey with one putt!")
    elif strokes_to_green_1 == hole_one_par - 1:
        print("That's Good! One putt for par now!")
    elif strokes_to_green_1 == hole_one_par - 2:
        print("Nice! \nLets go for that birdie, but make sure you leave an easy putt for par if you miss!")
    elif strokes_to_green_1 == hole_one_par - 3 and hole_one_par != 3:

        ##In the above line, the operatore "!=" is specifying "does not equal"
        ## "if/elif" is used in the lines above and below to create a condition statement with varying outputs depending on the inputs
        ## "and" is also used as a conditional statement implying that it must also satisfy a second standard

        print("Amazing! You have a lot of putts to work with now, lets make an eagle!")
    if strokes_to_green_1 <= hole_one_par - 2:
        reg_1 = 1
    else:
        reg_1 = 0
    hole_one_putts = int(input("How many putts did you take?: "))
    if strokes_to_green_1 == 1 and hole_one_putts == 0:
        print("WOW! A Hole-In-One" + "!" * 5 + " Drinks are on you!")

    ## The string operator "*" multiplies "!" five times in the output

    score_1 = strokes_to_green_1 + hole_one_putts

    ## In the line above, instead of concatanating two strings, I am mathematically adding two integers in the form of variables

    print("You scored a " + str(score_1) + " on hole one!")

    hole_two_par = int(input("Please enter the par for hole two: "))
    print("For a par " + str(hole_two_par) + ", try to reach the green in " + str(hole_two_par - 2) + " strokes!")
    strokes_to_green_two = int(input("How many strokes did it take for you to reach the green?: "))
    if strokes_to_green_two == hole_two_par:
        print("Not great, but we can save bogey with one putt!")
    elif strokes_to_green_two == hole_two_par - 1:
        print("That's Good! One putt for par now!")
    elif strokes_to_green_two == hole_two_par - 2:
        print("Nice! \nLets go for that birdie, but make sure you leave an easy putt for par if you miss!")
    elif strokes_to_green_two == hole_two_par - 3 and hole_two_par != 3:
        print("Amazing! You have a lot of putts to work with now, lets make an eagle!")
    if strokes_to_green_two <= hole_two_par - 2:
        reg_2 = 1
    else:
        reg_2 = 0
    hole_two_putts = int(input("How many putts did you take? :"))
    if strokes_to_green_two == 1 and hole_two_putts == 0:
        print("WOW! A Hole-In-One! Drinks are on you!")
    score_2 = strokes_to_green_two + hole_two_putts
    print("You scored a " + str(score_2) + " on hole two!")
    combined_1_2 = score_1 + score_2
    print("Your score through two holes is " + str(combined_1_2))

    hole_three_par = int(input("Please enter the par for hole three: "))
    print("For a par " + str(hole_three_par) + ", try to reach the green in " + str(hole_three_par - 2) + " strokes!")
    strokes_to_green_three = int(input("How many strokes did it take for you to reach the green?: "))
    if strokes_to_green_three == hole_three_par:
        print("Not great, but we can save bogey with one putt!")
    elif strokes_to_green_three == hole_three_par - 1:
        print("That's Good! One putt for par now!")
    elif strokes_to_green_three == hole_three_par - 2:
        print("Nice! \nLets go for that birdie, but make sure you leave an easy putt for par if you miss!")
    elif strokes_to_green_three == hole_three_par - 3 and hole_three_par != 3:
        print("Amazing! You have a lot of putts to work with now, lets make an eagle!")
    if strokes_to_green_three <= hole_three_par - 2:
        reg_3 = 1
    else:
        reg_3 = 0
    hole_three_putts = int(input("How many putts did you take? :"))
    if strokes_to_green_three == 1 and hole_three_putts == 0:
        print("WOW! A Hole-In-One! Drinks are on you!")
    score_3 = strokes_to_green_three + hole_three_putts
    print("You scored a " + str(score_3) + " on hole three!")
    combined_1_3 = combined_1_2 + score_3

    print("Your total score is " + str(combined_1_3) + ",")
    reg_total = reg_1 + reg_2 + reg_3
    reg_percent = reg_total / 3 * 100

    ## above we see the division operator "/" and the multiplication operator "*" both being used to calculate percent

    print("and your greens in regulation percentage was " + str(format(reg_percent, '.2f')) + "%")
        ## in the line above "format(,'.2f') is used to format the reg_percent result to be rounded to 2 decimal places
    print("Thank you for playing!")

if __name__ == '__main__': main()

##The above code calls back to my main function, which allows the user to repeat the program as often as they want

