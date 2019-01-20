
# The following program calculates lean body mass

weight = int(input("Enter in your weight KG: \n"))
height = int(input("Enter in your height in CM: \n"))
age = int(input("Enter in your age in Years \n"))
isMale = str(input("Are you male ?(y/n)"))

if isMale == "y":
    isMale = True
elif isMale == "n":
    isMale = False
else:
    print("Error")
    quit()

if isMale:
        bmr = 66.5 + (13.75 * weight)+(5* height)-(6.755* age)
else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)


bmr = round(bmr)

Cal = str('calories')


print (bmr ,Cal)