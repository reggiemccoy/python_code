

weight = int(input(" please enter in your weight in pounds: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line

height = int(input("enter in you height in inches: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line


age = int(input("enter in you age in years: \n"))  # making sure the data entered is integer
#  and then make the text appear on a new line
isMale = str(input("Are you male? (y/n)\n"))

if isMale == 'y':  # added an equal too
    isMale = True
elif isMale == "n":
    isMale = False

else:
    print(" Error ,Please Enter(y/n)\n") # Add in case user enters an invalid value
    quit()


if isMale:
    bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)


else:

    bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

bmr = round(bmr)
print(bmr)
