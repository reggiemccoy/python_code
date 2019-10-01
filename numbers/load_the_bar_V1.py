
b = int(input('Please enter weight to load on the bar: '))-int(input('Please enter bar weight : '))

print(int(b//45), "45's") if int(b//45)%2 == 0 else print(int(b//45)-1, "45's")

a = b  # The following prints the total amount of weight without the bar
print("Bar weight : " + str(a))
b = b%45


# //  Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# %   Divides and returns the value of the remainder.

# x = b





