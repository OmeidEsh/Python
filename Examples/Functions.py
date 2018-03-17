#Functions:

import time
start_time = time.time()
print("time: ", time.asctime())
print("\n")




### The id stays the same, and the parameter is changed globaly as soon as we change it. 
def changeme(mylist):
	print("\t mylist_inFunc_BeforeInsert = ", mylist)
	print("\t mylist_inFunc_id_BeforeInsert = ", id(mylist))
	mylist[2]=500 ### This will change the array's element inside and outside and it's not a local var.
	mylist=20000    ### But this is will generate a local var. and it will not effect the "arrey" list!
	print("\t mylist_inFunc_AfterInsert = ", mylist)
	print("\t mylist_inFunc_id_AfterInsert = ", id(mylist))
	return mylist



# ###(same as ^) The id stays the same, and the parameter is changed globaly as soon as we change it. 
# def changeme(gooz):
# 	print("\t mylist_inFunc_BeforeInsert = ", gooz)
# 	print("\t mylist_inFunc_id_BeforeInsert = ", id(gooz))
# 	gooz[2]=500
# 	print("\t mylist_inFunc_AfterInsert = ", gooz)
# 	print("\t mylist_inFunc_id_AfterInsert = ", id(gooz))
# 	return



# ###When we set the parameter =  to something new INSIDE the function, it creates a new id that
# ###independent of the outside id. Also, when we change the values of the parameter, the outside
# ###parameter doesn't change. 
# def changeme(mylist):
# 	print("Changed mylist inside the Functions")
# 	mylist = [10, 20, 30]
# 	print("\t mylist_inFunc_BeforeInsert = ", mylist)
# 	print("\t mylist_inFunc_id_BeforeInsert = ", id(mylist))
# 	mylist[2]=500
# 	print("\t mylist_inFunc_AfterInsert = ", mylist)
# 	print("\t mylist_inFunc_id_AfterInsert = ", id(mylist))
# 	return



# def changeme(mylist):
# 	print("Changed mylist inside the Functions")
	
# 	inFunc_mylist = mylist #same id's inside & outside the function.
# 	#inFunc_mylist = [10, 20, 30]

# 	print("\t inFunc_mylist_inFunc_BeforeInsert = ", inFunc_mylist)
# 	print("\t inFunc_mylist_inFunc_id_BeforeInsert = ", id(inFunc_mylist))
# 	inFunc_mylist[2]=500
# 	print("\t inFunc_mylist_inFunc_AfterInsert = ", inFunc_mylist)
# 	print("\t inFunc_mylist_inFunc_id_AfterInsert = ", id(inFunc_mylist))
# 	print("\t mylist_inFunc_AfterInsert = ", mylist)
# 	print("\t mylist_inFunc_id_AfterInsert = ", id(mylist))
# 	#mylist = inFunc_mylist
# 	return 




mylist = [1, 2, 3]
print("mylist_BeforeFunc = ", mylist)
print("mylist_id_BeforeFunc", id(mylist))

print("\n")
changeme(mylist)
print("\n")

print("mylist_AfterFunc = ", mylist)
print("mylist_id_AfterFunc = ", id(mylist))


print("\n")
print("\n")
print("--- %s seconds ---" % (time.time() - start_time), "(time.time() - start_time)")
print("--- %s seconds ---" % time.clock(), "time.clock()")