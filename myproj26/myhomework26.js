
const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];


//input

const { question } = require("readline-sync");      //readline-sync


// shuffle  // 이해안됨, 구글 참조

const shuffle = animal_names
    .map(a => ([Math.random(), a]))
    .sort((a, b) => a[0] - b[0])
    .map(a => a[1])


// slicing

const slicing = shuffle.slice(0, 5)


let ok_counter = 0;

const start_time = new Date();

for (random_animal_name of slicing) {
    console.log(random_animal_name);
    const input = question("please enter>>> ");

    if (input === random_animal_name) {
        ok_counter += 1;
        // ok_counter++;  둘다 되지만 위에 것만 이해됨
        console.log("정확합니다.");
    }
    else {
        console.log("오타가 있어요.");
    }
}

const end_time = new Date();

const time = end_time.getTime() - start_time.getTime();

console.log(`${ok_counter}번 성공!`);
console.log(`총 ${time / 1000}초가 걸렸습니다.`);



