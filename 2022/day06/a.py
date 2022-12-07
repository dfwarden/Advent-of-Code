'''
- input is lines of random characters
- look for line character index after first group of 4 characters with no repeat
'''
with open('input', 'r') as f:
    for line in f:
        datastream = line.strip()
        for (cursor, char) in enumerate(datastream):
            if(len(set(datastream[cursor:cursor+4])) == 4):
                print(f'Processed {cursor+4} characters to find 4 different characters')
                break

