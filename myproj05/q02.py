import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


artist_dict = {}

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1
