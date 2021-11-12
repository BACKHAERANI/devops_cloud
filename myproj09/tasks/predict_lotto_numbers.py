import random
from typing import List

def check_available(received_text: str) ->bool:
    return received_text in ("로또", "로또번호 점지해줘")

def make_response(received_text: str, candidate_numbers:List[int] = None) ->str :
    if candidate_numbers is None:
        candidate_numbers = random.sample(range(1, 46),7)
    *numbers, bonus = candidate_numbers
    predict_numbers: str = ", ".join(map(str, sorted(numbers)))
    message = f"로또번호는 {predict_numbers}이며, 보너스번호는 {bonus} 입니다."
    return message

# def test_predict_lotto_numbers():
#     assert predict_lotto_numbers.check_available("로또")
#     assert predict_lotto_numbers.check_available("로또번호 점지해줘")
#
#     candidate_numbers = [1, 2, 3, 4, 5, 6, 7]
#     response_text = predict_lotto_numbers.make_response("", candidate_numbers)
#     assert response_text == f"로또번호는 1, 2, 3, 4, 5, 6 이며, 보너스 번호는 7입니다."