def intersect(lista,listb):
    '''takes two lists with no duplicate values and returns
    a list containing values present in both lists'''
    common = []
    lista.sort()
    listb.sort()
    for i in range(len(lista)):
        for j in range(len(listb)):
            if lista[i] == listb[j]:
                common.append(lista[i])
                
    return common
    
    pass

def pay(wage,hours):
    '''takes wage and number of worked to compute pay...
    if hours more than 40 but less than/equal to 60 pay is
    1.5x regular, if hours more than 60 pay is 2x regular'''
    payroll = 0
    if hours > 60:
        payroll = (40*wage) + (20*(1.5*wage))
        hours -= 60
        payroll = payroll + (hours*(2*wage))
    elif hours > 40:
        payroll = (40*wage)
        hours -= 40
        payroll = payroll + (hours*(1.5*wage))
    else:
        payroll = hours * wage
        
    return payroll
    
    pass

def lastfirst(names):
    '''takes list of names in <last,first> order and returns
    two lists: (1) first names, (2) last names'''
    fnames = []
    lnames = []
    temp = ''
    for i in range(len(names)):
        temp = names[i].split(', ')
        fnames.append(temp[1])
        lnames.append(temp[0])
        temp = ''
    newnames = [fnames,lnames]

    return newnames

    pass

def inversions(string):
    '''returns the total number of inversions
    (out of order pairs) in string'''
    count = 0
    j = 0
    for i in range(len(string)):
        while (j < len(string)):
            if(ord(string[i]) > ord(string[j])):
                #print('COUNT: ',string[i],string[j],j)
                count += 1
            j += 1
        j = i + 1

    return count
    
    pass

def sublist(list1,list2):
    '''checks if list1 is a sublist of list2 by seeing
    if the elements in list1 appear in the same order
    as they appear in list2'''
    temp = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i] == list2[j]):
                if(j < temp):
                    return False
                temp = j

    return True

    pass
