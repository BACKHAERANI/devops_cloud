// const [name, ...rest] = ["Tom", 10, "seoul"]

// console.log(name);
// console.log(rest);

const numbers = [1, 2, 3]

const new_numbers = [
    10, 20, 30,
    ...numbers,
    40, 50, 60,
    ...numbers,
    70, 80, 90,
    ...numbers,
];

console.log(new_numbers);


const steve = {
    ...tom,
    name: "steve",
};
console.log(steve);