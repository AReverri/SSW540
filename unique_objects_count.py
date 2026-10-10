objects = []

number = int(input("How many objects? "))

for i in range(number):
    name = input("Enter object name: ")
    objects.append(name)

print("Objects:", objects)

unique_objects = []

for item in objects:
    count = 0
    for other in objects:
        if item == other:
            count = count + 1

    if count == 1:
        unique_objects.append(item)

if len(unique_objects) == 0:
    print("No unique objects found.")
else:
    print("Unique objects:", unique_objects)
    print("Number of unique objects:", len(unique_objects))

    #https://github.com/AReverri/SSW540