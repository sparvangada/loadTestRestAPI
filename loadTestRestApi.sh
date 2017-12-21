#!/bin/bash

    counter=0
    
    [ $# -eq 0 ] && { echo "Usage: $0 number_of_parallel_runs" >> bash.out;exit 1; }

 	
    while [ $1 -gt $counter ]
    do
    	echo "calling restApi iteration....$counter" >> bash.out
    	python -u restApi.py & 
    	((counter=counter +1))
    done
    echo All done
