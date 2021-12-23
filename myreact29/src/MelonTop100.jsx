//바뀌지 않는 데이터

import { useState } from "react";
import initialSongList from "data/melon_data.json";
import {Button as BootstrapButton} from 'react-bootstrap';
import {Button as AntdButton} from 'antd';
import Axios from 'axios';
import 'MelonTop100.css';


function MelonTop100(){
    const [songList, setSongList] = useState([]);
    const handleClick1 = () => {setSongList(initialSongList);};
    const handleClick2 = () => {
      const url="https://antigravity-daejeon-2021.herokuapp.com/api/melon/"
      Axios.get(url).then((response) =>{
          const{data} = response;
          setSongList(data);
    //   console.log('응답을 받았습니다.'); 
    //   console.log(response);
  })
  .catch((error) => {
      console.error(error);
  });
  };

  const handleClick3 =()=>{
      setSongList([]);
  };

    return(

        <div>
          <h2>멜론 top 100</h2>
          <BootstrapButton variant="success" onClick={handleClick1}>파일 로딩</BootstrapButton>
          <AntdButton type="primary" onClick={handleClick2}>서버 로딩</AntdButton>
          <AntdButton type="dashed" onClick={handleClick3}>클리어</AntdButton> 

            <ul className="songList">
                {
                    songList.map((song) => {
                        return <li key={song.song_no}>
                          [{song.rank}] {song.title} _ {song.artist} ❤{song.like} </li>
                    })
                }
            </ul>
        </div>
    );
}

export default MelonTop100;