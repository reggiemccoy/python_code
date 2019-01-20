# The following program displays the President by number

person = int(input('Enter President number :'))

if person == 45:
    print('Donald Trump')

elif person == 44:
    print('Barack Obama')

elif person == 43:
    print('George Bush')

elif person == 42:
    print('Bill Clinton')

elif person == 41:
    print('George Bush')


elif person <= 0:
    print('Error please enter in a validate number')

elif person > 45:
    print('Will 45 be the last US President before the Global Leader ?')

elif person <= 41:
    print('This program only displays the last few Presidents.')
    print(' Please try again ')

