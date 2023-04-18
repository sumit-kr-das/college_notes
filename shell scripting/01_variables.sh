# $ cat /etc/shells
#! /bin/bash

echo "Variables in shell shripting"

# 1) System Variables. Maintained by Unix
# 2) User Defined Variables. Created or Maintained by us

# => example of some system variables
echo "-------------------example of some system variables-----------------------"
echo Bash name $BASH
echo Bash version $BASH_VERSION
echo Home directory $HOME
echo Present working directory $PWD

# => example of some user defined variables
echo "-------------------example of some user defined variables-----------------------"
name=sumit
roll=51
echo My name is $name and roll $roll