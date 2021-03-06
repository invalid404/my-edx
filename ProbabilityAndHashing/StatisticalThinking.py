__author__ = 'aDmin'

import random
import pylab

def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)
    allLen = 0.0
    if (len(L) == 0):
        return float('NaN')

    for str in L:
        allLen += len(str)

    mean = allLen / N
    s = 0.0
    for str in L:
        s += (len(str) - mean) ** 2

    return (s / N) ** 0.5

def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)

    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))

    pylab.title('Difference between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(Heads - Tails)')
    pylab.plot(xAxis,diffs)

    pylab.figure()
    pylab.title('Heads/Tails ratio')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis,ratios)

    #Additional code to produce different plots from the same data
    pylab.figure()
    pylab.title('Difference between Hads and Tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'o')
    pylab.semilogx()
    pylab.semilogy()

    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios, 'o')
    pylab.semilogx()

def stdDev(data):
    mean = sum(data)/float(len(data))
    tot = 0.0
    for val in data:
        tot += (val - mean)**2

    return (tot / len(data))**0.5

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1

    numTails = numFlips - numHeads
    return numHeads, numTails

def flipPlot2(minExp, maxExp, numTrials):
    meanRatios, meanDiffs, ratiosSDs, diffsSDs = [],[],[],[]
    xAxis = []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [],[]
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads-numTails))

        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))

    pylab.plot(xAxis, meanRatios,'o')
    pylab.title('Mean Heads/Tails ratios ('
                + str(numTrials) + 'Trails)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()

    pylab.figure()
    pylab.plot(xAxis, ratiosSDs, 'o')
    pylab.title('SD Head/Tails Ratios ('
                + str(numTrials) + 'Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard deviation')
    pylab.semilogx()
    pylab.semilogy()

    pylab.figure()
    pylab.title('Mean abs(#Heads - #Tails) ('
                + str(numTrials) + 'Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean abs(#Heads - #Tails)')
    pylab.plot(xAxis, meanDiffs,'o')
    pylab.semilogx()
    pylab.semilogy()

    pylab.figure()
    pylab.title('SD abs(#Heads - #Tails) ('
                + str(numTrials) + 'Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('SD of Diffs')
    pylab.plot(xAxis,diffsSDs,'o')
    pylab.semilogx()
    pylab.semilogy()


def main():
    # print 'Standard deviation of [a, z, p] is',\
    #     str(stdDevOfLengths(['a', 'z', 'p']))
    # print 'Standard deviation of [apples, oranges, kiwis, pineapples] is',\
    #     str(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))

    random.seed(2)
    # flipPlot(4, 20)
    flipPlot2(4, 20, 20)
    pylab.show()

if __name__ == '__main__':
    main()

