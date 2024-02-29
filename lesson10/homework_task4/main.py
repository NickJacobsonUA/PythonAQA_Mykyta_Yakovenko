import re


def get_dates(filename):
    dates = []
    date_pattern = re.compile(r'\d{1,2}\w{1,2} \w+ \d{4}')

    with open(filename) as f:
        for line in f:
            match = date_pattern.search(line)
            if match:
                date = match.group()
                dates.append({"date": date})

    return dates

dates = get_dates('authors.txt')
print(dates)