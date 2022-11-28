import re

def run():
    with open('input') as f:
        lines = f.readlines()
    line_pattern = r'(?P<min_count>[0-9]+)-(?P<max_count>[0-9]+) (?P<test_char>[a-z]): (?P<password>[a-z]+)$'
    valid_passwords = 0
    for line in lines:
        match = re.match(line_pattern, line)
        (min_count, max_count, test_char, password) = match.groups()
        if password.count(test_char) >= int(min_count) and password.count(test_char) <= int(max_count):
            print(f'{password} has {min_count} - {max_count} (inclusive) instances of {test_char}')
            valid_passwords += 1
    print(f'Found {valid_passwords} valid passwords.')


if __name__ == '__main__':
    run()
