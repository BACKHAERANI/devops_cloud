import PageAbout from "./pages/PageAbout";
import PageCounter from './pages/PageCounter';
import PageLotto from "./pages/PageLotto";
import TopNav from "./components/TopNav";
import { useState } from "react";
import PageYoutube from "./pages/PageYoutube";

function App(){
  const [pageName, setPageName] =useState('about');
  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };
 return (
  <div>
  <h1>백해란의 리액트</h1>
  {/* <button onClick={changePageName}>페이지 토글</button> */}
  <TopNav changePageName = {setPageName}/>
  {pageName ==="about" && <PageAbout/>}
  {pageName ==="counter" && <PageCounter />}
  {pageName ==="Lotto" && <PageLotto />}
  {pageName === "playlist" && <PageYoutube />}
</div>
 );
}

export default App;
