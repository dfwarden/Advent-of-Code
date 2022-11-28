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
        if set(required_fields) - set(record.keys()) != set():
            continue
        # All fields are present, now process per-field validity rules
        # I'm not sure about the performance inpact of range(). I think Python 3 does the right thing.
        # But you do need to add 1 to the upper bound of range to include that number.
        byr_pattern = r'^[0-9]{4}$'
        byr_range = range(1920, 2002+1)
        if not re.match(byr_pattern, record['byr']) or int(record['byr']) not in byr_range:
            print(f'{record["byr"]} does not mattch {byr_pattern} or not in range {byr_range}')
            continue
        iyr_pattern = r'^[0-9]{4}$'
        iyr_range = range(2010, 2020+1)
        if not re.match(iyr_pattern, record['iyr']) or int(record['iyr']) not in iyr_range:
            print(f'{record["iyr"]} does not mattch {iyr_pattern} or not in range {iyr_range}')
            continue
        eyr_pattern = r'^[0-9]{4}$'
        eyr_range = range(2020, 2030+1)
        if not re.match(eyr_pattern, record['eyr']) or int(record['eyr']) not in eyr_range:
            print(f'{record["eyr"]} does not mattch {eyr_pattern} or not in range {eyr_range}')
            continue
        hgt_pattern = r'^(?P<height_number>[0-9]+)(cm|in)$'
        hgt_cm_range = range(150, 193+1)
        hgt_in_range = range(59, 76+1)
        if not re.match(hgt_pattern, record['hgt']):
            continue
        if record['hgt'][-2:] == 'cm' and int(record['hgt'][:-2]) not in hgt_cm_range:
            print(f'{record["hgt"]} does not mattch {hgt_cm_range}')
            continue
        if record['hgt'][-2:] == 'in' and int(record['hgt'][:-2]) not in hgt_in_range:
            print(f'{record["hgt"]} does not mattch {hgt_in_range}')
            continue
        hcl_pattern = r'^#[0-9a-f]{6}$'
        if not re.match(hcl_pattern, record['hcl']):
            print(f'{record["hcl"]} does not mattch {hcl_pattern}')
            continue
        ecl_pattern = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
        if not re.match(ecl_pattern, record['ecl']):
            print(f'{record["ecl"]} does not mattch {ecl_pattern}')
            continue
        # match() behavior is to search from the start of the string.
        # The pattern needs $ to ensure no junk after the first 9 digits!
        pid_pattern = r'^[0-9]{9}$'
        if not re.match(pid_pattern, record['pid']):
            print(f'{record["pid"]} does not mattch {pid_pattern}')
            continue
        valid_records += 1
    print(f'Valid records: {valid_records}')


if __name__ == '__main__':
    run()
