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
    # Try to find at least 2 contiguous numbers that sum to 217430975 (numbers[584])
    target_number = 217430975
    for start_index in range(0, len(numbers)):
        for end_index in range(start_index, len(numbers)):
            group_sum = sum(numbers[start_index:end_index])
            if(group_sum > target_number):
                break
            if(group_sum == target_number):
                group = numbers[start_index:end_index]
                print(f'Found contiguous numbers that sum to {target_number}: {group}')
                print(f'Sum of smallest and largest in that group: {min(group) + max(group)}')
                return





if __name__ == '__main__':
    run()
