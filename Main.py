import streamlit as st

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")



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

import streamlit as st
import read_data

person_dict = read_data.load_data()
person_names = read_data.get_person_list()
st.session_state.current_user = st.selectbox("Versuchsperson", person_names)

