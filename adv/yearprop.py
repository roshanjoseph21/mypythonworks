#print 1800 - 2024

years=[y for y in range(1800,2025)]
print(years)


century_year=[y for y in years if y%100==0]
print(century_year)

#print leap year 
leap_year=[y for y in years if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0)]
print(leap_year)

