person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}


print(f"Imię: {person["name"]}")
print(" ")
print(f"Hobby: {person['hobby'][0]}, {person['hobby'][1]}")

# for key,value in person.items():
#     print(f"{key}: {value}")
    
person['surname'] = "Nowak"
person['married'] = False
person['gender'] = "Male"
person["hobby"].append("Bicycle")
person['phone']['work'] = "313131444"
print(" ")
for key,value in person.items():
    print(f"{key}: {value}")