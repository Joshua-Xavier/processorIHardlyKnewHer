# FIT2070 Assignment 3
##### Josh Nelsson-Smith
##### 16/09/16
--
## Installing the program
Start by downloading and unzipping the file named '25954113_A3.zip', once
unzipped you should see a folder that contains the following files:

```
TREE VIEW WILL GO HERE
```
The `src` directory contains the various python files that are used to create the
program. The main entry for the program is the `main.py` file that we will use
to run the program. Note that to use this program you have python 3 installed on
your machine.

## Using the program

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
Also if you would prefer to direct your output you can use something like
```sh
$ ./compileScript.sh > output/your_output_filename.txt
```

## The program
You will see after running the program it will output quite a lot of text.
It runs your input process file through 3 different scheduling algorithms.
First come first serve scheduling, wherein the processes are serviced according
to the order in which they arrive. Round robin scheduling, where processes go
into a queue after they arrive and get a set time slice each before going to
the back of the queue (in this implementation the time slice is set to 2).
And finally shortest remaining time scheduling where the process with the
shortest remaining time is scheduled to execute at any time. 

`src`
