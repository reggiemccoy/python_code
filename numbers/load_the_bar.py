b = int(input('Please enter weight to load on the bar: '))
bartype = int(input('Please enter bar weight: '))

b = (b - bartype)


print(b//45, "45's")
b = b%45
# //  Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# %   Divides and returns the value of the remainder.

print(b//25, "25's")
b = b%25
print(b//10, "10's")
b = b%10

print(b//5, "5's")
b = b%5

print(int(b/2.5), "2.5's")
b = b%2.5

