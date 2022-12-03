fileObj = open('../input.txt', "r")
rounds = fileObj.read().split('\n')

total_score= 0
for round in rounds:
    opponent_choice = round.split()[0]
    my_strategy = round.split()[1]

    # need to loose
    if(my_strategy=='X'):  
        if(opponent_choice=='A'):
            my_choice='C'
            total_score+=3
        elif(opponent_choice=='B'):
            my_choice='A'
            total_score+=1
        else:
            my_choice='B'
            total_score+=2
    # need to draw
    elif(my_strategy=='Y'):
        my_choice=opponent_choice
        if(opponent_choice=='A'):
            total_score+=1
        elif(opponent_choice=='B'):
            total_score+=2
        else:
            total_score+=3
    # need to win
    else:
        if(opponent_choice=='A'):
            my_choice='B'
            total_score+=2
        elif(opponent_choice=='B'):
            my_choice='C'
            total_score+=3
        else:
            my_choice='A'
            total_score+=1

    if my_choice == opponent_choice:
        total_score += 3
    elif ((my_choice=='A' and opponent_choice=='C') or (my_choice=='B' and opponent_choice=='A') or (my_choice=='C' and opponent_choice=='B')):
        total_score += 6
        
print(total_score)