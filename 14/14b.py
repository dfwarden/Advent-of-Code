import copy


def run():
    '''
        File input is a plain text file of lines.

        Lines can either be a mask or mem[x] line.
    '''
    with open('input') as f:
        lines = f.readlines()
    instructions = [line.rstrip().split(' = ') for line in lines]
    #print(instructions)
    current_mask = 'X' * 36
    memory = dict()
    for (operation, argument) in instructions:
        if operation == 'mask':
            current_mask = argument
            #print(f'Updated current_mask to: {current_mask}')
        if operation[:3] == 'mem':
            bank = operation[4:operation.index(']')]
            input_binary = f'{int(bank):036b}'
            print(f'mask: {current_mask}\ninpu: {input_binary}')
            # Mask values now mean - 0: no change, 1: set bit to 1, X: both values are possible
            # First, process the 0 and 1 mask values, and retain X mask values for later processing.
            output_binary = []
            for (mask_chr, input_chr) in zip(current_mask, input_binary):
                if mask_chr == '0':
                    output_binary.append(input_chr)
                else:  # '1' or 'X'
                    output_binary.append(mask_chr)
            output_binary = ''.join(output_binary)
            print(f'out:  {output_binary}')
            # Next, process the X characters
            memory_banks_binary = process_x(output_binary)
            print(f'After a bunch of work, adding the following to bank {bank} from input {argument}:')
            for b in memory_banks_binary:
                memory[int(b, 2)] = int(argument)
                print(f'wrote {argument} to memory bank {int(b,2)}')

    # now find the sum of all memory banks set
    print(f'Sum of all memory bank values: {sum(memory.values())}')


def process_x(input_binary):
    if input_binary.find('X') == -1:
        return [input_binary]
    return process_x(input_binary.replace('X','1',1)) + process_x(input_binary.replace('X','0',1))

if __name__ == '__main__':
    run()
