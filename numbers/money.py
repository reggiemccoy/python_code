c=int(input('Please enter an amount between 0-99:'))
print(c//25, "quarters")
c = c%25
# //  Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# %   Divides and returns the value of the remainder.


print(c//10, "dimes")
c = c%10
print(c//5, "nickles")
c = c%5
print(c//1, "pennies")