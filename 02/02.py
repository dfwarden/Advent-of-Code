def run_02():
    with open('input') as f:
        input = f.read()
    numbers = [number for number in map(int, input.split())]
    print(f'len: {len(numbers)}\n{numbers}')
    for number in numbers:
        for number2 in numbers:
            for number3 in numbers:
                if number + number2 + number3 == 2020:
                    print(f'found entries: {number} * {number2} * {number3} = {number * number2 * number3}')

if __name__ == '__main__':
    run_02()
