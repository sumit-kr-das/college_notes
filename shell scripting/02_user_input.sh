#! /bin/bash

echo "Enter your name & roll numbers: "
read name roll
echo Entered name is $name and roll is $roll

# => input at the same prompt / line
read -p "username: " user_var
echo "username: $user_var"

# => hidden/silent input prompt 
read -sp "password: " user_pass
echo "password: $user_pass"

# => input like an array
echo "Enter multiple names: "
read -a user_names
echo "Names ia ${user_names[0]}, ${user_names[1]}"

# => input without storing inside a variable
echo "Enter name: "
read
echo "Name without variable is $REPLY"