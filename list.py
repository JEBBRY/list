lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']
print(lst)
print("Length of the list is: ", len(lst))
print("First element of the list is: ", lst[0])
print("Last element of the list is: ", lst[-1])

lst.append('Papaya')
print("Updated List: ", lst)

lst.remove('Guava')
print(" Updated List : ", lst)

lst.sort()
print("Sorted List: ", lst)

lst.pop(1)
print("Updated List: ", lst)

lst.reverse()
print("Reversed List: ", lst)

print("Multiplication on list: ", lst * 2)

lst = lst[:4]
print("Sliced List: ", lst)

lst.clear()
print("Updated  List: ", lst) 