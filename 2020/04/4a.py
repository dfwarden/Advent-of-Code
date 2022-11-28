import re

def run():
    '''
        File input is a plain text file of key:value pairs separated by spaces.
        Multiple key:value pairs comprise a record, which is separated by a blank line.
        I added a newline to the end of the input file to make processing easier.
    '''
    with open('input') as f:
        lines = f.readlines()
    # 'cid' is a possible field but is not required for North Pole creds.
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    field_pattern = r'(?P<key>[a-z]+):(?P<value>\S+)'
    records = []
    record = {}
    for line in lines:
        # if blank line, store the record we have so far (if any)
        if line == '\n':
            if record != {}:
                records.append(record)
                record = {}
            continue
        # Not blank line, parse key:value pairs
        pairs = re.findall(field_pattern, line.rstrip())
        record.update(pairs)
    # records parsed, count how many are valid
    valid_records = 0
    for record in records:
        # Record is valid if all of the fields in required_fields are in record
        # There are 2 ways I can think to do this: set different, and all()
        # print(f'Comparing:\n\tset method: {set(required_fields) - set(record.keys())}\n\t{all(True if field in record.keys() else False for field in required_fields)}')
        # Set different is more readable to me: "If set difference is empty set, all fields in required are present in record."
        if set(required_fields) - set(record.keys()) == set():
            valid_records += 1
    print(f'Valid records: {valid_records}')


if __name__ == '__main__':
    run()
