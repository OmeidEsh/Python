#Functions:

import time
start_time = time.time()
print("time: ", time.asctime())
print("\n")


##############################################################################
c=0
def sum(a,b):
	#print("c_inside_beforeAdd = ", c)
	c=a+b
	print("c_inside_afterAdd = ", c)
	return c

sum(3,11)
print("c_outside_afterFunc = ", c)	





##############################################################################
### The id stays the same, and the parameter is changed globaly as soon as we change it. 
def changeme(mylist):
	print("\t mylist_inFunc_BeforeInsert = ", mylist)
	print("\t mylist_inFunc_id_BeforeInsert = ", id(mylist))
	
	mylist[2]=500 ### This will change the array's element inside and outside and it's not a local var.
	mylist=20000  ### But this is will generate a local var. and it will not effect the "arrey" list!
	mylist=[201,202,203,204] ### Same as above, doesn't change the variables. 
	
	print("\t mylist_inFunc_AfterInsert = ", mylist)
	print("\t mylist_inFunc_id_AfterInsert = ", id(mylist))
	return 



mylist = [1, 2, 3]
print("mylist_BeforeFunc = ", mylist)
print("mylist_id_BeforeFunc", id(mylist))

print("\n")
changeme(mylist)
print("\n")

print("mylist_AfterFunc = ", mylist)
print("mylist_id_AfterFunc = ", id(mylist))





##############################################################################








print("\n")
print("\n")
print("--- %s seconds ---" % (time.time() - start_time), "(time.time() - start_time)")
print("--- %s seconds ---" % time.clock(), "time.clock()")