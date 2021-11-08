hw = """1이상 100미만 범위에서 3과 5의 공배수를 모두 출력하기 
(공배수 : 2개 이상의 자연수의 공통인 배수)"""

print(hw)

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
