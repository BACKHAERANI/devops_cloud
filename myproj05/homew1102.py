from random import randint
number = randint(1,100)
#is_pass = false
 
for retry in range(10): 
    line = input(f"[{retry}]try guess number : ")
    try:
        answer = int(line. strip()or 0)   # OR 0 제외
#    # except valueError:  
#         print("잘못된 값을 입력하셨습니다")
#         continue  #for 다시 반복


    if answer == number :
        break    #가장 근접한 for 명령을 중지한다.
    elif answer < number:
        print ("더 큰 수를 입력해주세요")
    elif answer > number:
        print ("더 작은 수를 입력해주세요")
    # else:
    #     pass


else:
    print("다음기회에...")




