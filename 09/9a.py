import re

def run():
    '''
        File input is a plain text file of lines where each line
        is an integer.

        Look for the first number that can't be the sum of the previous 25 numbers.
    '''
    numbers = []
    with open('input') as f:
        lines = f.readlines()
    for line in lines:
        numbers.append(int(line))
    preamble_count = 25
    for index in range(preamble_count, len(numbers)):
        # determine if this number is the sum of any of the {preamble_count} previous numbers
        number = numbers[index]
        found_sum = False
        for first_num in range(index - preamble_count, index):
            for second_num in range(index - preamble_count, index):
                if numbers[first_num] + numbers[second_num] == number:
                    found_sum = True
        if not found_sum:
            print(f'Could not find 2 numbers that add to {number} in {numbers[index - preamble_count:index]}')
            break





if __name__ == '__main__':
    run()
