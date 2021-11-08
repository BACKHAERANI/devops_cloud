# 곡명에 가을이 들어가는 곡명만 출력해보세요.


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])
