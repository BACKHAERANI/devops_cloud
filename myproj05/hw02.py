# 멜론 TOP100 리스트에서

# 좋아요수가 제일 많은/작은 곡


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
print("좋아요 수가 가장 많은 곡과 작은 곡은?")


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)
for song_dict in sorted_song_list[0:1]:
    print("[가장 많은 곡] {artist} {title} [{like}]".format(**song_dict))
for song_dict in sorted_song_list[99:100]:
    print("[가장 적은 곡] {artist} {title} [{like}]".format(**song_dict))


# 곡명 단어수가 가장 많은 곡/작은곡

print("곡명 단어수가 가장 많은 곡과 적은 곡은?")


t_list = []


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    t_list.append((song_dict["title"], len(song_dict["title"].split(" "))))

sorted_t_list = sorted(t_list, reverse=True, key=lambda x: x[1])

for title_dict in sorted_t_list[0:1]:
    print("[가장 많은 곡]", title_dict)
for title_dict in sorted_t_list[99:100]:
    print("[가장 적은 곡]", title_dict)


# 곡명 글자수가 가장 많은 곡/작은곡

print("곡명 글자수가 가장 많은 곡/작은곡?")


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


t_list = []


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    t_list.append(song_dict["title"])

print("[가장 많은 곡]", max(t_list, key=lambda s: (len(s))))
print("[가장 작은 곡]", min(t_list, key=lambda s: (len(s))))
