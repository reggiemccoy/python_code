b=int(input('Please enter weight to load on the bar: '))
bartype=int(input('Please enter bar weight '))
x = bartype
b = (b-x)
print(b//45, "45's")
b = b%45
print(b//25, "25's")
b = b%25
print(b//10, "10's")
b = b%10
# I need to print 2.5 without leading zeros
print(int(b/2.5), "2.5's")
b = b%2.5

print(b//5, "5's")
b = b%5