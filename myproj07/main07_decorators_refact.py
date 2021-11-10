import time

# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:
#         time.sleep(1)  # 1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]


def memoize(fn):
    cached = {}

    def wrap(x, y):
        key = (x, y)
        if key not in cached: fn
            return cached[key]

    return wrap


@memoize
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2)

# mysum2(1,2)


@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x * y + 10


# mymultiply2 = memoize(mymultiply2)

print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))


print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))
