# write your code here
from random import randint


friend_num = int(input('Enter the number of friends joining (including you):'))
if friend_num <= 0:
    print('\nNo one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    friend_dict = {input(): 0 for i in range(friend_num)}
    rand_list = list(friend_dict)
    bill = float(input('\nEnter the total bill value:'))
    friend_dict = {v: round(bill / friend_num, 2) for v in friend_dict}
    friend_dict2 = {v: round(bill / (friend_num - 1), 2) for v in friend_dict}
    if input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:') == 'Yes':
        lucky = rand_list[randint(0, (friend_num - 1))]
        print(f'\n{lucky} is the lucky one!')
        friend_dict2[lucky] = 0
        print(f'\n{friend_dict2}')
    else:
        print('\nNo one is going to be lucky')
        print(friend_dict)
