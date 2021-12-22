const { melon_data: song_array } = require("./melon_data");


// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.


// const top_like_song = song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, song) => {
//         if (!acc || acc.like > song.like)
//             return song;
//         return acc;
//     }, null);


// console.log(top_like_song);


//-2 랭크가 제일 적은 (높은) 곡

Array.prototype.min = function (key_fn) {
    return this.reduce((acc, song) => {
        key_fn(acc);
        key_fn(song);
        return key_fn(acc) > key_fn(song) ? song : acc;
    });
}

const top_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .min(song => song.like);

console.log(top_song);
