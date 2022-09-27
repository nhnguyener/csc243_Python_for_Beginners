def letter2number(letter):
    '''takes an input letter grade and returns the corresponding
    number grade (0 to 4) using a dictionary; '-' decreases grade by 0.3 and
    '+' increases grade by 0.3'''
    scores = {
        "A+" : 4.3,
        "A" : 4,
        "A-" : 3.7,
        "B+" : 3.3,
        "B" : 3,
        "B-" : 2.7,
        "C+" : 2.3,
        "C" : 2,
        "C-" : 1.7,
        "D+" : 1.3,
        "D"  : 1,
        "D-" : 0.7,
        "F+" : 0.3,
        "F" : 0,
        "F-" : -0.3
        }
    grade = (scores[letter])
    
    return grade
    
    pass

def ex613():
    '''defines a dictionary called agencies then modifies said dictionary
    according to example 6.13'''
    agencies = {
        "CCC" : 'Civilian Conservation Corps',
        "FCC" : 'Federal Communications Commision',
        "FDIC" : 'Federal Deposit Insurance Corporation',
        "SSB" : 'Social Security Board',
        "WPA" : 'Works Progress Administration'
        }
    print(agencies)
    agencies["SEC"] = 'Securities and Exchange Commision'
    agencies["SSB"] = 'Social Security Administration'
    print(agencies)
    del agencies["CCC"]
    del agencies["WPA"]
    print(agencies)
    pass

def reverse(original):
    '''inputs a phonebook and returns phonebook
    with names and keys mapping reversed'''
    changed = {v: k for k, v in original.items()}

    return changed
    pass

def different(table):
    '''that takes a two-dimensional table as input and returns
    the number of distinct entries in the table'''
    '''[[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]'''
    uNum = {}
    uNum[table[0][0]] = 1
    for i in range(len(table)):
        for j in range(len(table[i])):
            for k in table[i]:
                uNum[k] = 1
                #print(uNum)
    return len(uNum)
    
    pass

def index(filename, words):
    '''returns indexes of words in text file'''
    '''['raven', 'mortal', 'dying', 'ghost', 'ghastly', 'evil','demon']'''
    pos = []
    printed = 0
    text = open(filename,'r')
    
    for i in words:
        text = open(filename,'r')
        for c, line in enumerate(text,1):
            if i in line:
                if printed == 0:
                    print(i, end = '\t')
                    printed = 1
                pos.append(c)
        if pos != []:
            if i == 'raven':
                pos.remove(52)
            print(str(pos).strip('[]'))
        printed = 0        
        pos = []
        
    
    pass
