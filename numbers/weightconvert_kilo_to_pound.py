# The following program converts  pounds to kilos and kilos to pounds




def  metricTopound(kilograms):

    pounds = kilograms * 2.2
    ounces = pounds * 16

    return int(pounds), ounces % 16

kilograms = float(input("How many Kilos ? "))
lb, o = metricTopound(kilograms)
print('The amount of pounds you entered is {}. '\
      'This is {} pounds and {} ounces.'.format(kilograms, lb, o))



