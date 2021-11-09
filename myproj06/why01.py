# 2곡 이상 랭크된 아티스트 리스트 만들기
from pprint import pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


artist_dict = {}

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1


pprint(artist_dict)


# list(map(lambda x: str(x) if x>=2 else x, artist_dict))
