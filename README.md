***FilePrefixAppender***

Python Based Script to Add Prefix to all the Files present in a directory:  

This Script adds the prefix to all files present in the path specified, i.e. recursively traverses all the file and adds the prefix.  

The **Syntax** to use the script is:  
python script.py <Path of Directory> <Prefix with which you want all the files to get appended with>  

**Important point to Note:**  
Do not space in <Path of Directory> or <Prefix>. The script is not yet modified to deal with those stuff.  

P.S. In case you have space in your main directory and it's not possible to remove that, you can symlink another directory to it.  
Syntax: ln -s <New Directory> <Directory you want to symlink to>  
