def computeTuition():
    '''Returns total tuition cost for student'''
    chour = input("Enter the number of credit hours: ")
    chour = int(chour)
    cost = input("Enter the cost per credit hour: ")
    cost = float(cost)
    ans = chour * cost
    if((ans).is_integer() == True):
        ans = int(ans)
    return ans
    pass


def createStr(character, number):
    '''Duplicates entered character by entered number of times'''
    string = ""
    #if(len(character) == 1):
        #if(int(number) > 0):
           #string = str(character) * int(number)
    string = character * int(number)
    return string
    pass


def sequences():
    '''Prints 3 pre-set sequences'''
    for i in range(18,51,2):
        print(i,end = ' ')
    print()
    for i in range(8):
        print(9*(i+3), end = ' ')
    print()
    for i in range(8):
        print(40-(4*i), end = ' ')
    pass


def printAllBut(s):
    '''Takes string parameter then checks if string is in inputed list of strings'''
    slist = eval(input("Type a list of strings: "))
    for i in range(len(slist)):
        if s.lower() not in slist[i].lower():
            print(slist[i])
    pass


def printNth(n):
    '''Prints the nth element of an inputed list'''
    usrList = eval(input("Type a list: "))
    if(n > (len(usrList)-1)):
        pass
    elif(n < (-1 * (len(usrList)-1))):
        pass
    else:
        print(usrList[n])
    pass
