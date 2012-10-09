#!/bin/bash

# This one is to briefly test your bash scripting skills. Please write a set of commands that would perform following procedure:

#     find files in some directory, but not deeper than 2 directories
#     files should be recent, changed 2 days ago max
#     for each file, do an in-place change, adding tab to the end of every line
#     print file size before and after the tab addition

usage(){
	echo "Usage: $0 dirname"
	exit 1
}

[[ $# -eq 0 ]] && usage
if [ ! -d "$1" ] ; then
    echo "$1: No such directory." 2>&1
    usage                
fi 

files(){
 find $1 -maxdepth 2 -type f -mtime -2 -printf "%p\t%s\n" 
}

#It is simpler to print size directly in 'find' command via 'printf' argument,
#but 'awk' is used only to show my ability to use various built-in programs.
files | awk -F '\t' '
	{ s += $2 } 
	{ print $1, $2, "\t"}
	END { print "---\nTotal size:", s }'

