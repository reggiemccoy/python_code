

b = int(input('Please enter weight to load on the bar: '))-int(input('Please enter bar weight : '))

print(int(b//45), "45's") if int(b//45)%2 == 0 else print(int(b//45)-1, "45's");

b = b%45
# //  Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# %   Divides and returns the value of the remainder.

print(b//25, "25's")
# print(int(b//25), "25's") if int(b//25)%2 == 0 else print(int(b//25)+1, "25's");
b = b%25

print(b//10, "10's")
# print(int(b//10), "10's")
b = b%10

print(b//5, "5's")
# print(int(b//5), "5's")
b = b%5

print(int(b/2.5), "2.5's")
b = b%2.5

# Currently working on a bug where the program works with  405 but fails with 365