# possible solutions
# get the first character then get the last
# get list of numbers only then get the first and last

def find_digit(line, reverse=False):
    number_list = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    start = 0
    stop = len(line) + 1 # +1 is only used on reverse, normal loop will not reach +1 value
    step = 1

    if reverse:
        start = -1
        stop *= -1 # stop = stop * -1
        step *= -1 # step = step * -1

    for i in range(start, stop, step):
        if line[i].isnumeric():
            return line[i]

        if reverse:
            current_string = line[i:]
        else:
            current_string = line[:i + step]

        for num in number_list:
            if num in current_string:
                return number_list[num]


def main():
    with open('input.txt', 'r') as f:
        total = 0
        for line in f:
            first_digit = find_digit(line)
            last_digit = find_digit(line, True)

            total += int(first_digit + last_digit)

        print(total)
main()
