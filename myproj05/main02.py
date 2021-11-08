# 좋아요 수 top10 뽑기


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


# 정렬을 하려면 각 값들의 대소비교가 가능해야 한다.
# 10<100  '가'<'나' - 가능
# {"a":1}<{"b":3} - 불가

sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)


for song_dict in sorted_song_list[
    :10
]:  # [] 0:10   - 0에서부터 10개 뽑아줘 (0)  0에서부터 10까지 뽑아줘(x)
    print("[{like}] {title} {artist}".format(**song_dict))


# key=
# reverse = true

# def sort_fn(value):
#     reture value


# sorted()
