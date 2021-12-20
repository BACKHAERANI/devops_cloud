def get_default_value():
    print("get_default_value()를 호출")
    return 10


# # 함수 정의 시점에 호출
# def hello(name, age=get_default_value()):
#     print(f"안녕, 나는 {name}이야, {age}살이지")


# 파이썬에서 디폴트값이 필요할 때마다 함수호출
def hello(name, age=None):
    if age is None:
        age = get_default_value()

    print(f"안녕, 나는 {name}이야, {age}살이지")


hello("Tom")
hello("Steve")
hello("John")
