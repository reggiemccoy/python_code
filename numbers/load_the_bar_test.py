
b = int(input('Please enter weight to load on the bar: '))-int(input('Please enter bar weight : '))

print(int(b//45), "45's") if int(b//45)%2 == 0 else print(int(b//45)-1, "45's")

b = b%45

# //  Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# %   Divides and returns the value of the remainder.

x = b


print(b//25, "25's")
## print(int(b//25), "25's") if int(b//25)%2 == 0 else print(int(b//25)+1, "25's");
x =x-b

