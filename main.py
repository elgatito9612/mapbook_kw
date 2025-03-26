users:list=[
    {"name":"Kaja","location":"Tomaszów Lub.","posts":69},
    {"name":"Wiktoria","location":"Chełm.","posts":6},
    {"name":"Sabina","location":"Opole","posts":110},
    {"name":"Weronika","location":"Tomaszów Maz.","posts":350},
    {"name":"Oliwka","location":"Warszawa","posts":420},

]

print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował(a) {user["posts"]} postów.")
