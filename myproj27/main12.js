const { melon_data: song_array } = require("./melon_data");


// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set


// if (!acc[artist]) acc [artist] =0;    // || = or

//-1
const artist_count_object = song_array
    .reduce((acc, song) => {
        acc[song.artist] ||= 0;
        acc[song.artist] += 1;
        return acc;
    }, {});


//console.log(artist_count_object)



//-2
// const artist_count_object = song_array
//     .reduce((acc, { artist }) => {
//         acc[artist] ||= 0
//         acc[artist] += 1;
//         return acc;
//     }, {});


const total = Object.values(artist_count_object)
    .filter(count => count >= 2)
    .length;


console.log(total);