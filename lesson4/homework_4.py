entered_words = []

while True:
    entered = input('Add a note: ')
    if entered == 'latest':
        print(entered_words)
        break

    elif entered == 'earliest':
        reverse = reversed(entered_words)
        print(list(reverse))
        break

    elif entered == 'short':
        words = sorted(entered_words, key=len)
        break
    elif entered == 'longest':
        print(sorted(entered_words, key = len, reverse=True))
        break
    elif entered == 'exit':
        print('Bye - bye')
        break
    else:
        entered_words.append(entered)




