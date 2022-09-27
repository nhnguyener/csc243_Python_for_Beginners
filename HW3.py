def indexes(string, char):
    '''returns indexes of where char appears in string'''
    return [i for i, ltr in enumerate(string) if ltr == char]

    pass

def doubles(numberList):
    '''returns a list of numbers that were double the value
    of the previous number in numberList'''
    dlist = []
    for i in range(len(numberList)-1):
        if numberList[i+1] == numberList[i]*2:
            dlist.append(numberList[i+1])
    return dlist

    pass

def rps(play1, play2):
    '''play1 and play2 are either rock paper or scissors. If play1 wins
    -1 is returned, 0 if tie, 1 if play2 wins.'''
    if play1.upper() == 'R':
        if play2.upper() == 'S':
            return -1
        elif play2.upper() == 'R':
            return 0
        elif play2.upper() == 'P':
            return 1
    elif play1.upper() == 'P':
        if play2.upper() == 'R':
            return -1
        elif play2.upper() == 'P':
            return 0
        elif play2.upper() == 'S':
            return 1
    elif play1.upper() == 'S':
        if play2.upper() == 'P':
            return -1
        elif play2.upper() == 'S':
            return 0
        elif play2.upper() == 'R':
            return 1

    pass

def tableMax(table):
    '''returns max value in 2D table of floats'''
    maxNum = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            #print("#: ", table[i][j])
            #if(i == 0):
            #    if table[i][-1] > table[i][j]:
            #        maxNum = table[i][-1]
            #        #print("max:", maxNum)
            #    elif table[i][-1] < table[i][j]:
            #        maxNum = table[i][j]
                    #print("max:", maxNum)
            #else:
            if (table[i][-1] > table[i][j]) and (table[i][-1] > maxNum):
                maxNum = table[i][-1]
                #print("max:", maxNum)
            elif (table[i][-1] < table[i][j]) and (table[i][j] > maxNum):
                maxNum = table[i][j]
                    #print("max:", maxNum)
    return maxNum
    
    
    pass

def columnMins(table):
    '''returns min val in each column from 2d table'''
    #x = [[1,2.1,-4],[-3,-1,6]],y = [[1,-1],[2,7.32],[0,4.2]],z = [[-5,8,4],[9,0,-4],[8,4,-10]]
    temp = 0
    col = []
    for i in range(len(table[0])):
        for j in range(len(table)):
            if(j < len(table)-1):
                if(table[j][i] < table[j+1][i]):
                    temp = table[j][i]
                elif(table[j+1][i] < table[j][i]):
                    temp = table[j+1][i]
            if(j < len(table)-1) and (j > 0):
                #print(table[j][i],table[j+1][i],"\n//////////")
                if(table[j][i] < table[j+1][i]) and (table[j][i] < table[j-1][i]):
                    temp = table[j][i]
                elif(table[j+1][i] < table[j][i]) and (table[j+1][i] < table[j-1][i]):
                    temp = table[j+1][i]
                elif(table[j-1][i] < table[j][i]) and (table[j-1][i] < table[j+1][i]):
                    temp = table[j-1][i]
                #print("Temp ",temp)
        col.append(temp)
    return col
    pass
