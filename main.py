'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: This is the main entry point for the program, it collects the input
data from the input file given by the command line argument, then feeds the
data into the 3 different scheduling algorithms to see how they perform differently
'''

import argparse

from src.fileRead import getData
from src.Task1 import firstComeFirstServeScheduler
from src.Task2 import roundRobinScheduler
from src.Task3 import shortestRemainingTimeScheduler
from src.testing import test

def main():
    parser = argparse.ArgumentParser(description="Evaluate the performance of differnt scheduling algorithms")
    parser.add_argument('--input-file', dest='input_file', required=True)
    args = parser.parse_args()

    processArray = getData(args.input_file)


    print("------Original Input--------")
    for process in processArray:
        print(process.stringify())

    print("------FCFSS Output--------")
    FCFSscheduler = firstComeFirstServeScheduler(processArray)
    while (not FCFSscheduler.isFinished()):
        FCFSscheduler.tick()

    for process in FCFSscheduler.finishedArray:
        print(process.stringify())

    print("AVERAGE TURNAROUND TIME: " + str(FCFSscheduler.getAvgTurnaroundTime()))
    print("AVERAGE WAITING TIME: " + str(FCFSscheduler.getAvgWaitingTime()))
    print("THROUGHPUT: " + str(FCFSscheduler.getThroughput()))

    print("------RRS Output--------")
    RRscheduler = roundRobinScheduler(processArray)
    while (not RRscheduler.isFinished()):
        RRscheduler.tick()

    for process in RRscheduler.finishedArray:
        print(process.stringify())

    print("AVERAGE TURNAROUND TIME: " + str(RRscheduler.getAvgTurnaroundTime()))
    print("AVERAGE WAITING TIME: " + str(RRscheduler.getAvgWaitingTime()))
    print("THROUGHPUT: " + str(RRscheduler.getThroughput()))

    print("------SRTS Output--------")
    SRTscheduler = shortestRemainingTimeScheduler(processArray)
    while (not SRTscheduler.isFinished()):
        SRTscheduler.tick()

    for process in SRTscheduler.finishedArray:
        print(process.stringify())

    print("AVERAGE TURNAROUND TIME: " + str(SRTscheduler.getAvgTurnaroundTime()))
    print("AVERAGE WAITING TIME: " + str(SRTscheduler.getAvgWaitingTime()))
    print("THROUGHPUT: " + str(SRTscheduler.getThroughput()))




if __name__ == '__main__':
    main()
