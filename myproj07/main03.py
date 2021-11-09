"""
멜론 top 100 리스트에서

1. 좋아요가 가장 많은/적은곡?
2. 곡명 단어수가 가장 많은/적은곡?
3. 곡명 글자수가 가장 많은/적은곡?

"""

from pprint import pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 1.


# 1-(1)
def peek_like_for_song(song_dict):
    return song_dict["like"]


song_dict = max(song_list, key=peek_like_for_song, default=None)
if song_dict == None:
    print("노래목록이 비었습니다.")
pprint(song_dict)


# 1-(2)

try:
    song_dict = max(song_list, key=peek_like_for_song)

except ValueError:
    print("노래목록이 비었습니다.")

else:
    print(song_dict)


# 1-(3)

if song_list:
    song_dict = max(song_list, key=peek_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다")


# 2
