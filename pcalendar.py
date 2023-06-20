# Exercise: Perpetual Calendar

# Description: This program recieves an input from the user of the day, month, and year that they would 
# like to know information about and tells the user what day of the year it would be, what day of the week 
# the date would be, what day of the week the date would be in 2020, what day of the week New Year's Day would 
# be, and what day of November Thanksgiving would be.

# This function determines if the year is a leap year.
# Parameters: year, an int representing the year tested
# Returns: True if the year is a leap year otherwise, it returns False
def is_leap(year):
    if ((year % 4) == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# This function returns the day of the year the first day of the month would be.
# Parameters: month, an int representing the month tested
# Returns: the day of the year of the first of the month inputed.
def magic_month(month):
    if month == 1:
        return 0
    elif month == 2:
        return 31
    elif month == 3:
        return 59
    elif month == 4:
        return 90
    elif month == 5:
        return 120
    elif month == 6:
        return 151
    elif month == 7:
        return 181
    elif month == 8:
        return 212
    elif month == 9:
        return 243
    elif month == 10:
        return 273
    elif month == 11:
        return 304
    else:
        return 334

# This function determines the day of the year for the date inputed.
# Parameters: month, an int representing the month tested; day, an int representing the day tested;
#             year, an int representing the year tested
# Returns: day_year, an int representing the day of the year    
def day_of_year(month, day, year):
    day_year = magic_month(month) + day
    if (month > 2) and is_leap(year) == True:
        day_year += 1
    return day_year

# This function determines the day of the week that New Year's Day lands on for the specified year.
# Parameters: year, an int representing the year tested
# Returns: the day of the week that New Year's Day lands on in integer form   
def new_years_day(year):
    total = year + (year // 4) - (year // 100) + (year // 400)
    if is_leap(year) == True:
        total -= 1
    return (total % 7) 

# This function determines the day of the week for the date inputed.
# Parameters: month, an int representing the month tested; day, an int representing the day tested;
#             year, an int representing the year tested
# Returns: the day of the week for the specified date in integer form   
def day_of_week(month, day, year):
    return ((day_of_year(month, day, year) + new_years_day(year) - 1) % 7)

# This function translates the day of the week into a string format.
# Parameters: month, an int representing the month tested; day, an int representing the day tested;
#             year, an int representing the year tested
# Returns: the day of the week for the specified date in string form
def day_of_week_str(month, day, year):
    number = day_of_week(month, day, year)
    if number == 0:
        return 'Sunday'
    elif number == 1:
        return 'Monday'
    elif number == 2:
        return 'Tuesday'
    elif number == 3:
        return 'Wednesday'
    elif number == 4:
        return 'Thursday'
    elif number == 5:
        return 'Friday'
    else:
        return 'Saturday'

# This function determines which day of November Thanksgiving would land on for the specified year.
# Parameters: year, an int representing the year tested
# Returns: the day that Thanksgiving would land on for the specified year.
def find_thanksgiving(year):
    for day in range(22, 29):
        if day_of_week_str(11, day, year) == 'Thursday':
            return day

# This function runs the program.
# Parameters: n/a
# Returns: n/a
def main():
    user_choice = 'y'
    while user_choice == 'y':
        print("Pick a date, any date (such as your birthday!)")
        user_month = int(input("What is the month? (1-12) "))
        user_day = int(input("What is the day? "))
        user_year = int(input("What is the year? "))
        print("This is day number", day_of_year(user_month, user_day, user_year), "of the year", user_year)
        print("This day falls on a", day_of_week_str(user_month, user_day, user_year))
        print("In 2020, this date falls on a", day_of_week_str(user_month, user_day, 2020))
        print("In ", user_year, ", New Year's Day falls on a ", day_of_week_str(1, 1, user_year), sep='')
        print("In ", user_year, ", Thanksgiving's Day falls on day ", find_thanksgiving(user_year), " of November", sep='')
        user_choice = input("Would you like to pick another date? (y for yes): ")
        if user_choice == 'y':
            print("\n")

main()