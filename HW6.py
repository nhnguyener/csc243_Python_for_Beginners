import random

def craps():
    '''simulates one round of craps game,
    returns 1 if player wins, 0 if loss'''
    player = 0
    while player not in [2,3,7,11,12]:
        player = random.randrange(1,7) + random.randrange(1,7)
        if(player == 7) or (player == 11):
            return 1
        elif(player == 2) or (player == 3) or (player == 12):
            return 0
    player = 0
    pass

def testCraps(n):
    '''returns percentage of games won
    in n games'''
    count = 0
    wins = 0
    while(count < n):
        wins += craps()
        count += 1
    print(wins, count, n)
    return (wins/n)
    pass

def game(n):
    '''n amount of simple addition games
    where numbers are [0,9], returning amount of
    correct answers out of total'''
    count = 0
    correct = 0
    while count < n:
        q1 = random.randrange(0,10)
        q2 = random.randrange(0,10)
        answer = q1 + q2
        print(q1,' + ', q2, '=')
        #print(answer)
        usrans = int(input("Enter answer: "))
        if(usrans == answer):
            print("Correct.")
            correct += 1
        else:
            print("Incorrect.")
        count += 1
    print("You got", correct,"answers out of", n)
            
    
    pass

def networks(n, friends):
    '''returns which friends belong to which social network'''
    groups= []
    for i in range(n):
        groups.append({i})
    for j in friends:
        fgroup = groups[j[0]]|groups[j[1]]
        for k in fgroup:
            groups[k] = fgroup
    groupset = set()
    for g in groups:
        groupset.add(tuple(g))
    i = 0
    #for s in groupset:
        #print("Social network",i,"is",set(s))
        #i += 1
    return groupset
    pass

