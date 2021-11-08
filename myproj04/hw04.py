# 가수별 곡수를 출력해보세요


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


artist_list_dict = {}

for song in song_list:
    if song["artist"] in artist_list_dict:
        artist_list_dict[song["artist"]] += 1
    else:
        artist_list_dict[song["artist"]] = 1


print(artist_list_dict)


# #  원래하고 싶었던 방법
# # 1.song_list에서 artist_list만 추출한다.
# # 2.artist_list를 오름차순으로 정렬한다.
# 3. artist_list 위에서부터 다른 이름이 나올 때까지 더한다.
# 4. 다른 이름이 나오면 =1를 생성한다.
# 5. 3,4를 반복한다.
