def test1():
    # two Lists with names
    # find the names that is not in both list, but is in one of the lists
    name1 = ["Zuks", "Kagiso", "Bheki"]
    name2 = ["Zuks", "Kagiso", "Lusani"]
    name3 = []

    for num in range(len(name1)):
        if name1[num] not in name2:
            name3.append(name1[num])

        if name2[num] not in name1:
            name3.append(name2[num])
    print(name3)


def test2(word):
    # biggest("ABBACD")
    # Output : B
    letters = list(word)
    no_duplicates = set(word)
    completed_list = []
    for key in no_duplicates:
        counter = 0
        for letter in letters:
            if key == letter:
                counter += 1
        my_words = {key: counter}
        completed_list.append(my_words)
    print(completed_list)

def palindrome(word):

    letters = list(word)
    my_list = []
    my_word = ""
    for letter in letters:
        my_list.insert(0, letter)

    for num in my_list:
        my_word += num

    if word == my_word:
        return True
    else:
        return False
    

import textwrap

def wrap(string, max_width):
    my_word = ""

    wrapper = textwrap.TextWrapper(width=max_width)
    wrap_list = wrapper.wrap(string)

    for word in wrap_list:
        my_word += f"{word}\n"
    return my_word.strip()


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

