name = input('Write Name : ')
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 30:
    print("Name must be a maximum of 30 characters.")
else:
    print("Name looks Good!")
