Tested on the flip server, using python 3.6.6.

NUM_PAIRS is the number of points.

Create test inputs:
python36 create_test_inputs.py $NUM_PAIRS

Brute force:
python36 brute_force.py $INPUT_FILE $OUTPUT_FILE
Output goes to $OUTPUT_FILE.

Naive Divide and Conquer:
python36 naivednc.py $INPUT_FILE
Output goes to naivednc-output.txt.

Enhanced Divide and Conquer:
python36 enhanceddnc.py $INPUT_FILE
Output goes to enhanced-dnc-output.txt.
