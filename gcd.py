side1 = 8
side2 = 12 

def pack(side1, side2):

    print('====== Packing (%s x %s) ======' % (side1, side2))
    # make a square using the smallest side.
    shortSide = side1
    longSide = side2

    if (side2 < side1):
        shortSide = side2
        longSide = side1

    print('Long side: %d' % (longSide))
    print('Short side: %d' % (shortSide))

    remainder = longSide % shortSide
    print('Total Blocks: (%d x %d): %d' % (shortSide, shortSide, longSide / shortSide))

    if (remainder == 0):
        print('Remainder: 0')
        print('GCD: %d' % (shortSide))
        return

    print('Remainder: 1 x (%s x %d) block' % (remainder, shortSide))
    return pack(shortSide, remainder)

pack(side1, side2)
