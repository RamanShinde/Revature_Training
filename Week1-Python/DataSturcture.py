#List
print("<----------------List------------------->")
number=[10,20,30]
print(number[0])
print(number[1])
print(number[2])

#it gives the id of nummber
print(id(number))
#Append() add at last
number.append(40)
print(number)
# gives the indes of any object
print(number.index(20))
# count occurenece of number
print(number.count(40))
#It insert the element where we want
number.insert(2, 15)
print(number)
number.insert(0,90)
print(number)
#It reverse the number
number.reverse()
print(number)
# it Sort the array
number.sort(reverse=True)
print(number)
print(number.pop(1))

#when we want to add the another list then use extend().
number1=[50,60,70,80]
number.extend(number1)
print(number)

#clear():-It make empty the list
number1.clear()
print(number1)

#for delete the list from memory then use Del
del(number1)


print("<----------------Tuple------------------->")
#Represent ()
#Imutable,allow duplicate
tupl1=(1,2,3,4)
print(tupl1[0])
print(tupl1[2])
print(tupl1[1])
print(tupl1[3])
#it has only two methode count() and index()
#Beacuse tuple is imutable so that why it has only two method
#That means we can do operation 

print("Count of 2 number:-",tupl1.count(2))
print(tupl1.index(1))

print("<----------------Set------------------->")
#set:-{},no duplicate,mutable(can be modified),no index/no order
set1={22,11,33,55,9,7}
print(set1)
set1.add(55)
print(set1)
set1.add(28)
print(set1)
set2={11, 44, 33, 66}
#Just unino of two set all element add in set3
set3=set1.union(set2)
print(set3)
#just common element list
set4=set1.intersection(set2)
print(set4)

set5=set1.difference(set4)
print(set5)

print("<----------------Dictonory------------------->")
#store K:V (key value) like map,mutable,named index by key,modification allowed

dict1={1:10,2:20,3:30,4:40}
print(dict1)
#To access use the key the value
print(dict1[1])

dict2={'rno':'123','name':'Raman'}
print(dict2)
print(dict2["rno"])
dict2['phn']=7058837256
print(dict2)
print("Number:-",dict2.get('phn'))
print(dict2.keys())
print(dict2.values())
print("Pop the pop",dict1.pop(2))