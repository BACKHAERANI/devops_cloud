//객체복사


const obj1 = { "value1": 10 };

const obj2 = obj1;   //얕은 복사


//깊은 복사를 하는 방법 중의 하나. 깊은 복사를 지원하는 다양한 JS라이브러리가 있다
//아래 방법은 가장 무식한 방법

const json_string = JSON.stringify(obj1)
const obj3 = JSON.parse(json_string);



obj1.value1 += 1;

console.log(obj1);
console.log(obj2);
console.log(obj3);

//지정속성이 없으면 undefined를 반환
// console.log(obj1.name);

// function fn() { }
// console.log(fn());

// obj1["value1"]
// obj1.value1

// obj1["p-1"]
// //obj1.p-1