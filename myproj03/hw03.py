hw = """1이상 100미만 범위에서 3과 5의 공배수를 합을 출력하기"""

print(hw)

ran = 0

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        ran += number
print(ran)
