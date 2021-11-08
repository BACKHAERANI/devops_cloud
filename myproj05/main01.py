import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        # print(song_dict["artist"], song_dict["title"], song_dict["like"])

        line = "{}, {}, {}".format(
            song_dict["artist"], song_dict["title"], song_dict["like"]
        )
        line = "{가수명}, {곡명}, {좋아요수}".format(
            가수명=song_dict["artist"], 곡명=song_dict["title"], 좋아요수=song_dict["like"]
        )
        line = "{artist}, {title}, {like}".format(
            artist=song_dict["artist"], title=song_dict["title"], like=song_dict["like"]
        )
        # unpack arguments
        line = "{artist}, {title}, {like}".format(**song_dict)  # dict에서만 사용 가능
        print(line)


artist_list = [song_dict["artist"] for song_dict in so_list]

# fmt:on

counter = counter(artist_list)

for artist in counter:  # key
    print(artist)


for artist in counter.values():  # values
    print(song_count)



for artist in counter:
    print(artist, counter[artist])  #잘안쓴다


 for artist, song_counter in counter.items() :   #제일좋음
     print(artist, song_count)
