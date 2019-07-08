import check_functions

#This file is solely for the checking of solutions. There are no functions defined here,
#simply calls the functions as previously defined.

all_passed = True

all_passed = check_functions.check_slopeintercept("Line 1","images/line1.bmp") and all_passed
all_passed = check_functions.check_slopeintercept("Line 2","images/line2.bmp") and all_passed
all_passed = check_functions.check_slopeintercept("Line 3","images/line3.bmp") and all_passed
all_passed = check_functions.check_slopeintercept("Line 4","images/line4.bmp") and all_passed

all_passed = check_functions.check_normal("Line 5","images/line5.bmp") & all_passed
all_passed = check_functions.check_normal("Line 6","images/line6.bmp") & all_passed
all_passed = check_functions.check_normal("Line 7","images/line7.bmp") & all_passed
all_passed = check_functions.check_normal("Line 8","images/line8.bmp") & all_passed

all_passed = check_functions.check_circles("Circles 1","images/circles1.bmp") & all_passed
all_passed = check_functions.check_circles("Circles 2","images/circles2.bmp") & all_passed
all_passed = check_functions.check_circles("Circles 3","images/circles3.bmp") & all_passed
all_passed = check_functions.check_circles("Circles 4","images/circles4.bmp") & all_passed

if all_passed:
	exit(0)
else:
	exit(1)
