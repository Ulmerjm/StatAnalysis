import math
import statistics
import numpy

def determinecorrelation(listx, listy):
    """Determine correlation coefiicent R"""

    # Get standard deviation for both lists
    meanx = sum(listx) / len(listx)
    meany = sum(listy) / len(listy)
    stddevx = statistics.stdev(listx, meanx)
    stddevy = statistics.stdev(test2, meany)

    covar = numpy.cov(listx, listy)[0][1]

    # Use Numpy to determine covariance and use our standard deviations
    return covar/(stddevy*stddevx)

test1 = [1, 2, 2, 3]
test2 = [1, 2, 3, 6]
print(determinecorrelation(test1, test2))








