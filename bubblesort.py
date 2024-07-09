my_list = [8, 10, 6, 2, 4, 1, 3, 5, 9, 7]
is_swapped = True

while is_swapped:
    is_swapped = False

    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            is_swapped = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)