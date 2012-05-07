=====
GPerf
=====

Graphing performance or system activity information.

using the output of ``sar`` tools.



Requirements
============

- matplotlib


How to use
==========

::

    Usage: gperf.py [options]

    Options:
      -h, --help            show this help message and exit
      -i INPUT_FILE, --input=INPUT_FILE
      -o OUTPUT_DIR, --ouput=OUTPUT_DIR
      --csv                 
      --stat                
      --minor               
      --height=HEIGHT       
      --width=WIDTH   


Recording all system activity.
::
    
    $ sar -A -o [output filename] [interval]

    $ sar -A -o activity_result 1


Convert result format into csv.
::
    
    $ sadf -d -- -A [output filename] > [csv filename]

    $ sadf -d -- -A activity_result > activity_result.csv

Create graph form ``-d`` format form sadf.
::

    $ python gperf.py -i activity_result.csv -o output_dir

    or

    $ python gperf.py --input activity_result.csv --output output_dir
