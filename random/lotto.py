def Texaslotto():
    import random
    integer = []
    for number in range(0 , 7):
        integer.append(random.randint(0, 100))
    return integer


print ('The Lucky Winning Numbers Are {}'. format(Texaslotto()))
print ('\nThank You for playing')

