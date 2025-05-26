phones_list = [
    {'city': 'Moscow', 'phone': '+7 (916) 205-41-05', 'name': 'Ivan'},
    {'city': 'Moscow', 'phone': '+7 (916) 230-00-75', 'name': 'Ivan'},
    {'city': 'Moscow', 'phone': '+7 (916) 778-71-05', 'name': 'Nikolay'},
    {'city': 'Moscow', 'phone': '232-19-55', 'name': 'Ivan'},
    {'city': 'Moscow', 'phone': '331-66-11', 'name': 'Nikolay'},
    {'city': 'Moscow', 'phone': '783-33-85', 'name': 'Nikolay'},
    {'city': 'Samara', 'phone': '+7 (916) 105-13-56', 'name': 'Anna'},
    {'city': 'Samara', 'phone': '200-11-15', 'name': 'Anna'},
    {'city': 'Vologda', 'phone': '+7 (931) 711-00-75', 'name': 'Anna'},
]

result = {}
for contact in phones_list:
    city = contact['city']
    phone = contact['phone']
    name = contact['name']

    if city not in result:
        result[city] = {}

    result[city][phone] = name

print(result)
