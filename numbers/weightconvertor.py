# The following script converts units of weight

def metricTopound(kilograms):
    pounds = kilograms * 2.2
    ounces = pounds * 16

    return int(pounds), ounces % 16


def poundsToMetric(pounds):
    kilograms = pounds / 2.2
    grams = kilograms * 1000

    return int(kilograms), grams % 1000


weight = input('Enter K for kilos  or P for pounds : ')

unit = weight
unit = unit.upper()  # The following converts lowercase to uppercase

if unit == "K":
    kilograms = float(input("How many Kilos ? "))
    lb, o = metricTopound(kilograms)
    print("The amount of pounds you entered is {}. " \
        "This is {} pounds and {}ounces.".format(kilograms, lb, o))

elif unit == "P":
    pounds = float(input("How many Pounds? "))
    kg, g = poundsToMetric(pounds)
    print("The amount of pounds you entered is {}. " \
          "This is {} kilograms and {} grams.".format(pounds, kg, g))

elif unit != "P" or "K":
    print("Sorry, that was an invalid option!: " + str(unit) + " \"Please only enter P or K:\"")


