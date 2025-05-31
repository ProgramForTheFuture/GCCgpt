#!/bin/bash
# Written with the assistance of Claude 4 Sonnet
# Script to create toc.txt files for each directory under kb
# These files are used by build.sh and build.py to identify files to be concatenated

for dir in kb/*/; do
    if [ -d "$dir" ]; then
        cd "$dir"
	rm -f toc.txt
        ls *.txt 2>/dev/null | sed 's/^/- /' | sed 's/.txt$//' > toc.tx1
        mv toc.tx1 toc.txt
        pwd
        cd - > /dev/null
    fi
done

