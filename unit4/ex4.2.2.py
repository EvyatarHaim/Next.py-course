def parse_ranges(ranges_string):
    ranges = (r.split('-') for r in ranges_string.split(','))
    return (num for start, stop in ranges for num in range(int(start), int(stop) + 1))
