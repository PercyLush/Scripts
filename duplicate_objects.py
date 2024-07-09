test_list = [

    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    },
    {
        "Name": "Zusakhe",
        "Surname": "Mbebe",
        "Age": 27
    },
    {
        "Name": "Kagiso",
        "Surname": "Lushaba",
        "Age": 25
    },
    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    },
    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    },
    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    },
    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    },
    {
        "Name": "Bheki",
        "Surname": "Lushaba",
        "Age": 22
    }
]
new_list = []

for items in range(len(test_list)):
    for item in range(0, len(test_list) - items - 1):
        if test_list[items]["Name"] == test_list[item]["Name"]:
            pass
        else:
            new_list.append(test_list[items])

print(new_list)