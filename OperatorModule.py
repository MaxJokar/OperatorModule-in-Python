import operator
# print(dir(operator))

# print(operator.add(17,9))
# print(operator.sub(17,9))
# print(operator.mul(17,9))
# print(operator.truediv(17,9))
# print(operator.floordiv(17,9))
# print(operator.mod(17,9))  # remaining


# eq ge gt le lt
# print(operator.le(7,3))  # little or  equal   <=
# print(operator.ge(7,3)) greate or equal      >=
# print(operator.le(7,7))    equals or not "True or False" ==
# print(operator.gt(7,3))        >
# print(operator.lt(7,3))        <   is  7 smaller?


# not 
# print(operator.not_(False))
# print(operator.not_(34>5))



#rshift
#lshift or rshift  work in  2 base :
# print(operator.rshift(17,1))  #17 in binary in calculator is :8
# print(operator.lshift(17,1)) 



#contains
#contains:to check amount of  somehting  inside something else
# print(operator.contains("jhkjhk'jhjhgghgdtd","p"))
#Does  the letter  P exist in this  string? True or False
# print(operator.contains(str(2345),str(2)))
#integers are possible if we convert them into str



#delitem
# list1=[12,23,45,56,89,78,56,4]
# operator.delitem(list1,2)
# print(list1)
# deletes the index inside the  List1





#Countof
# To count amount of  numbers or  letters inside :
# print(operator.countOf([23,45,56,89,78,45,12,56],5))
 
# print(operator.countOf("uyd dfddfpo dfd w er gfd df","u"))



#itemgetter
#to get items from a  packages or iterable brings us ITEMs gets a list , tuple and brings items with this numbers Below
# list1=[23,56,78,45,89,45,56,89,4]
# getter=operator.itemgetter(1)
# print(getter(list1))  Brings the Items needed
# print(operator.itemgetter(1,5)(list1))



# list1=[23,56,78,45,89,45,56,89,4]
# tuple1=("Andy","Dany","George","Sandra")
# getter=operator.itemgetter(1,3)

# print(getter(list1))
# print(getter(tuple1))



# to sort  list of people base on their  items
people=[("Dany","Max",42),("Rony","Alex",16),("Rony","Alex",85)]
list1=[23,56,12,45,566,54,4,78]
# print(sorted(list1))
# print(sorted(people,key=operator.itemgetter(2)))
print(sorted(people,key=operator.itemgetter(1)))









































