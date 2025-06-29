def gen_secs():
    for s in range(60):
        yield s


def gen_minutes():
    for m in range(60):
        yield m


def gen_hours():
    for h in range(24):
        yield h


def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for m in range(1, 13):
        yield m


def gen_days(month, leap_year=True):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year:
        num_days = 29
    else:
        num_days = days_in_month[month - 1]
    for d in range(1, num_days + 1):
        yield d


def gen_date():
    for y in gen_years():
        for m in gen_months():
            for d in gen_days(m, leap_year=(y % 4 == 0 and y % 100 != 0)):
                for time in gen_time():
                    yield f"{y}/{m}/{d} {time}"


def main():
    gen = gen_date()
    i = 0  # loop counter
    while True:
        current = next(gen)
        if i % 1000000 == 0:
            print(current)
        i += 1


if __name__ == '__main__':
    main()
