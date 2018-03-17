#DictionaryFun

#clear():
print("clear() method:")
dict0={'Name':'Omeid', 'Age':27}
print("dict0 = ", dict0)
print("len(dict0) = ", len(dict0))
dict0.clear()
print("dict.clear()")
print("dict0 = ", dict0)
print("len(dict0) = ", len(dict0))
print("\n")

#copy():
print("copy() method:")
dict1= {'subjects':['phy', 'che']}
dict2= dict1.copy()
print("dict2 = dict1.copy() =  ", dict2)
print("\n")

#dict2.append():
print("dict2['subjects'].append('maths')")
dict2['subjects'].append('maths')
#As you'll see, when we append something to dict1, dict2 changes as well.
#this is because of the "shallow copy".
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print("\n")

#fromkeys():
print("fromkeys() method:")
seq = ('name', 'age', 'sex') ###MAKE SURE IT'S A TUPLE!!! Since they are the keys.
dict0 = dict0.fromkeys(seq) #values optional
print('dict0.fromkeys(seq) = ', dict0)
dict0 = dict0.fromkeys(seq, 10)
print('dict0.fromkeys(seq, 10) = ', dict0)
#assign all the "key's (left)" with a 10 as their "value (right)".
print("\n")

#get():
print("get() method: ")
dict0 = {'Name':'Omeid', 'Age':'27'}
print("dict0 = ", dict0)
print("dict0.get('Age') = ", dict0.get('Age'))
print("dict0.get('Sex') = ", dict0.get('Sex'))
print("\n")

#items():
print("items() method:")
print("dict0.items() = ", dict0.items())
print("\n")

#keys():
print("keys() method: ")
dict0 = {'Name':'Omeid', 'Age':27}
print("dict.keys() = ", dict0.keys())
print("\n")

#values():
print("values() method: ")
print("dict0.values() = ", dict0.values())
print("\n")

#setdefault():
print("setdefault() method: ")
print("dict0.setdefault('class', None) = ", dict0.setdefault("class", None)) #if this key doesn't exist, it will creat a new one called class.
print("dict0.setdefault('Age', 100) = ", dict0.setdefault("Age", 100))
print("dict0 = ", dict0)
print("\n")

#update():
print("update() method")
dict0 = {'Name':'Alen', 'Age':7}
dict1 = {'Sex':'male'}
print("dict0 = ", dict0, "\n", "dict1 = ", dict1)
dict0.update(dict1)
print("dict0.update(dict1)")
print("dict0 = ", dict0)
print("\n")