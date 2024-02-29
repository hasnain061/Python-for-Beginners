numbers = [2,2,3,4,5,6,3,1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
