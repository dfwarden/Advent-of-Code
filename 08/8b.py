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
    repair_attempted = False
    attempted_repair_indexes = []
    executed_indexes = []
    while True:
        if current_index >= len(instructions):
            print('Success! executed last instruction.')
            break
        instruction = instructions[current_index]
        if current_index in executed_indexes:
            # Hit a repeat, reset
            print(f'Refusing to repeat instruction {current_index}, starting over')
            current_index = 0
            accumulator = 0
            executed_indexes = []
            repair_attempted = False
            continue
        # Store operation locally so we can "repair" it without interfering with future runs.
        operation = instruction['operation']
        # Attempt to repair (switch between nop/jmp)
        # the current instruction if it is nop/jmp and we haven't tried yet
        if operation in ['nop', 'jmp'] and current_index not in attempted_repair_indexes and not repair_attempted:
            repair_attempted = True
            attempted_repair_indexes.append(current_index)
            print(f'Attempting to repair instruction {current_index}')
            if operation == 'nop':
                operation = 'jmp'
            else:
                operation = 'nop'
        #print(f'Executing index {current_index}: {instruction}')
        executed_indexes.append(current_index)
        if operation == 'acc':
            accumulator += instruction['argument']
        if operation == 'jmp':
            current_index += instruction['argument']
        else:
            current_index += 1
    print(f'After execution, accumulator is: {accumulator}')





if __name__ == '__main__':
    run()
