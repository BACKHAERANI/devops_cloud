def mysum3(x, y, z):
    return x + y + z


print(mysum3(1, 2, 3))

print(mysum3(x=1, y=2, x=3))
print(mysum3(x=3, y=1, x=2))


kwargs = {"x": 1, "y": 2, "z": 3}
mysum3(**kwargs)  # unpacking

# ...


people = [
    {"name": "Tom", "age": 10, "region": "Seoul"},
    {"name": "Steve", "age": 12, "region": "Pusan"},
]

for person in people:
    print(person["name"], person["age"])
