input_data = {"Name": "", "Surname": "", "Year of birth": "", "City": "", "Email": "", "Phone Number": ""}

for i in input_data.keys():
    input_data[i] = input(f"Enter {i}- ").split()

def params(name, surname, year, city, email, phone):
    print(f"{name[0]} {surname[0]} was born in {year[0]} in {city[0]}. Contacts: {email[0]}, {phone[0]}")

params(*input_data.values())