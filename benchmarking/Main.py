from invoke import run
import time
from numpy import *

IterationNumber = 1


SetupStartFile = open('SetupStartTime.txt', 'rw')
TeardownStopFile = open('TeardownStopTime.txt', 'rw')

#===================================================
for x in range(0, IterationNumber):

    SetupStartTime = time.time()
    SetupStartFile.writelines(SetupStartTime)
    run('python ../Benchmark_Cyclone.py')

    TeardownStopTime = time.time()
    TeardownStopFile.writelines(TeardownStopTime)

#===================================================

SetupStopFile = open('SetupStopTime.txt', 'r')
MessageStartFile = open('MessageStartTime.txt', 'r')
MessageStopFile = open('MessageStopTime.txt', 'r')
TeardownStartFile = open('TeardownStartTime', 'r')

s_start = []
s_stop = []
m_start = []
m_stop = []
t_start = []
t_stop = []

for y in range(0, IterationNumber):
    s_start.append(SetupStartFile.readline())
    s_stop.append(SetupStopFile.readline())

    m_start.append(MessageStartFile.readline())
    m_stop.append(MessageStopFile.readline())

    t_start.append(TeardownStartFile.readline())
    t_stop.append(TeardownStopFile.readline())

s_start = array(s_start)
s_stop = array[s_stop]
m_start = array[m_start]
m_stop = array[m_stop]
t_start = array[t_start]
t_stop = array[t_stop]

s_dif = (s_stop - s_start)
m_dif = (m_stop - m_start)
t_dif = (t_stop - t_start)

s_dif