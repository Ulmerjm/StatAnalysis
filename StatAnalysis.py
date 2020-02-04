import math


def determinecorrelation(listx, listy):
    """Determine correlation coefiicent R"""

    # Get standard deviation for both lists
    meanx = math.fsum(listx) / listx.count()
    meany = math.fsum(listy) / listy.count()
    sqrlistx = ()
    sqrlisty = ()

    for x in listx:
        sqrlistx.append((x - meanx) ** 2)

    for y in listy:
        sqrlisty.append((x - meany) ** 2)

    sqrmeanx = math.fsum(sqrlistx) / listx.count()
    sqrmeany = math.fsum(sqrlisty) / listy.count()

    stddevx = math.sqrt(sqrmeanx)
    stddevy = math.sqrt(sqrlisty)

    # Use standard deviation to determine correlation
    for x in listx:





