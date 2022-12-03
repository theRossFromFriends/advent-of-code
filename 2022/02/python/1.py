fileObj = open('../input.txt', "r")
rounds = fileObj.read().split('\n')

total_score= 0
for round in rounds:
    opponent_choice = round.split()[0]
    my_choice = round.split()[1]

    if(my_choice=='X'):
        total_score+=1
        my_choice='A'
    elif(my_choice=='Y'):
        total_score+=2
        my_choice='B'
    else:
        total_score+=3
        my_choice='C'

    if my_choice == opponent_choice:
        total_score += 3
    elif ((my_choice=='A' and opponent_choice=='C') or (my_choice=='B' and opponent_choice=='A') or (my_choice=='C' and opponent_choice=='B')):
        total_score += 6
        
print(total_score)