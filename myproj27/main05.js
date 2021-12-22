const { melon_data: song_array } = require("./melon_data");


// TODO: #4 좋아요수가 200,000 이상인 곡명만 오름차순 정렬 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

function compare_String_for_sort(string1, string2, is_ascending = true) {
    if (string1 < string2) { return is_ascending ? -1 : 1; }
    else if (string1 > string2{
        return is_ascending ? 1 : -1;
    }
    else { return 0; }
)
}


const filtered_song_array = song_array
    .filter(({ like }) => like >= 200_000);
    .sort((song1, song2) => {
        if (song1.title < song2.like) {
            return -1;
        }
        else if (song1.title > son2.title) {
            return 1;
        }
        else { return 0; })  
}


//오름차순
// song1이 song2보다 크다면 음수를 반환, 
// song1이 song2보다 작다면 양수를 반환, 
//내림차순
// song1이 song2보다 크다면 양수를 반환 , 
// song1이 song2보다 작다면 음수를 반환 , 
//같으면 0을 반환


const new_song_array = song_array.filter(({ like }) => like >= 200_000)
    .sort((song1, song2) => { return compare_String_for_sort(song1.title, song2.title, true) });


for (const song of filtered_song_array) {
    console.log(`[${song.like}] ${song.title} ${song.artist}`);
}