# name, *rest = ["Tom", 10, "seoul"]

# print(name)
# print(rest)


numbers = [1, 2, 3]
new_numbers = [*numbers, 10, 20, 30 * numbers, 40, 50, 60 * numbers, 70, 80, 90]


print(new_numbers)

tom = {
    "name": "Tom",
    "age": 10,
    "region": "seoul",
}

# steve는 tom과 age/region 이 같아서
# tom을 참조하여 name만 변경해서
# 새로우 steve를 만든다

steve = dict(tom, name="steve")
print(steve)
