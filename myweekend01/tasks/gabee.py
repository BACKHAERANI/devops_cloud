import requests
from bs4 import BeautifulSoup

def check_available(received_text: str) -> bool:
    return received_text == "가비인스타"

def make_response(received_text: str, html: str = None) -> str:
    if html is None:
        url=
        response = requests.get(url)
        html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.select_one("").text

tag_list = soup.select("")
