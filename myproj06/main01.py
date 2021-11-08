"""
"방탄소년단" 곡명만 출력하기
곡명에 "사랑"이 포함된 곡명만 출력하기
"좋아요" 수가 200,000 이상인 곡명만 출력하기
"""
from pprint import pprint
from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


"""'
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들기

"""




def check_bts_song(song_dict):
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


# """
# bts 노래라면 true를 반환합니다.
# """

 new_sing_list: List[dict] = []

# for song_dict in song_list:
#     if check_bts_song(song_dict):
#         new_song_list.append(song_dict)

# pprint(title_list)


filter(check_bts_song, song_list)

new_song_llist = list(filter(check_bts_song, song_list))
print(new_song_list)

"""
곡명에 사랑이 포함된 곡들의 곡명 리스트를 만들어보세요.

"""

def check_contains_love(song_dict):
    title:str = song_dict["title"]
    return "사랑" in title

for song_dict in filter(check_contains_love, song_list):
    print("{rangk} {title} {artist}"format(**song_dict))



# title_list: List[str] = []

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     if "사랑" in title:
#         title_list.append(title)

# print(title_list)


"""

좋아요수가 200000이상인 곡명의 리스트를 만들어보세요.

"""

def check_above_200000(song_dict):
    like:int=song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200000, song_list):
    print ("{title} - {like}".format(**song_dict) ")



# title_list

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     if like >= 200_000:
#         title_list.append(title)

# print(title_list)


# title_list: List[str] = []

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         title: str = song_dict["title"]
#         title_list.append(title)

# print(title_list)
