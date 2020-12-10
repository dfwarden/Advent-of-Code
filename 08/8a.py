import re

def run():
    '''
        File input is a plain text file of lines where each line
        is an instruction, structured as:
        (operation, argument)
    '''
    with open('input') as f:
        lines = f.readlines()
    instructions = []
    instruction_pattern = r'(?P<operation>acc|jmp|nop) (?P<argument>[+-][0-9]+)'
    for line in lines:
        instruction = re.match(instruction_pattern, line).groupdict()
        instruction['argument'] = int(instruction['argument'])
        instructions.append(instruction)
    instructions_indexes = range(0, len(instructions))
    accumulator = 0
    current_index = 0
    executed_indexes = []
    while True:
        instruction = instructions[current_index]
        print(f'Executing index {current_index}: {instruction}')
        if current_index in executed_indexes:
            break
        executed_indexes.append(current_index)
        if instruction['operation'] == 'acc':
            accumulator += instruction['argument']
        if instruction['operation'] == 'jmp':
            current_index += instruction['argument']
        else:
            current_index += 1
    print(f'Stopped before executing instruction {current_index} twice, accumulator: {accumulator}')





if __name__ == '__main__':
    run()
