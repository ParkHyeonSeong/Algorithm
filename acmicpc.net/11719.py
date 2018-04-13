string = [] # input value

while True:
    try:
        input_str = input()
        if input_str == "": # new line
            string.append(input_str)
            input_str = input()
            if input_str == "":
                break   # 2 new line break
            else:
                string.append(input_str)    # adding
        else:
            string.append(input_str)    # adding
    except EOFError:
        break   # Error Breaking

for line in string:
    print(line)