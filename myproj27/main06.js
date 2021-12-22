const { melon_data: song_array } = require("./melon_data");


// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`


const title_array = song_array
    .map((song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return `${song.title}/${word_count}`;
    },
    );

// const title_array = song_array
//     .map(({ title }) => `${title} / ${title.split(/\s+/).length}`);



for (const title of title_array) {
    console.log(title);
}

