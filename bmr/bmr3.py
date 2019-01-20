
# TODO: fix the issue with selecting type of person


typeCov = str(input("Please enter in K for kilos or P for pounds  "))
if typeCov == 'k':  # added an equal too
    typeCov = True
elif typeCov == "p":
    typeCov = False

else:
    print(" Error ,Please Enter(k/p)\n") # Add in case user enters an invalid value
    quit()

weight = int(input(" please enter in your weight in pounds or kilos: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line

height = int(input("enter in you height in inches: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line


age = int(input("enter in you age in years: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line
isMale = str(input("Are you male? (y/n)\n"))


if typeCov == "p":
    if typeCov == 'p':  # added an equal too
        typeCov = True
elif typeCov == "p":
    typeCove = False

if isMale == 'y':
    if isMale == 'y':  # added an equal too
        isMale = True
elif isMale == "n":
    isMale = False


# else:
#    print(" Error ,Please Enter(y/n)\n") # Add in case user enters an invalid value
#    quit()


if typeCov:
    bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)


else:

    bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)


if typeCov == "k":
    if typeCov == 'k':  # added an equal too
        typeCov = True
elif typeCov == "k":
    typeCove = False

if isMale == 'y':
    if isMale == 'y':  # added an equal too
        isMale = True
elif isMale == "n":
    isMale = False

# else:
#    print(" Error ,Please Enter(y/n)\n") # Add in case user enters an invalid value
#   quit()


if typeCov:
            bmr = 66 + (13.7 * weight) + (5 * height) - (4.7 * age)


else:

    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

# else
#(" Error ,Please Enter(y/n)\n") # Add in case user enters an invalid value
# quit()







bmr = round(bmr)
print(bmr)
