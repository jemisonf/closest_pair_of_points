#/bin/bash

for i in {1..10}
do
    python36 ./create_test_inputs.py 1000 testinput-1000-$i
    { time python36 ./brute_force.py testinput-1000-$i testoutput-1000-$i & } 2> testoutput-time-1000-$i
done
