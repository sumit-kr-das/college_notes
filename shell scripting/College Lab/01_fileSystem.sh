ls - command in unix
ls refers to List information about the FILEs, 
and it represemts the current directory by default
Syatax: ls [OPTION]... [FILE]... 

a)Listing Files with ls command without any arguments
$ ls
b)Listing files in reverse order
$ ls -r
c)Listing file and directory permissions with -l option
$ ls -l
d)Viewing files in a human-readable format
$ ls -lh
e)Viewing Hidden files
$ ls -a
f)Displaying the inode number of files and directories
$ ls -i
g) Displaying the UID & GID of files and directories
$ ls -n
............................................................................
cd - linux command
To change directory - change the current working directory to a specific Folder.
Syntax: cd [Options] [Directory]
a) navigate to any path
$cd path/to/directory
...............................................................................
cat
cat - concatenate files and print the content on standard output.
syntax: cat [OPTION]... [FILE]...
a)List contents of file1 on stdout
$ cat file1
b)List the contents of file1 and file2 together on stdout
$ cat file1 file2
c)Copy contents of file1 and file2 to file3
$ cat file1 file2 > file3
d)Append contents of file1 and file2 to file4
$ cat file1 file2 >> file4
.............................................................................
man
man it is the interface used to view the system's reference manuals.
syntax: man [file]
...............................................................................
wc 
wc - print newline count, word count and byte count for each file.
syntax: 
wc [OPTION]... [FILE]...
wc [OPTION]... --files0-from=F

a)Display count information of a file
$wc code.txt
b)Display count information of multiple files
$wc exam.txt marks.txt  
