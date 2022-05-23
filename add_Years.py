#The function addYears() used to add a given number of years to a date
def addYears(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result