#RandomeNumberFunc

import random

#choice() Function
print("randome number from range(100) : ", random.choice(range(100)))
list=[1,2,3,5,9]
print("randome element from list : ", random.choice(list))
str="Hello World"
print("randome character from string : ", random.choice(str))
print("\n")

#randrange() Function
print("randrange(1, 100, 2) : ", random.randrange(1, 100, 2))
print("randrange(100) : ", random.randrange(100))
print("\n")

#random() Function
print("1st random() : ", random.random())
print("2nd random() : ", random.random())
print("\n")

#seed() Function

# import random
# random.seed( 3 )
# print "Random number with seed 3 : ", random.random() #will generate a random number 
# #if you want to use the same random number once again in your program
# random.seed( 3 )
# random.random()   # same random number as before

random.seed()
print("random number with defult seed", random.random())
random.seed(10)
print("random number with int seed", random.random())
random.seed("hello", 2)
print("random number with str seed", random.random())
print("\n")

#shyffle() Functuon
list = [20,16,10,5]
random.shuffle(list)
print("Reshuffled list : ", list)
print("\n")

#uniform() Function:
print("Random Float Uniform(5,10) : ", random.uniform(5,10)) #lower=5 upper=10
print("\n")
####For some reason, i get the same number from the uniform code above
#### 5.255433459829996
#### but on terminal, it works fine.