'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 14/10/16
DESCRIPTION:
'''

import argparse

from src.fileRead import getData
from src.Task1 import firstComeFirstServeScheduler
from src.Task2 import roundRobinScheduler
from src.Task3 import shortestRemainingTimeScheduling
from src.testing import test

def main():
    parser = argparse.ArgumentParser(description="Evaluate the performance of differnt scheduling algorithms")
    parser.add_argument('--input-file', dest='input_file', required=True)
    args = parser.parse_args()

    processArray = getData(args.input_file)
    print("--TESTING----")
    test()

    print("------Original Input--------")
    for process in processArray:
        print(process.stringify())

    print("------FCFSS Output--------")
    FCFSscheduler = firstComeFirstServeScheduler(processArray)
    while (not FCFSscheduler.isFinished()):
        FCFSscheduler.tick()

    for process in FCFSscheduler.finishedArray:
        print(process.stringify())

    print("------Original Input--------")
    for process in processArray:
        print(process.stringify())

    print("------Other version Output--------")
    RRscheduler = roundRobinScheduler(processArray)
    while (not RRscheduler.isFinished()):
        RRscheduler.tick()

    for process in RRscheduler.finishedArray:
        print(process.stringify())
'''
    print("------SRTS Output--------")
    SRTSarray = shortestRemainingTimeScheduling(processArray)
    for process in SRTSarray:
        print(process.stringify())

'''


if __name__ == '__main__':
    main()
