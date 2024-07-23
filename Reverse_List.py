def insert_list():
    my_list = [1, 2, 3]
    for v in range(len(my_list)):
        my_list.insert(1, my_list[v])
    print(my_list)


    new_list = [1, 2, 3, 4]
    print(new_list[-3:-2])

numbers = [9, 0, 3, 2, 5, 6, 1, 4, 8, 7, 10]


def bubblesort(number):

    swapped = True # Dummy To ensure the while loop runs

    while swapped:
        swapped = False
        for x in range(len(number) - 1):
            if number[x + 1] > number[x]: #Descending order
                swapped = True
                number[x], number[x + 1] = number[x + 1], number[x]
    print(number)
                

bubblesort(numbers)