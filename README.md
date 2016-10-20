# FIT2070 Assignment 3
##### Josh Nelsson-Smith
##### 21/09/16
--
## Installing the program
Start by downloading and unzipping the file named '25954113_A3.zip', once
unzipped you should see a folder that contains the following files:

```
25954113_A3
├── README.pdf
├── Task_4.pdf
├── compileScript.sh
├── input
│   └── processes.txt
├── main.py
├── output
│   ├── 1a.txt
│   ├── 1b.txt
│   ├── 1c.txt
│   ├── 1d.txt
│   ├── 1e.txt
│   └── lecture_test.txt
└── src
    ├── Process.py
    ├── Queue.py
    ├── Scheduler.py
    ├── Task1.py
    ├── Task2.py
    ├── Task3.py
    ├── __init__.py
    └── fileRead.py

3 directories, 19 files
```
The `src` directory contains the various python files that are used to create the
program. `Process.py` contains the code for a class that represents a Process object.
The `Queue.py` file contains similar code for a queue class that is used by the
various scheduling algorithms. `Scheduler.py` is a Scheduler class that operates
on the input processes and simulates the scheduling of them. `Task1.py`, `Task2.py` and `Task3.py`
contain the subclasses of the scheduler inherit from the scheduler and implement their own
`tick` function. `fileRead.py` handles the processing of the input file containing the
information about the process stream file the user feeds the program. The main entry for the program is the `main.py` file that we will use
to run the program. Note that to use this program you have python 3 installed on
your machine.

## Setting up the program

- to input data you should create a text file of the form
ProcessName processArrivalTime processDuration

For instance the included one, located in `input/processes.txt` is:

```
P1 0 3
P2 1 6
P3 4 4
P4 6 2
```
Using the program requires running `main.py` and feeding it a required
argument `--input-file="yourPathHere/yourFile.txt"`.
For instance, to run the program with the example `processes.txt` file we would
write:

```sh
python3 main.py --input-file="input/processes.txt"
```

You should notice you can just edit `input/processes.txt` if you want to make your life a little easier.

Further more to this I suggest running `compileScript.sh` which is a shell
script that runs the above line by default. If you want to run it simply type:

```sh
$ ./compileScript.sh  
```
ensuring that the correct permissions are enabled for the file to execute.


## The program
The program serves as a simulation of a few different types of scheduling
algorithms.
First come first serve scheduling, wherein the processes are serviced according
to the order in which they arrive. Round robin scheduling, where processes go
into a queue after they arrive and get a set time slice each before going to
the back of the queue (in this implementation the time slice is set to 2).
And finally shortest remaining time scheduling where the process with the
shortest remaining time is scheduled to execute at any time.

When running the program you will be presented with a menu to decide what you want to run:
```
0. Run all 3 scheduling algorithms
1. First come first serve
2. Round robin scheduling
3.Shortest time remaining
Please enter what type of scheduling you want to run:
```
After selecting your choice you will also be asked whether you want to show
the process traces:
```
Would you like to print out process traces? (y/n):
```
Typing 'y' will enable this so that the program outputs which process is
running at any given time interval and at what stage of its completion it is at.
This is useful for debugging purposes or ensuring the processes are being served
in the correct order.

After entering these choices the program will output the
individual processes' turnaround and waiting times, as well as the average turnaround time, average waiting time and overall throughput.
