#PRINT ALL LEAP YEAR 1800,2024

for year in range(1800,2025):
    if year%100==0 and year%400==0:
        print(year)
    elif year%4==0:
        print(year)