# Alizon Martinez
# 11/11/26
# Create dictionary

contact_info = {
    "name": "Alizon Martinez",
    "address": "123 Main Street",
    "city": "Salt Lake City",
    "state": "UT",
    "zip": "84101"
}

print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

del contact_info["name"]

full_name = {
    "first name": "Alizon",
    "last name": "Martinez"
}

full_name.update({
    "honorific": "Ms."
})

contact_info.update({
    "full_name": full_name
})

print(f"""
{contact_info['full_name']['honorific']}
{contact_info['full_name']['first name']}
{contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

