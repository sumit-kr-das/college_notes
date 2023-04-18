#! /bin/bash
echo -e "Enter the name of file: \c"
read file_name

# -e exist or not
# -f file is exist and regular file or not
# -d directory is exist or not


if [ -e $file_name ]
then
    echo "$file_name is exist"
else
    echo "$file_name not found"
fi