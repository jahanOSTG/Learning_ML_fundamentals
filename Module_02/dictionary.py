# key and value
guest={
    "name": "Janie",
    "age": 25,
    "favourite_snack": "Cake"
}

print("Guest name :",guest["name"])
print("Guest age :",guest["age"])

guest["favourite_color"]="Black"
print(guest)

guest.pop("age")
print(guest)

for key,val in guest.items():
    print(key,val)

party_guests={
    "guest1" : {"name" : "Janie","favourite_snack": "Cake"},
    "guest2" : {"name" : "Antor","favourite_snack" :["chips","choco"]}
}
print(party_guests["guest2"]["favourite_snack"][0])