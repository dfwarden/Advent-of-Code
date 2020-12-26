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
            print(f'Updated current_mask to: {current_mask}')
        if operation[:3] == 'mem':
            bank = operation[4:operation.index(']')]
            # mask argument with current_mask, then store in memory[bank]
            input_binary = f'{int(argument):036b}'
            #print(f'mask: {current_mask}\ninpu: {input_binary}')
            output_binary = ''.join([input_chr if mask_chr == 'X' else mask_chr for (mask_chr, input_chr) in zip(current_mask, input_binary)])
            #print(f'outp: {output_binary}')
            memory[bank] = int(output_binary, 2)

    # now find the sum of all memory banks set
    print(f'Sum of all memory bank values: {sum(memory.values())}')


if __name__ == '__main__':
    run()
