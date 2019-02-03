#/bin/bash

for i in 100 1000 10000
do
	for j in {1..10}
	do
		echo "trial no, time" > trial_$i.csv
		python3 ./create_test_inputs.py $i
		time=$( { /usr/bin/time -f %e python3 ./brute_force.py testinput-$i testouput-$i ; } 2>&1 )
		echo "$j,$time"
		echo "$j,$time" >> "trial_$i.csv"
	done	
done
