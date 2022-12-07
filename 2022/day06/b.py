'''
- input is lines of random characters
- look for line character index after first group of 14 characters with no repeat
'''
with open('input', 'r') as f:
    for line in f:
        datastream = line.strip()
        for (cursor, char) in enumerate(datastream):
            if(len(set(datastream[cursor:cursor+14])) == 14):
                print(f'Processed {cursor+14} characters to find 14 different characters')
                break

