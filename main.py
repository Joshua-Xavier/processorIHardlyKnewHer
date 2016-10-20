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

def main():
    '''we define the cmd line arg here to select file for input'''
    parser = argparse.ArgumentParser(description="Evaluate the performance of differnt scheduling algorithms")
    parser.add_argument('--input-file', dest='input_file', required=True)
    args = parser.parse_args()

    processArray = getData(args.input_file)

    '''We define the various scheduling run functions here for the simulation'''
    def inputDescription():
        print("------Original Input--------")
        for process in processArray:
            print(process.stringify())

    def fcfsDescription(detailed_output):
        print("\n------FCFSS Output--------")
        FCFSscheduler = firstComeFirstServeScheduler(processArray)
        while (not FCFSscheduler.isFinished()):
            FCFSscheduler.tick(detailed_output)

        for process in FCFSscheduler.finishedArray:
            print("Process: " + process.getID()
            + " Turnaround Time: " + str(process.getTurnAroundTime())
            + " Waiting Time: " + str(process.getWaitingTime()))

        print("\nAVERAGE TURNAROUND TIME: " + str(FCFSscheduler.getAvgTurnaroundTime()))
        print("AVERAGE WAITING TIME: " + str(FCFSscheduler.getAvgWaitingTime()))
        print("THROUGHPUT: " + str(FCFSscheduler.getThroughput()))

    def rrDescription(detailed_output):
        print("\n------RRS Output--------")
        RRscheduler = roundRobinScheduler(processArray)
        while (not RRscheduler.isFinished()):
            RRscheduler.tick(detailed_output)

        for process in RRscheduler.finishedArray:
            print("Process: " + process.getID()
            + " Turnaround Time: " + str(process.getTurnAroundTime())
            + " Waiting Time: " + str(process.getWaitingTime()))


        print("\nAVERAGE TURNAROUND TIME: " + str(RRscheduler.getAvgTurnaroundTime()))
        print("AVERAGE WAITING TIME: " + str(RRscheduler.getAvgWaitingTime()))
        print("THROUGHPUT: " + str(RRscheduler.getThroughput()))

    def srtDescription(detailed_output):
        print("\n------SRTS Output--------")
        SRTscheduler = shortestRemainingTimeScheduler(processArray)
        while (not SRTscheduler.isFinished()):
            SRTscheduler.tick(detailed_output)

        for process in SRTscheduler.finishedArray:
            print("Process: " + process.getID()
            + " Turnaround Time: " + str(process.getTurnAroundTime())
            + " Waiting Time: " + str(process.getWaitingTime()))

        print("\nAVERAGE TURNAROUND TIME: " + str(SRTscheduler.getAvgTurnaroundTime()))
        print("AVERAGE WAITING TIME: " + str(SRTscheduler.getAvgWaitingTime()))
        print("THROUGHPUT: " + str(SRTscheduler.getThroughput()))


    '''Below here we have the main program menu that lets you select which
    scheduling algorithm you want to run'''

    print("0. Run all 3 scheduling algorithms\n1. First come first serve\n2. Round robin scheduling\n3.Shortest time remaining")
    valid_cmd = False
    while (not valid_cmd):
        valid_cmd = True
        cmd = input("Please enter what type of scheduling you want to run: ")
        detailed_output = False
        d_o = input("Would you like to print out process traces? (y/n): ")
        # defaults to no if user does not enter y
        if(d_o == "y" or d_o == "Y"):
            detailed_output = True

        if(cmd == "0"):

            inputDescription()
            fcfsDescription(detailed_output)
            rrDescription(detailed_output)
            srtDescription(detailed_output)

        elif(cmd == "1"):
            inputDescription()
            fcfsDescription(detailed_output)

        elif(cmd == "2"):
            inputDescription()
            rrDescription(detailed_output)

        elif(cmd == "3"):
            inputDescription()
            srtDescription(detailed_output)

        else:
            print("Invalid cmd entered, please choose from menu. 0, 1, 2 or 3\n")
            valid_cmd = False





if __name__ == '__main__':
    main()
