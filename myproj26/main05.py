# list
# 항상 좌항과 우항의 변수가 같아야 함

name, age, region = ["Tom", 10, "seoul"]

name, *extra = ["Tom", 10, "seoul"]

name, *__ = ["Tom", 10, "seoul"]

__, age, __ = ["Tom", 10, "seoul"]
