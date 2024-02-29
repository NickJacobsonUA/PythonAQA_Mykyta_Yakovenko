def get_surnames(filename):
    surnames = []

    with open(filename) as f:
        for line in f:
            parts = line.split()
            surnames.append(parts[1])

    return surnames

surnames = get_surnames('names.txt')
print(surnames)