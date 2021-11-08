# 멜론 TOP100리스트에서 리스트에 랭크된 가수는 총 몇팀인가요?(중복제거한 가수명 리스트의 크기)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
artist_list = []
total = 0

artist_list = df.artist.tolist()*

artist_Set = set(artist_list)
artist_list = list(artist_Set)

for singer in artist_list:
    total += 1
print(total)

# 2곡 이상 랭크된 가수는 몇 팀인가요?




# "방탄소년단의 좋아요 총 합은?"

total = 0

for song in song_list:
    if song["artist"] == "방탄소년단":
        total += song["like"]

print(total)
