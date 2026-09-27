n = int(input())
list = []
for i in range(n):
    a = input("station name: ")
    list.append(a)
#using slicing to rotate the stations for 3 units
rotated_list = list[3:] +  list[:3]
print(rotated_list)