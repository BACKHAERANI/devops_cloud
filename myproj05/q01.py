import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


t_list = []


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    t_list.append(song_dict["title"])

print(max(t_list, key=lambda s: (len(s))))
print(min(t_list, key=lambda s: (len(s))))
