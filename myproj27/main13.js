const { melon_data: song_array } = require("./melon_data");


// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.


// //-1
// song_array
//     .filter(({ artist }) => artist === '방탄소년단')
//     .reduce((acc, song) => {
//         if (!acc)
//             return song;
//         else if (acc.like < song.like)
//             return song;
//         else
//             return acc;
//     }, null);

// //acc:null 곡1.like=100 => 곡1
// //acc:곡1(100) 곡2(200) => 곡2

// //-2
// const top_song = song_array
//     .filter(({ artist }) => artist === '방탄소년단')
//     .reduce((acc, song) => {
//         if (!acc || acc.like < song.like)
//             return song;
//         else
//             return acc;
//     }, null);

// console.log(top_song);

// //-3
// const top_song = song_array
//     .filter(({ artist }) => artist === '방탄소년단')
//     .reduce((acc, song) => {
//         return acc.like < song.like ? song : acc;
//     });

// console.log(top_song);


//-4 랭크가 제일 큰 곡

Array.prototype.max = function (key_fn) {
    return this.reduce((acc, song) => {
        key_fn(acc);
        key_fn(song);
        return key_fn(acc) < key_fn(song) ? song : acc;
    });
}

const top_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .max(song => song.like);

console.log(top_song);