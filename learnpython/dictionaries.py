# re-learning dictionaries even though i can do it incidentally in the past

# phonebook = {}
# phonebook["Vero"] = 6282333807624
# phonebook["Doi"] = 6282333807622

# print(phonebook)

phonebook = {
    "Vero" : 6282333807624,
    "Doi" : 6282333807622
}

print(phonebook)

#########
## iterating dictionaries

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#########
## remmoving value

# del phonebook["Doi"]
# print(phonebook)

#########
# exercise

# adding someone into phonebook
# removing Doi from phonebook

phonebook["Someone"] = 6282333807623
del phonebook["Doi"]

if "Someone" in phonebook:
    print("Someone is in phonebook")

if "Doi" not in phonebook:
    print("Doi is not in phonebook anymore")