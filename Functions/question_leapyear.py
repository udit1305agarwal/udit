def is_leap_year(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400  == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(is_leap_year(2050))

        