hw = """ 반복문을 활용해 3단.6단.9단 구구단 출력하기"""

print(hw)

for number in range(3, 10, 3):
    for b in range(1, 10):
        print(f"{number}*{b}={number*b}")
