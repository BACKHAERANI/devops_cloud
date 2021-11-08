# import pandas as pd

# df = pd.read_csv("https://bit.ly/3nsLDXy")
# song_list = list(df.T.to_dict().values())
# t_list = []


# def filter_fn1(song_dict):
#     return song_dict["title"]


# for song_dict in filter(filter_fn1, song_list):
#     t_list.append(len(song_dict["title"].split(" ")))


# new_list = sorted(t_list, reverse=True)


# print(new_list)

# # sorted_t_list = sorted(t_list, reverse=false)


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
t_dict = []


def filter_fn1(song_dict):
    return song_dict["title"]


for song_dict in filter(filter_fn1, song_list):
    t_dict.append((song_dict["title"], len(song_dict["title"].split(" "))))

sorted_t_list = sorted(t_dict, reverse=True, key=lambda x: x[1])

for new_dict in sorted_t_list[:10]:
    print(new_dict)
