entered_words = []

while True:
    entered = input('Add a note: ')
    if entered == 'latest':
        print(entered_words)
        continue

    elif entered == 'earliest':
        reverse = reversed(entered_words)
        print(list(reverse))
        continue

    elif entered == 'shortest':
        print(sorted(entered_words, key=len))
        continue

    elif entered == 'longest':
        print(sorted(entered_words, key = len, reverse=True))
        continue

    elif entered == 'exit':
        print('Bye bye')
        break

    else:
        entered_words.append(entered)




