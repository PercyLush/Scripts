def is_year_leap(year):
    is_leap = False
    
    if year % 4 == 0:
        is_leap = True
    if year % 400 == 0:
        is_leap = True
    if year % 100 == 0:
        is_leap = False
    return is_leap
        
def days_in_month(year, month):
    if isinstance(year, int) and isinstance(month, int):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = is_year_leap(year)
        
        if is_leap:
            months[1] = 29
            
        return months[month-1]
    return None
def day_of_year(year, month, day):
    is_leap = is_year_leap(year)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Days = 0
    if is_leap:
        months[1] = 29
        
    for n in range(month-1):
        Days += months[n]
        
    Days = Days + day
    return Days
    
print(day_of_year(2000, 12, 31))
