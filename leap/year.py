def is_leap_year(year):
    four = by_four(year)
    hundred = by_hundred(year)
    four_hundred = by_four_hundred(year)
    if (four):
        if (hundred):
            if (four_hundred):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def by_four(year):
    if ((year%4) == 0):
        return True
    else:
        return False

def by_hundred(year):
    if ((year%100) == 0):
        return True
    else:
        return False

def by_four_hundred(year):
    if ((year%400) == 0):
        return True
    else:
        return False
