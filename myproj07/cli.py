import requests
from bs4 import BeautifulSoup


def naver_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [{"title": tag.text} for tag in soup.select(".lst_total .total_tit")]


while True:
    line = input("Enter question (quit: q) : ")
    if line == "q":
        print("벌써 가려고?")
        break
    elif line == "야":
        print("왜?")
    elif line == "헤이":
        print("Hey~ >♡<")
    elif line.startswith("네이버 검색:"):
        query = line[7:]  # 검색어
        post_list = naver_search(query)
        print(f"=== 네이버 검색 결과 : {query} ===")
        for idx, post in enumerate(post_list, 1):
            print(f"[{idx}] {post['title']}")
    else:
        print("네가 무슨 말을 하는지 모르겠어ㅜㅜ!!!")
