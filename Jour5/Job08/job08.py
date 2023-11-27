def my_sort(lst):
 swaps = 0

 for i in range(len(lst)):
     for j in range(len(lst) - 1):
         if lst[j] > lst[j + 1]:
             lst[j], lst[j + 1] = lst[j + 1], lst[j]
             swaps += 1

 return lst, swaps

lst = [5, 3, 8, 1, 6]
sorted_lst, swaps = my_sort(lst)

print("Liste triée :", sorted_lst)
print("Nombre de coups :", swaps)
