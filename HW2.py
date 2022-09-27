def doubleList(listOfNumbers):
    '''doubles the values in an int list'''
    newList = []
    for i in listOfNumbers:
        newList.append(i*2)
    listOfNumbers[:] = newList
    
    pass


def acronym(stringOfWords):
    '''returns the first letter of each input word to create acronym'''
    words = stringOfWords.split(' ')
    acro = ''
    for i in words:
        acro = acro + i[0].capitalize()
    return acro

    pass


def multiples(listOfInts, n):
    '''returns multiples of int n in list of ints'''
    multList = []
    for i in listOfInts:
        if(i%n == 0):
            multList.append(i)
    return(multList)

    pass


def formatNames(inName, outName):
    '''reads text file of names and reorganizes by last name'''
    uNames = open(inName, "r")
    content = uNames.readlines()
    sNames = open(outName, "w+")
    first = ''
    middle = ''
    last = ''
    tcontent = ''
    for i in range(len(content)):
        fdata = content[i].split(' ')
        if len(fdata) <= 2:
            first = fdata[0]
            last = fdata[1][:-1]
            tcontent = "{}, {}\n".format(last, first)
            sNames.write(tcontent)
        elif len(fdata) <= 2 and i == len(fdata):
            first = fdata[0]
            last = fdata[1]
            tcontent = "{}, {}\n".format(last, first)
            sNames.write(tcontent)
        elif len(fdata) > 2 and i == len(fdata):
            first = fdata[0]
            middle = fdata[1][0]
            last = fdata[2]
            tcontent = "{}, {} {}.\n".format(last, first, middle)
            sNames.write(tcontent)
        else:
            first = fdata[0]
            middle = fdata[1][0]
            last = fdata[2][:-1]
            tcontent = "{}, {} {}.\n".format(last, first, middle)
            sNames.write(tcontent)
    uNames.close()
    sNames.close()
        
    pass


def partition(listOfStrings, letter):
    '''takes in list of strings and a character, then returns words from list that start with 'a' and end with a letter before the input letter, or the input letter'''
    words = []
    for i in listOfStrings:
        if(ord(i[0].lower()) <= ord(letter.lower())):
            words.append(i)
    return(words)
    
    pass

