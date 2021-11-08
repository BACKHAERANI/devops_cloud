# 멜론 TOP100리스트에서 "TITLE" 단어수 출력하기

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    print(song_dict["title"], len(song_dict["title"].split(" ")))


# "곡명" 단어수로 TOP10곡명 출력하기 (우선순위)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
t_list = []


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    t_list.append((song_dict["title"], len(song_dict["title"].split(" "))))

sorted_t_list = sorted(t_list, reverse=True, key=lambda x: x[1])

for new_list in sorted_t_list[:10]:
    print(new_list)
