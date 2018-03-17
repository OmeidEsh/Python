#ForDictionary

dict={"key1":"Value1",   "key2":"Value2",   "key3":"Value3"}
print(dict)
print("\n")

for key in dict:
	print("for key in dict: ", dict[key])
print("\n")

for key,value in dict.items():
	print("for key,value in dict.items(): ", key,value)
print("\n")

for val in dict.values():
	print("for val in dict.values(): ", val)
print("\n")

for key in dict.keys():
	print("for key in dict.keys(): ", key)
print("\n")	