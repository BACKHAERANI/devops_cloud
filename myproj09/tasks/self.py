def check_available(received_text: str):
    return received_text == "메뉴를 추천해줘"

def make_response(received_text: str) -> str:
    return "그런 건 네가 알아서 해!"