const { melon_data: song_array } = require("./melon_data");


// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set





// const artist_array = song_array.map(({ artist }) => artist);
// const artist_set = new Set(artist_array).size;       //new set 집합으로 만들고 .size(집합은 중복값이 제거됨)

// console.log(artist_set)





const artist_array = song_array.map(({ artist }) => artist);
const total1 = new Set(artist_array).size;

console.log(`랭크된 가수는 ${total1}팀입니다.`);


const total2 = song_array
    .reduce((acc, { artist }) => {
        acc.add(artist);
        return acc;
    }, new Set())
    .size;

console.log(`artist_count:`, total2);
