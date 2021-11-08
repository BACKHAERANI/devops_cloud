for collections import counter    
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
print(song_list)




#과제1

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["artist"])



#과제2

for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])


#과제3

song_count=0

for song_dict in song_list:
    if song_dict["like"] >200_000:
        song_count+=1
        
print(song_count)



#과제4

artist_dict={}

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     #artist_list.append(artist)
#     if artist not in artist_dict:
#         artist_dict[artist] =0
#         artist+dict[artist]+=1

print(artist_dict)



#4-1

# artist_list=[]


# for song_dict in song_list:
#     artis : str = song_dict["artist"]
#     artist_list.append(artist)
    


#4-2

artist_list=[]

artist_list =[song_dict["artist"] for song_dict in song_list]
    

print(counter(artist_list))
