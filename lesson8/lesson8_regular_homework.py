import re

# Task 1:


regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_])[\w]+$"

test_str = "Test_123"

result = re.search(regex, test_str)

print(result)

# Task 2:

strings = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

pattern = r"\(.*?\)"

new_strings = []
for string in strings:
    new_string = re.sub(pattern, "", string)
    new_strings.append(new_string)

print(new_strings)
