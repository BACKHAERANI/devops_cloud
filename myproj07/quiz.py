def mysum2(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10


# 가변인자


def mysum(*args):
    print("args:", args)
    return sum(args) + 10  # 튜플 args=tuple


print(mysum())
print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))

