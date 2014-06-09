import time

from Benchmark_Cyclone import ServerSetup as CycloneMain
from Benchmark_Tornado import ServerSetup as TornadoMain
from Benchmark_Twisted import ServerSetup as TwistedMain



def test_module(library):
    times = []
    port = 8020
    NumberOfIterations = 1

    for x in range(0, NumberOfIterations):

        startTime = time.time()

        library(port)

        stopTime = time.time()

        difference = (stopTime - startTime)
        times.append(difference)
        port += 1

    average = sum(times) / len(times)

    print 'From setup to teardown, it took: ' + str(average) + ' seconds.\n'
    print '=========================================\n'

test_module()