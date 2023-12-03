import re

p1_ans = 0
with open('AOC2023_D1.txt', 'r') as file:
    for l in file:
        digits = ''.join(filter(str.isdigit, l))  # Filter out only the digits
        if digits:  # Check if there is at least one digit
            calc_num = int(digits[0] + digits[-1])
            p1_ans += calc_num

print('Day 1 Part 1 Answer: ', p1_ans)

#Step 1: Initialize variable to store final answer
p2_ans = 0

#Step 2: Setup dictionary based on problem information
char_to_digit = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def process_line(line, mapping):
    # Replace spelled-out numbers with intermediate representations
    for word, replacement in mapping.items():
        line = line.replace(word, replacement)
    
    # Remove all remaining letters
    line = re.sub(r"[a-zA-Z]", "", line)

    # Calculate the value from the first and last digits
    if len(line) >= 2:
        return int(line[0] + line[-1])
    elif len(line) == 1:
        return int(line) * 11
    else:
        return 0

# Calculate the total sum
p2_ans = 0
with open('input3.txt', 'r') as file:
    for line in file:
        p2_ans += process_line(line.strip(), char_to_digit)

print('Day 1 Part 2 Answer: ',p2_ans)
