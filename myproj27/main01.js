
const { melon_data: song_array } = require("./melon_data");


// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort


// array의 sort는 자신의 순서도 변경하고 자신을 반환하는데
// 파이썬의 list sort는 리스트 자신의 순서만 변경하고 리턴값이 없다
song_array.sort(
    (song1, song2) => song1.like - song2.like,
);



//-1
for (const song of song_array) {
    console.log(song.like, song.title);
}

//-2
// for (const { like, title } of song_array) {
//     console.log(like, title);
// }