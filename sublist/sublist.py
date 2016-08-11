EQUAL = True
UNEQUAL = True
SUBLIST = True
SUPERLIST = True

def check_lists(list1, list2):
    if (is_superlist(list1, list2)):
        return SUPERLIST
    elif(is_sublist(list1, list2)):
        return SUBLIST
    elif(list1 == list2):
        return EQUAL
    else:
        return UNEQUAL

def is_superlist(list1, list2):
    if (not list2):
        return True
    else:
        list2length = len(list2)
        list2index = 0
        for index in range(len(list1)):
            if ((list1[index] == list2[list2index]) and ((list2index+1) < list2length)):
                list2index += 1
            elif ((list1[index] == list2[list2index]) and ((list2index+1 >= list2length))):
                return True
            else:
                list2index = 0
        return False

def is_sublist(list1,list2):
    if (not list1):
        return True
    else:
        return is_superlist(list2,list1)
