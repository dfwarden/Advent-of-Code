import re

def run():
    with open('input') as f:
        lines = f.readlines()
    line_pattern = r'(?P<first_index>[0-9]+)-(?P<second_index>[0-9]+) (?P<test_char>[a-z]): (?P<password>[a-z]+)$'
    valid_passwords = 0
    for line in lines:
        match = re.match(line_pattern, line)
        (first_index, second_index, test_char, password) = match.groups()
        first_index = int(first_index)
        second_index = int(second_index)
        if((password[first_index-1] == test_char) ^ (password[second_index-1] == test_char)):
            print(f'{password} has only one of {test_char} in ({password[first_index-1]}, {password[second_index-1]})')
            valid_passwords += 1
    print(f'Found {valid_passwords} valid passwords.')


if __name__ == '__main__':
    run()
