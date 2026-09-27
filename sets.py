#set is a collection of unordered items. each collection in the set must be unique and immutable
nums = {1,2,3,4,"RishabKumar",1}
set2 = {1,2,2,2,2} #this will be (1,2)
print(nums)
print(set2)
#we cannot store dictionary and lists inside sets but we can use tuples
print(type(set2))
print(len(nums))
empty = set()#this is how empty set is made

#sets are mutable but the elements in the set are immutable
nums.add(6)
nums.remove(1)
print(nums)

set2.clear()
set2.add("empty")
print(set2)

nums.pop()#it removes a random value
print(nums)

print(nums.pop())

print(nums.union(set2))#this is how we can use union 
print(nums.intersection(set2))#this is how we can use intersection of a set
