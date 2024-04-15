import json

# Opening JSON file
file = open("person_db.json")

# Loading the JSON File in a dictionary
person_data = json.load(file)
print(person_data)

def load_person_data():
    file = open("person_db.json")
    person_data = json.load(file)
    return person_data

import json

def load_data():
    with open('person_db.json', 'r') as file:
        data = json.load(file)
    return data

def get_person_list():
    data = load_data()
    person_list = []
    for person in data:
        full_name = f"{person['firstname']} {person['lastname']}"
        person_list.append(full_name)
    return person_list

if __name__ == "__main__":
    person_list = get_person_list()
    print(person_list)



