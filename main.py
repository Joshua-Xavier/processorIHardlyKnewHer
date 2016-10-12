'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 11/10/16
DESCRIPTION:
'''

import argparse

from src.fileRead import getData
from src.FCFSS import firstComeFirstServeScheduling


def main():
    parser = argparse.ArgumentParser(description="Evaluate the performance of differnt scheduling algorithms")
    parser.add_argument('--input-file', dest='input_file', required=True)
    args = parser.parse_args()

    processArray = getData(args.input_file)
    for process in processArray:
        print(process.stringify())
    print("-----------------")
    FCFSSarray = firstComeFirstServeScheduling(processArray)
    for process in FCFSSarray:
        print(process.stringify())



if __name__ == '__main__':
    main()
