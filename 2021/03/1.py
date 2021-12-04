fileObj = open('input', "r")
lines = fileObj.read().splitlines()
line_length = len(lines[0])

bit_count = [[0, 0] for x in range(line_length)]
for i in range(0, len(lines)):
    line = lines[i]
    for j in range(0, line_length):
        if line[j] == '0':
            bit_count[j][0] += 1
        else:
            bit_count[j][1] += 1

gamma = '0b'
epsilon = '0b'
for i in range(0, line_length):
    if bit_count[i][0] > bit_count[i][1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
