!/bin/bash

command='code.py'
for d in */
do
    echo "$d"
    cd "$d"
    python3 code.py
    cd ..
done
