hw = """구구단 퀴즈 break 없는 버전"""

print(hw)


for number in range(2, 10):
    for i in range(1, 10):
        if number >= i:
            print(f"{number}*{i}={number*i}")
