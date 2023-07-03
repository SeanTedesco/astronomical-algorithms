"""
JULIAN DAY CONVERSION

In this module, we give a method of converting a date, givven in the
Julian or in the Gregorian calender, into the corresponding Julian Day
number (JD), or vice versa.

Chapter 7 of Astronomical Algorithms
"""
from datetime import datetime
import time
import math


def date_to_juilian(year: int, month: int, day: float):
    A = int(year / 100)
    B = 2 - A + int(A / 4)
    juilian_day = (
        int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
    )
    return juilian_day


def date_to_modified_julian_day(year: int, month: int, day: float):
    """
    MJD = 0.0 corresponds to 1858 November 17 at 0h UT
    """
    jd = date_to_juilian(year, month, day)
    mjd = jd - 2400000.5
    return mjd


def date_from_julian(julian_day: float):
    day, month, year = -1, -1, -1
    a, b, c, d, e, f, alpha = 0, 0, 0, 0, 0, 0, 0

    f, z = math.modf(julian_day + 0.5)

    if z >= 2299161:
        alpha = int((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - int(alpha / 4)
    else:
        a = z

    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)

    day = b - d - int(30.6001 * e) + f
    if e < 14:
        month = e - 1
    elif e == 14 or e == 15:
        month = e - 13
    if month > 2:
        year = c - 4716
    elif month == 1 or month == 2:
        year = c - 4715

    return (year, month, day)


def time_between_dates(year1, month1, day1, year2, month2, day2):
    jd1 = date_to_juilian(year1, month1, day1)
    jd2 = date_to_juilian(year2, month2, day2)
    return jd2 - jd1


def main():
    julian_day = date_to_juilian(1957, 10, 4.81)
    print(julian_day)

    day = date_from_julian(julian_day)
    print(day)

    time_delta = time_between_dates(1910, 4, 20, 1986, 2, 9)
    print(time_delta)


if __name__ == "__main__":
    main()
