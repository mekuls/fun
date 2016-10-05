isSorted  = False

theList = [3, 2000, 500, 450, 300, 200, 1]
print('List: %s' % ', '.join(str(x) for x in theList))

while isSorted == False:

    isSorted = True
    for i in range(0, len(theList) - 1):

        if theList[i] > theList[i + 1]:
            temp = theList[i + 1]
            theList[i + 1] = theList[i]
            theList[i] = temp
            print('List: %s' % ', '.join(str(x) for x in theList))

            isSorted = False


print('List: %s' % ', '.join(str(x) for x in theList))
