// //Array
// const [name] = ["Tom", 10, "seoul"];

// const [, age] = ["Tom", 10, "seoul"];

// // height는 undefined
// const [name, age, region, height] = ["Tom", 10, "seoul"];

// // 값 할당에 실패했을 때 적용되는 디폴드 값
// const [name, age, region, height = 140] = ["Tom", 10, "seoul"];

// // 디폴드값을 함수로 호출 지정
// function get_default_height() {
//     console.log("get_default_height 함수를 호출했습니다.");
//     return 140;
// }
// const [name, age, region, height = get_default_height()] = ["Tom", 10, "seoul", 150];


function get_default_height() {
    console.log("get_default_height 함수를 호출했습니다.");
    return 140;
}
const [name, age, region, height = get_default_height()] = ["Tom", 10, "seoul"];