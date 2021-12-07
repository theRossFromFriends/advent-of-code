import numpy as np

fileObj = open('input', "r")
fish_array = np.array(fileObj.read().split(',')).astype(int)

age_days_to_n = {}
def calc_age_days_to_n(age, days):
    if (age, days) in age_days_to_n:
        return age_days_to_n[(age, days)]

    if days == 0:
        n = 1
    elif age == 0:
        n = calc_age_days_to_n(6, days-1) + calc_age_days_to_n(8, days-1)
    else:
        n = calc_age_days_to_n(age-1, days-1)
    age_days_to_n[(age, days)] = n

    return n


for days in range(257):
    for age in range(9):
        calc_age_days_to_n(age, days)

fish_after_n_days = {age: age_days_to_n[(age, 256)] for age in range(9)}

count = 0
for fish in fish_array:
    count += fish_after_n_days[fish]

print(count)
