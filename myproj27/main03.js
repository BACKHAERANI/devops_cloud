const { melon_data: song_array } = require("./melon_data");


// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`



//좋아요수에대한 내림차순 정렬 ->처음 10개
const like_top10_song_array = song_array.sort(
    (song1, song2) => song2.like - song1.like).slice(0, 10)



// const top10_song_array = song_array.sort(
//     (song1, song2) => song2.like - song1.like
// ).slice(0, 10);


//-1
for (const [index, song] of like_top10_song_array.entries()) {
    console.log(`${index + 1} [${song.like}] ${song.title} by ${song.artist}`);



// for (const {like, title, artist} of like_top10_song_array.entries()) {
//     const rank = index + 1;
//     console.log(`${rank} [${like}] ${title} by ${artist}`);    