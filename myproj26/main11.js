const fs = require("fs");
const fspromises = fs.promises;

//await는 promise문법에 대한 축약
function main() {
    try {
        const files = await fspromises.readdir("c:/Dev");
        console.log("loaded:", files);
    }
    catch (error) {
        console.error(error);
    }
}

main();

// //1번
// const fs = require("fs");
// const fspromises = fs.promises;

// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else { console.log(files);
//      }
// });

// console.log("ENEED");


//2번
// const fs = require("fs");
// const fspromises = fs.promises;

// fspromises.readdir("c:/Dev")
//     .then(function(files){
//         console.log("loaded:", files);
//     })
//     .catch(function(error){
//         console.error(error);
//     });



// //2번-(2)

// const fs = require("fs");
// const fspromises = fs.promises;

// fspromises.readdir("c:/Dev")
//     .then(files => console.log("loaded:", files))
//     .catch(error => console.error(error));


