list = [1,2,7,4]
list.append(5)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

Fruits = ["Banana", "Apple", "Guava", "Litchi"]
Fruits.sort(reverse=True)#here descending order is done by alphabetical order
print(Fruits)
Fruits.reverse()#reverses the lists
print(Fruits)
list.insert(2, 9)
print(list)

list.remove(1)
print(list)
list.pop(-2)#just like remove function but with indexing
print(list)