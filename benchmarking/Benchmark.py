from Benchmark_Cyclone import ServerSetup as CycloneMain
from Benchmark_Tornado import ServerSetup as TornadoMain
from Benchmark_Twisted import ServerSetup as TwistedMain

#TornadoMain(8000)

TwistedMain(8020)

CycloneMain(8010)


