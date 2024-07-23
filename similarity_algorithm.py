# Create a search bar algorithm, that queries the Database
# Displays/prints from most similar to least similar Using first_name and last_name

name = ["Percy Lushaba", "Percival Sibiya", "Bheki Lushaba", "Peaches Khoza", "Percy Stander"]

def search(names, first_name, last_name):
    
    first_name = first_name.lower()
    last_name = last_name.lower()
    Searched = []

    for name in names:
        Rating = 0
        Name = ""
        Name += name
        Name_lower = Name.lower()

        if first_name in Name_lower and last_name in Name_lower:
            Rating += 1
            Searched.append({"Name": Name.strip(),"Rating": Rating})
        else:  
            if first_name in Name_lower:
                Rating += 0.5
                Searched.append({"Name": Name.strip(),"Rating": Rating})
                    
            elif last_name in Name_lower:
                Rating += 0.5
                Searched.append({"Name": Name.strip(),"Rating": Rating})
        
    print(Searched)


first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

search(name, first_name, last_name)