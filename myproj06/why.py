# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 좋아요 수와 제목글자수의 곱을 출력해보세요.
# 1) for/if로 구현
# 2) filter/map 위주로 구현


# import pandas as pd

# df = pd.read_csv("https://bit.ly/3nsLDXy")
# song_list = list(df.T.to_dict().values())

# value_list = []

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if len(artist) >= 3:
#         value: int = song_dict["like"] * len(song_dict["artist"])
#         value_list.append(value)

# for value in value_list:
#     print(value)


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

new_song_list: list[dict] = []

for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        new_song_list.append(dict(song_dict, value=value))
        # new_song_list.append({"title": song_dict ["title"], "artist" :song_dict["artist"] "like": song_dict["like"], "album": song_dict["album"],"rank": song_dict["rank"], "value": value,})

for song_dict in new_song_list:
    print("{title} / {value}".format(**song_dict))
