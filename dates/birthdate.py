
# The date must be entered in this format:
# YYYY-MM-DD
#


import datetime
import calendar

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get the birth date
birthday = input("Enter your date of birth in format YYYY-MM-DD:\n")

if not birthday:
    print("You did not enter a birthday. Lets set it to 2000-01-01 in order to be able to go on...\n")
    birthday = "2000-01-01"

try:
    # Split it to year, month and day
    year, month, day = birthday.split('-')

    # Get a date object for the day of birth
    bdate = datetime.datetime(int(year), int(month), int(day), 0, 0, 0, 0)

    # Get the integer weekday for the day of birth
    weekday = bdate.weekday()

    # Tell the user
    print("\nIt was a", weekdays[weekday], "!\n\n")

    # Print ASCII calendar for the month/year of birth
    print(calendar.month(bdate.year, bdate.month))

except:
    # Some invalid date was received from the user
    print(
        "\nInvalid date or date format incorrect. Try again and make sure you enter a valid date in format: YYYY-MM-DD")