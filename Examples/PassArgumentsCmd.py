#Pass arguments from Cmd line:

import sys
print ("Number of arguments: ", len(sys.argv), "arguements.")
print ("Argument List: ", str(sys.argv))
x=int (sys.argv[1])
y=int (sys.argv[2])
z=x+y
print (x, "+", y, "=", z)


#in command line:
#C:\Users\Omeid\Desktop\Python>PassArgumentsCmd.py 1 2
#1 + 2 = 3