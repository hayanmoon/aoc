# possible solutions
# get the first character then get the last
# get list of numbers only then get the first and last

def main():
    with open('input.txt', 'r') as f:
        total = 0
        for line in f:
            # firstNum = None
            # lastNum = None
            # for i in range(len(line)):
            #     if firstNum != None and i ==

            #     if firstNum == None and line[i].isnumeric():
            #         firstNum = line[i]

            #     if lastNum == None and line[len(line)-i].isnumeric():
            #         lastNum == line[len(line)-i]

            # print(firstNum, lastNum)

            list = [num for num in line if num.isnumeric()]
            total = total + int(list[0] + list[len(list)-1])
        print(total)
main()
