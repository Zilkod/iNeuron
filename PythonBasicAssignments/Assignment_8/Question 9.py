def split_full_name(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    return first_name, last_name

full_name = "Suzad Mohammad"
first_name, last_name = split_full_name(full_name)
print("First Name:", first_name)
print("Last Name:", last_name)
