import numpy as np

fileObj = open('input', "r")
input_data = np.array(fileObj.read().splitlines())
data = [(y[0].split(), y[1].split()) for y in [x.split('|') for x in input_data]]

def check_for_substring(substring, string):
    return (0 not in [s in string for s in substring])

def

count = 0
for (displays, outputs) in data:
    symbols_dict = {}
    displays_to_delete = []
    for idx, display in enumerate(displays):
        if len(display) == 2:
            symbols_dict[display] = 1
            displays_to_delete.append(idx)

        elif len(display) == 3:
            symbols_dict[display] = 7
            displays_to_delete.append(idx)
        elif len(display) == 4:
            symbols_dict[display] = 4
            displays_to_delete.append(idx)
        elif len(display) == 7:
            symbols_dict[display] = 8
            displays_to_delete.append(idx)

    displays = [display for (idx, display) in enumerate(displays) if idx not in displays_to_delete]
        
    for key, value in symbols_dict.items():
        if value == 1:
            representation_1 = key
        elif value == 7:
            representation_7 = key
        elif value == 4:
            representation_4 = key
        elif value == 8:
            representation_8 = key

    displays_to_delete = []
    for idx, display in enumerate(displays):
        if len(display) == 6:
            if check_for_substring(representation_4, display):
                symbols_dict[display] = 9
                displays_to_delete.append(idx)
                print(symbols_dict[display])
            elif (check_for_substring(display, representation_8) and (not check_for_substring(representation_7, display))):
                symbols_dict[display] = 6
                displays_to_delete.append(idx)
            else:
                symbols_dict[display] = 0
                displays_to_delete.append(idx)

    displays = [display for (idx, display) in enumerate(displays) if idx not in displays_to_delete]

    for key, value in symbols_dict.items():
        if value == 9:
            representation_9 = key
        elif value == 0:
            representation_0 = key
        elif value == 6:
            representation_6 = key

    for idx, display in enumerate(displays):
        if len(display) == 5:
            if check_for_substring(display, representation_6):
                symbols_dict[display] = 5
            elif check_for_substring(display, representation_9):
                symbols_dict[display] = 3           
            else:
                symbols_dict[display] = 2

    number = ''
    for output in outputs:
        for key, value in symbols_dict.items():
            if (len(output) == len(key) and check_for_substring(output, key)):
                number += str(value)
    count += int(number)

print(count)