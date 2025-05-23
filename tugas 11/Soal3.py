def jumlahkan_2_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

print(jumlahkan_2_list([78, 28, 32], [46, 25, 96]))  
