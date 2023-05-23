1) pwd
The pwd command writes to standard output the full path name of your current directory
$ pwd
................................wildcards in unix..............................
* – This wildcard represents all the characters
? – This wildcard represents a single character
[] – This wildcard represents a range of characters.

q) it will search for characters starting with S and ending with f and exactly one character in between them.
$ ls A?f

q)  S**n will match anything between S and n. The number of characters between them do not count.
$ ls A*f

q) that files starting with ‘A’ followed by a range of characters from b to c 
and ending with f 
$ ls A[b-c]f

Combination of all wildcards

q) one character and any number of characters are displayed with ending characters as f
ls -l ?*f

...................................Pipes and Filters in unix..............................

Pipe is used to combine two or more commands, and in this, the output of one command 
acts as input to another command,
 and this command’s output may act as input to the next
 command and so on. It can also be visualized as a temporary connection between two or 
 more commands/ programs/ processes. The command line programs that do the further
  processing are referred to as filters. 

Syntax : 
command_1 | command_2 | command_3 | .... | command_N 

1. Listing all files and directories and give it as input to more command. 
$ ls -l | more 

2. count the line no of a file
$ cat abc | wc -l

------------------------------cut command---------------------
 Basically the cut command slices a line and extracts the text. 
 It is necessary to specify option with command otherwise it gives error. 
 If more than one file name is provided then data from each file is not precedes by
  its file name.

Syntax:
cut OPTION... [FILE]...

abc.txt
name|roll|dept
sumit|51|MCA
amit|20|BCA
dulal|52|Mtech

q) in the following show all the deperments
$ cut -d "|" -f3 abc.txt
OP:
dept
MCA
BCA
Mtech

