const { melon_data: song_array } = require("./melon_data");


// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce




// song_array.filter(({artist}) => artist === "방탄소년단")
// .reduce((acc, {like}) => acc += like, 0);


//-1
const like_total = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => acc + song.like, 0);

console.log(`좋아요 총 합 : ${like_total}`);



//-2
Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
};


const result = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .map(({ like }) => like)
    .sum();

console.log("result:", result)








