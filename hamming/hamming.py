def distance(str1, str2):
    count = 0;
    str1length = len(str1);
    str2length = len(str2);
    if (str1length != str2length):
        print "Nothing to do, they are not the same length"
    else:
        for index in range(str1length):
            if (str1[index] != str2[index]):
                count += 1;
    print count
    return count;
