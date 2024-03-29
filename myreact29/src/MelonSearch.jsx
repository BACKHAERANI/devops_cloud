import { Input } from 'antd';
import { useState } from 'react';
import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';
import { List, Card } from 'antd';


function MelonSearch() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };

  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        // ALBUMCONTENTS, ARTISTCONTENTS
        const {
          data: { SONGCONTENTS: searchedSongList },
        } = response;

        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();

        setSongList(searchedSongList);
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();
      });
  };

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      {songList.map((song) => {
        return (
      
            <List
              grid={{ gutter: 16, column: 2 }}
              dataSource={songList}
              renderItem={(song)=> (
                <List.Item>
                  <Card title=
                  {<img src={song.ALBUMIMG}/>}>
                  {song.ARTISTNAME}
                    {song.SONGNAME}
                    
                    </Card>
                </List.Item>
              )}
            />
        );
    })}
    </div>
  );
}
export default MelonSearch;