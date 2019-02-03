INTERPRETER=python36
SIZE=100000

10runsbrute: brute_force.py
	for trial in 1 2 3 4 5 6 7 8 9 10 ; do \
	  $(INTERPRETER) create_test_inputs.py $(SIZE) ; \
		echo -n "Trial $$trial" >> brute_out ; \
		echo "Trial $$trial" ; \
	 	{ time $(INTERPRETER) brute_force.py testinput-$(SIZE) testoutput-$(SIZE) ; } 2>> brute_out ; \
	done

10runsnaive: naivednc.py
	for trial in 1 2 3 4 5 6 7 8 9 10 ; do \
	  $(INTERPRETER) create_test_inputs.py $(SIZE) ; \
		echo -n "Trial $$trial" >> naive_out ; \
		echo "Trial $$trial" ; \
	 	{ time $(INTERPRETER) naivednc.py testinput-$(SIZE) testoutput-$(SIZE) ; } 2>> naive_out ; \
	done

10runsenhanced: enhanced_dnc.py
	for trial in 1 2 3 4 5 6 7 8 9 10 ; do \
	  $(INTERPRETER) create_test_inputs.py $(SIZE) ; \
		echo -n "Trial $$trial" >> naive_out ; \
		echo "Trial $$trial" ; \
	 	{ time $(INTERPRETER) enhanced_dnc.py testinput-$(SIZE) testoutput-$(SIZE) ; } 2>> enhanced_out ; \
	done


clean:
	rm -f testinput*
	rm -f testoutput*
	rm -f enhanceddnc-output.txt
	rm -f naive_out
	rm -f brute_out
	rm -f enhanced_out
