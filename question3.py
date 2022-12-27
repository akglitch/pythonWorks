import calendar 

def date_printer(date):
    splitdate = date.split("/")
    a = f"{calendar.month_name[int(splitdate[0])].title()} {splitdate[1]}, {splitdate[2]}."
    return a

print(date_printer("04/10/2022"))