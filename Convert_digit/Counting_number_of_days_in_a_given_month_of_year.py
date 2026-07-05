#Number of days in a given month of a given year in  Python
"""Number of days in any month of a year can vary specifically in February as the cycle of leap year repeats in every 4 years when the year is leap February gives the count to 29 days but the when the year is not leap it gives count to 28 days and so no of days in a year varies from 365 to 366."""

month = 12
year=2012
    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29");

elif(month==2) :
    print("Number of days is 28");

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31");

else :
    print("Number of days is 30");