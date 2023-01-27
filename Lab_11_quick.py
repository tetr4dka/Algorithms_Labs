def sort(array):
    if len(array)> 1:
        pivot=array.pop()
        greater_lst, equal_lst, smaller_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                greater_lst.append(item)
            else:
                smaller_lst.append(item)
        return (sort(smaller_lst) + equal_lst + sort(greater_lst))
    else:
        return array

array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
array=sort(array)
print("Отсортированный массив: ", array)
