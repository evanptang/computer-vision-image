import check_functions
import cgi, cgitb


#This file is solely for the checking of solutions. There are no functions defined here,
#simply calls the functions as previously defined.

form = cgi.FieldStorage()
value = form.getvalue('cases3')

print "Content-type:text/html\r\n"
#print "DEBUG"
if value == "0":
    num = check_functions.check_circles("Circles 1","images/circles1.bmp")
    print num
elif value == "1":
    num = check_functions.check_circles("Circles 2","images/circles2.bmp")
    print num
elif value == "2":
    num = check_functions.check_circles("Circles 3","images/circles3.bmp")
    print num
elif value == "3":
    num = check_functions.check_circles("Circles 4","images/circles4.bmp")
    print num
elif value =="4":
    pair = check_functions.check_slopeintercept("Line 1","images/line1.bmp")
    print pair[0]
    print pair[1]
elif value == "5":
    pair = check_functions.check_slopeintercept("Line 2","images/line2.bmp")
    print pair[0]
    print pair[1]
elif value == "6":
    pair = check_functions.check_slopeintercept("Line 3","images/line3.bmp")
    print pair[0]
    print pair[1]
elif value == "7":
    pair = check_functions.check_slopeintercept("Line 4","images/line4.bmp")
    print pair[0]
    print pair[1]
elif value == "8":
    pair = check_functions.check_normal("Line 5","images/line5.bmp")
    print pair[0]
    print pair[1]
elif value == "9":
    pair = check_functions.check_normal("Line 6","images/line6.bmp")
    print pair[0]
    print pair[1]
elif value == "10":
    pair = check_functions.check_normal("Line 7","images/line7.bmp")
    print pair[0]
    print pair[1]
elif value == "11":
    pair = check_functions.check_normal("Line 8","images/line8.bmp")
    print pair[0]
    print pair[1]
