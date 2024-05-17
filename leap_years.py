leap_years = []
for year in range(1900, 2102):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)

print("Leap years from 1900 to 2100 are==", leap_years)