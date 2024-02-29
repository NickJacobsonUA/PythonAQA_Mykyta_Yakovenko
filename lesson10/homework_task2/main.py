import csv


# with open('domains.txt') as domains:
#     domains_reader = csv.reader(domains, delimiter=',')


def get_domain_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            name = line.strip().lstrip('.')
            names.append(name)
    return names


domain_names = get_domain_names('domains.txt')
print(domain_names)
