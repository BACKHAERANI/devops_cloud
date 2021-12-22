import json

open("melon_data.json", "rt") as f:
song_list = json.loads(f.read())

song_list.sort(key=lambda song:song['like'], reverse=True)


for song in enumerate(song_list[:10], 1):
    print("{index}[{like}]{title} by {artist}".format(index=index, **song))
