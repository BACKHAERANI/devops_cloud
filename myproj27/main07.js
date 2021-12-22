const { melon_data: song_array } = require("./melon_data");


// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]


// const bts_title_array = song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .map(({ title }) => title);


// for (const title of bts_title_array) {
//     console.log(title);
// }


///reduce

// const numbers = [1, 2, 3, 4, 5]

// const result_sum = numbers.reduce((acc, number) => {
//     acc += number;
//     return acc;
// }, 0);


// console.log(`합: ${result_sum}`);

const numbers = [1, 2, 3, 4, 5]

// const new_numbers = numbers.reduce((acc, number) => {
//     acc.push(number * number);
//     return acc;
// }, []);

// console.log(new_numbers)


const new_number_object = numbers.reduce((acc, number) => {
    acc[number] = number * number;
    return acc;
}, {});

console.log(new_number_object)