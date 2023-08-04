def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

def get_season(month, day):
    if (month == 12 and day >= 21) or (month <= 3 and day < 20):
        return "Winter"
    elif month >= 3 and month <= 5:
        return "Spring"
    elif month >= 6 and month <= 8:
        return "Summer"
    else:
        return "Autumn"

def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365

def get_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

if __name__ == "__main__":
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        season = get_season(month, day)
        print(f"The season for {month}/{day}/{year} is {season}.")

        if is_leap_year(year):
            print(f"{year} is a leap year. It has {get_days_in_year(year)} days.")
        else:
            next_leap_year = get_next_leap_year(year)
            print(f"{year} is not a leap year. The next leap year is {next_leap_year}.")

    except ValueError:
        print("Invalid input. Please enter valid integers for year, month, and day.")
