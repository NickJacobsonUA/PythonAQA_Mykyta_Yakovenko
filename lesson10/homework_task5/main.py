import csv

def read_csv(file_name):
  lines = []
  with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      lines.append(row)
  return lines

def write_csv(file_name, lines):
  with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)

lines = [
  ['Name', 'Age'],
  ['Alice', '25'],
  ['Bob', '30']
]

# Write file
write_csv('test.csv', lines)

# Read file and add lines
read_lines = read_csv('test.csv')
read_lines.append(['Charlie', '35'])
read_lines.append(['Dave', '40'])

# Write updated data to new file
write_csv('new.csv', read_lines)