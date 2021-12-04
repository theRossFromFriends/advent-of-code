fileObj = open('input', "r")
lines = fileObj.read().splitlines()

count = 0
for i in range(1, len(lines)-2):
    current_sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    previous_sum = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
    if current_sum > previous_sum:
        count += 1

print(count)
