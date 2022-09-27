def Rtriangle(n):
    if n == 0:
        pass
    else:
        Rtriangle(n-1)
        print("*"*n)

def Rsilly(n):
    if n > 0:
        return ('!' + Rsilly(n-1) + '?')
    else:
        return ''

def count_helper(lst, n, length, index, count):
    if length == index:
        return count
    else:
        if lst[index] == n:
            return count_helper(lst, n, length, index+1, count+1)
        else:
            return count_helper(lst, n, length, index+1, count)

def Rcount(lst, n):
    count = 0
    count = count_helper(lst, n, len(lst), 0, count)
    return count

def filter_helper(lst, n):
    if length == index:
        return count
    else:
        if lst[index] == n:
            return count_helper(lst, n, length, index+1, count+1)
        else:
            return count_helper(lst, n, length, index+1, count)
        

def Rfilter(lst, n):
  
    

def RdeleteEveryOther(lst):

