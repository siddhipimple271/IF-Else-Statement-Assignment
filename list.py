# name=["riddhi", "fine","sam","radha",]
# name.append("siddhi")
# print(name)

# number=[45,43,65,2,5]
# number.insert(32,77)
# print(number)

# match=[3.3,"ram",54,"emn"]
# stud=match.copy()
# print(match)
# print(stud)

# a=[1,2,3] 
# b = a.copy()
# print(a)
# print(b)

# a = [10, 20]
# a.extend([56,78])
# print(a)

# a = [1, 2, 3]
# b=[9,8,7,5]
# a.extend(b)
# print(a)

# k=["kishor","ram","radha"]
# k.extend(["rajesh","ram"])
# print(k)    

# name=["jasmin","falower"]
# name.append("ram")
# print(name)

fruits = ["apple", "mango", "apple", "banana", "apple"]
print(fruits.count("apple"))


number=[1,1,2,1,4,5,3,7,8,2,]
print(number.count(1))

name=["raj","shiv","sam"]
print(name.index("shiv"))

number=[67,7,8,3,]
number.pop(1)
print(number)

numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(number)

number=[10,20,30,3]
number.remove(20)
print(number)

number=[20,2,8,78,22]
number.sort(reverse = True)
print(number)


name=["manago","banana","apple"]
name.sort()
print(name)

number=[2,8,4,7,2,0]
number.clear()
print(number)


number=[23,9,6,3,12]
number.reverse()
print(number)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a.__add__(b)
print(c)

a = [10, 20, 30]
b = [40, 50, 60]
c = a.__add__(b)
print(c)