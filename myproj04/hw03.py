# 좋아요 수가 200000이 넘는 곡수는?


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

count = 0

for song in song_list:
    if song["like"] > 200000:
        count += 1

print(count)
