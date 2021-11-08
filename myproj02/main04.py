import random


print("1~100사이 숫자가 주어집니다.정답을 맞혀주세요")

count = 1

a = random.randint(1, 100)

for number in range(10):
    number = int(input(">>>"))
    if a > number:
        print("더 큰 수를 입력해주세요.")
        count += 1
    if a < number:
        print("더 작은 수를 입력해주세요.")
        count += 1
    if a == number:
        print(f"{count}번만에 성공했습니다.")

if count == 10:
    print("다음 기회에...")
